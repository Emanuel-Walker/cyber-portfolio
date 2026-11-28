# compute.tf
# Why: we need one EC2 host for two reasons. (1) attack scenario 02 pivots
# from the EC2 instance profile to the over-privileged role. (2) scenario
# 01 runs the "stolen token" API calls from somewhere, and running them
# from a VPS makes the user-agent and source-IP realistic.
# How: smallest-possible t3.micro, Amazon Linux 2023, SSM-managed so you
# never need SSH.

data "aws_ami" "al2023" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-2023.*-x86_64"]
  }
}

resource "aws_instance" "lab" {
  ami                    = data.aws_ami.al2023.id
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.ec2.id]
  iam_instance_profile   = aws_iam_instance_profile.ec2.name

  # Why: encrypt even the lab root volume. Cheap habit, matters for findings.
  root_block_device {
    encrypted   = true
    volume_size = 10
    volume_type = "gp3"
  }

  metadata_options {
    # IMDSv2 only. Scenario 02 still works, but we are not shipping
    # with the known-bad IMDSv1 default.
    http_tokens                 = "required"
    http_endpoint               = "enabled"
    http_put_response_hop_limit = 2
  }

  user_data = <<-EOF
    #!/bin/bash
    # Minimal user data. Install awscli v2, boto3, and jq so an operator
    # can run the attack scripts from the box if they want to.
    dnf -y install python3-pip jq
    pip3 install boto3 awscli
    echo "lab host ready" > /var/log/lab-ready.log
  EOF

  tags = {
    Name = "${local.name_prefix}-ec2"
  }
}
