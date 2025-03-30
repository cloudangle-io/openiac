import yaml
import argparse
import os
import shutil
import subprocess

OPENIAC_HOME = os.getenv("OPENIAC_HOME")

parser = argparse.ArgumentParser(description="Process an input YAML file.")
parser.add_argument("input_file", type=str, help="Path to the input YAML file")
args = parser.parse_args()

with open(args.input_file, "r") as file:
    data = yaml.safe_load(file)

openiac_folder = os.path.join(os.getcwd(), ".openiac")
os.makedirs(openiac_folder, exist_ok=True)

subprocess.run("cp -R " + OPENIAC_HOME + "/resources .openiac/", shell=True)

for s in data["stacks"]:
    print(f"Stack Name : {s}")

    provider_name = ''
    provider_version = ''

    provider_name = data["stacks"][s]["provider"]
    print(f"Provider Name: {provider_name}")
    provider_version = data["stacks"][s]["provider_version"]
    print(f"Provider Version: {provider_version}")

    for environment in data["stacks"][s]["environment"]:
        print(f"Environment : {environment}")
        print(f"Environment : {data['stacks'][s]['environment'][environment]}")

        
        if "services" in data["stacks"][s]:
            print("Services:")
            for service in data["stacks"][s]["services"]:
                resource_file = OPENIAC_HOME + f"/resources/{provider_name}/{provider_version}/{service['type']}/module.tf" 
                destination = service['name'] + "_" + os.path.basename(resource_file)
                shutil.copy(resource_file, destination)

        subprocess.run(["export AWS_PROFILE=" + data["stacks"][s]["environment"][environment]["profile"]], shell=True)
        subprocess.run(["tofu", "validate"])
        subprocess.run(["tofu", "plan"])





