# Cloudflare-DDNS #

In order for the cloudflare-ddns service to work, we need a valid `config.json` that will be wraped inside a kubernetes secret. In this directory we have the following to files:

> ./config.template.jsonc  
> ./generate-secret.sh

1. Edit the `config.template.jsonc` according to your need as per this reference: https://github.com/timothymiller/cloudflare-ddns?tab=readme-ov-file#-example-
2. Assuming the namespace `cloudflare-ddns` already exists, we can now run the script `generate-secret.sh`

## Remarks ##

The comments in the `.jsonc` document are prefaces with a `#` so that jq can handle them correctly when 'rendering' it.