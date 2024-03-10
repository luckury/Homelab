#!/bin/bash

jq -n -f config.template.jsonc | op inject -f -o /tmp/config.json
kubectl create secret generic -n cloudflare-ddns cloudflare-ddns-config --from-file=/tmp/config.json --output='yaml'
rm /tmp/config.json