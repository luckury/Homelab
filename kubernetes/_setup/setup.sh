#!/bin/bash

## Setup HAProxy and Keepalived with Ansible
ansible-playbook -i inventory -e 'machine=haproxy_nodes' setup.yaml

## Deploy ArgoCD itself
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

## Enable access to ArgoCD API, if needed!
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'  # via type "LoadBalancer"
## alternatively configure an Ingress resource: https://argo-cd.readthedocs.io/en/stable/operator-manual/ingress/
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo

kubectl apply -f .
