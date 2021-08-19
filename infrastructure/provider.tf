# Esse está no lugar do main.tf
provider "aws" {
    region = var.aws_region   # Não está usando $ pq não está dentro de uma string
}


# Centralizar o arquivo de controle de estado do terraform
terraform {
  backend "s3" {
    bucket  = "terraform-state-igti-manoell"    
    key     = "state/igti/edc/mod1/terraform.tfstate"     # Caminho do bucket on o arquivo vai ficar
    region  = "us-east-2"                                 # Não dá pra usar variáveis aki.
  }
  
}