#!/bin/bash

jq -n -f config.template.jsonc | op inject -f -o config.json
kubectl create secret generic cloudflare-ddns-config --from-file=config.json --output='yaml' | kubectl apply -f -
rm config.json