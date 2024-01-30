# Setup Management Cluster #

The management cluster is comprised of 3 Intel NUCs, which are set up as a Kubernetes cluster with k3s. The host OS of choice is Ubuntu.
Services on Management Cluster ##

01. ArgoCD
02. Longhorn
03. Ranger
04. piHole
05. Authentik
06. Cert-Manager
07. External-DNS
08. External Secrets
09. Prometheus Operator
10. CloudflareDDNS
11. Omada Controller

## Setup Instruction ##

1. Install Ubuntu 22.04.03 LTS (MaaS)
2. Install HAProxy and Keepalived (Ansible)
3. Setup k3s (Ansible)
4. Install ArgoCD (by Hand).
5. Deploy Argo AppProjekt, Application and Secret.
6. Watch the rest of the apps get installed.
