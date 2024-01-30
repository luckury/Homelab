#!/bin/bash

## Deploy ArgoCD itself
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

## Enable access to ArgoCD API
#kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'  # via type "LoadBalancer"
## alternatively configure an Ingress: https://argo-cd.readthedocs.io/en/stable/operator-manual/ingress/

