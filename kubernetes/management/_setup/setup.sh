#!/bin/bash

## Deploy ArgoCD itself
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

## Enable access to ArgoCD API, if needed!
#kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'  # via type "LoadBalancer"
## alternatively configure an Ingress resource: https://argo-cd.readthedocs.io/en/stable/operator-manual/ingress/

kubectl apply -f .
