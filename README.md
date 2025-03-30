# openiac
Open IaC to allow simple yaml based config to build infra with sensible defaults. 

Open IaC is built on Tofu. 

# Prerequisites
- python3
- aws cli
- tofu

# Usage

create a yaml file with definitions. See example in test yaml

``` python3 iac.py <path to file>/test.yml ```

The script will generate tofu files in the local. It will copy all resources under the .openiac folder from where you execute the script. Then it will run the following automatically.

``` tofu validate ```

``` tofu plan ```
