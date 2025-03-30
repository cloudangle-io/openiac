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

# YAML

The config yaml is abstracted to a high level making it much easier to developers to build infra with sensible defaults. We will keep allowing more and more flexibility without removing the sensible default layer to avoid unnecessary optimisations. For most applications the defaults should work without any changes eventually.

```
version: 0.1

stacks:
  myapp:
    provider: aws
    provider_version: v1.0
    region: ap-southeast-2
    environment:
      - dev
      - test
      - prod
    services:
      - name: test
        type: s3
        properties:
          bucket: test
          region: us-east-1
```
