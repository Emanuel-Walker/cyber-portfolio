# vpc.tf
# Why: GuardDuty VPC Flow Logs analysis needs an actual VPC. The EC2 host
# needs a subnet. We keep this as minimal as possible to keep cost near zero.
# How: one VPC, one public subnet, IGW, route table. No NAT gateway (that
# costs real money and we do not need outbound-from-private for the lab).

resource "aws_vpc" "lab" {
  cidr_block           = "10.42.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "${local.name_prefix}-vpc"
  }
}

resource "aws_internet_gateway" "lab" {
  vpc_id = aws_vpc.lab.id
  tags   = { Name = "${local.name_prefix}-igw" }
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.lab.id
  cidr_block              = "10.42.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "${var.region}a"

  tags = { Name = "${local.name_prefix}-public" }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.lab.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.lab.id
  }

  tags = { Name = "${local.name_prefix}-public-rt" }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

# Why: VPC Flow Logs are one of the cheapest and most useful detection
# inputs you can enable. We send them to CloudWatch rather than S3 to
# keep the lab simple.
resource "aws_flow_log" "vpc" {
  log_destination      = aws_cloudwatch_log_group.vpc_flow.arn
  log_destination_type = "cloud-watch-logs"
  iam_role_arn         = aws_iam_role.flow_log.arn
  traffic_type         = "ALL"
  vpc_id               = aws_vpc.lab.id
}

resource "aws_cloudwatch_log_group" "vpc_flow" {
  name              = "/aws/vpc/${local.name_prefix}-flow"
  retention_in_days = 7
}

resource "aws_iam_role" "flow_log" {
  name = "${local.name_prefix}-flow-log-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = { Service = "vpc-flow-logs.amazonaws.com" }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "flow_log" {
  name = "flow-log-write"
  role = aws_iam_role.flow_log.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogStreams"
      ]
      Resource = "${aws_cloudwatch_log_group.vpc_flow.arn}:*"
    }]
  })
}

# Security group for the lab EC2. Only the operator CIDR gets in on 22.
resource "aws_security_group" "ec2" {
  name        = "${local.name_prefix}-ec2-sg"
  description = "Lab EC2 ingress from operator only"
  vpc_id      = aws_vpc.lab.id

  ingress {
    description = "SSH from operator"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.allowed_source_cidr]
  }

  egress {
    description = "all out"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
