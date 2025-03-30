import yaml
import argparse
import os
import shutil
import subprocess

OPENIAC_HOME = os.getenv("OPENIAC_HOME")

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Process an input YAML file.")
parser.add_argument("input_file", type=str, help="Path to the input YAML file")
args = parser.parse_args()

# Load YAML file
with open(args.input_file, "r") as file:
    data = yaml.safe_load(file)

# Copy the resource file into the .openiac folder as a module
openiac_folder = os.path.join(os.getcwd(), ".openiac")
os.makedirs(openiac_folder, exist_ok=True)

# Copy the resource file into the .openiac folder as a module
subprocess.run("cp -R " + OPENIAC_HOME + "/resources .openiac/", shell=True)

for s in data["stacks"]:
    print(s)
    print(f"Stack Name : {s}")
    print("---")

    provider_name = ''
    provider_version = ''

    # List all providers
    provider_name = data["stacks"][s]["provider"]
    print(f"Provider Name: {provider_name}")
    provider_version = data["stacks"][s]["provider_version"]
    print(f"Provider Version: {provider_version}")

    # Print services for each stack
    if "services" in data["stacks"][s]:
        print("Services:")
        for service in data["stacks"][s]["services"]:
            print(f"- {service}")
            resource_file = OPENIAC_HOME + f"/resources/{provider_name}/{provider_version}/{service['type']}/module.tf" 
            destination = service['name'] + "_" + os.path.basename(resource_file)
            shutil.copy(resource_file, destination)
            # print(f"Resource file copied to: {destination}")

    print("---")
    subprocess.run(["tofu", "validate"])
    subprocess.run(["tofu", "plan"])





