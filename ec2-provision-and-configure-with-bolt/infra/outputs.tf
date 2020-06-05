output "EC2_IP" {
  value = aws_instance.web.public_ip
}