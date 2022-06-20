import os

os.chdir("./terraform_file")
print(os.popen("terraform init").read())
print(os.popen('terraform plan').read())