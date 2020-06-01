terraform {
  backend "s3" {}
}

provider "aws" {
  region = local.workspace["aws_region"]
  shared_credentials_file = "/workspace/credentials"
}

resource "aws_security_group" "web_sg" {
  name        = "Web SG"
  description = "Managed by Terraform"
  vpc_id      = local.workspace["vpc_id"]

  tags = {
    Name = "HelloWorldNebula"
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web" {
  ami                    = var.ec2_ami
  instance_type          = var.ec2_machine_type
  vpc_security_group_ids = [aws_security_group.web_sg.id]
  key_name               = local.workspace["key_name"]

  tags = {
    Name = "HelloWorldNebula"
  }

  root_block_device {
    volume_type = "gp2"
    volume_size = var.ec2_disk_size
  }

  depends_on = [aws_security_group.web_sg]
}