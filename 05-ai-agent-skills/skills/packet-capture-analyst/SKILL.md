---
name: packet-capture-analyst
description: >-
  Use when someone has a question about a PCAP file or network traffic and needs
  the exact Wireshark filters and clicks to find the answer, for labs, portfolio
  write-ups, CTFs, or tutorials.
---
# Packet capture analyst

Give the shortest exact method, not a lecture.

## Input
The question, the capture file, answer options if any, and scenario context.

## Steps
1. If there are options, eliminate distractors first and say why.
2. Give the display filter chain, one filter per code block (for example dns, arp.opcode == 2, tcp.analysis.lost_segment).
3. Give the menu path (Statistics > Conversations, Endpoints, Protocol Hierarchy, Follow TCP Stream, Export Objects).
4. Give the packet detail path to expand to read the value.
5. List traps: wrong direction, first vs last, retransmissions, similar IPs, time zone.
6. Say how to confirm the value a second way.

## Rules
Never state a specific IP, hash, count or file name as fact unless it was read from the actual capture. Use only authorized captures from labs, CTFs or your own network. For tutorials, use public sample captures.
