import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--access_key', type=str, required=True)
parser.add_argument('--secret_key', type=str, required=True)
parser.add_argument('--aws_region', type=str, required=True)
args = parser.parse_args()

os.chdir("./terraform_file")
print(os.popen("terraform init").read())

apply = f"terraform apply -var 'access_key={args.access_key}' -var 'secret_key={args.secret_key}' -var 'aws_region={args.aws_region}' --auto-approve"
# destroy = f"terraform destroy -var 'access_key={args.access_key}' -var 'secret_key={args.secret_key}' -var 'aws_region={args.aws_region}' --auto-approve"


print(os.popen(apply).read())
# print(os.popen(destroy).read())
