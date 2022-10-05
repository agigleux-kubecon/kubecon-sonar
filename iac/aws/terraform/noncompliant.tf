resource "aws_ebs_volume" "foo_disabled1" { # Noncompliant (S6275): no "encrypted" entry provided
  availability_zone = "us-east-1a"
  size              = 40

  tags = {
    Name = "test-unencrypted1"
  }
}

resource "aws_ebs_volume" "foo_disabled2" {
  availability_zone = "us-east-1a"
  size              = 40
  encrypted         = false # Noncompliant (S6275)

  tags = {
    Name = "test-unencrypted2"
  }
}

resource "aws_ebs_encryption_by_default" "foo_disabled3" {
  enabled = false # Noncompliant (S6275)
}

resource "aws_launch_configuration" "foo_disabled4" {
  image_id      = data.aws_ami.freetier.id
  instance_type = "t2.micro"

	root_block_device { # Noncompliant (S6275): no "encrypted" entry provided
	}

	ebs_block_device { # Noncompliant (S6275): no "encrypted" entry provided
    device_name = "/dev/sdg"
	}
}

resource "aws_launch_configuration" "foo_disabled5" {
  image_id      = data.aws_ami.freetier.id
  instance_type = "t2.micro"

	root_block_device {
		encrypted = false # Noncompliant (S6275)
	}
	ebs_block_device {
    device_name = "/dev/sdg"
		encrypted = false # Noncompliant (S6275)
	}
}