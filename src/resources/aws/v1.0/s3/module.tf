variable "bucket_name" {
  description = "The name of the S3 bucket."
  type        = string
}

module "s3" {
  source = "./.openiac/resources/aws/v1.0/s3/_module/"
  bucket_name = var.bucket_name
}