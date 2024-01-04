#!/bin/bash

jq -n -f config.template.jsonc | op inject -f -o config.json
podman-compose up -d
