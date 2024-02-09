# Setup Management Cluster #

The management cluster is comprised of 3 Intel NUCs, which are set up as a Kubernetes cluster with k3s. The host OS of choice is Ubuntu.
Services on Management Cluster ##

01. ✅ ArgoCD ⚠️(Make self-managed)
02. ✅ Longhorn 
03. ✅ Cert-Manager 
04. ✅ CloudflareDDNS 
05. ⚠️ Rancher (not compatible with Kubernetes 1.28.0)
06. ✅ piHole
07. Authentik
08. External-DNS
09. External-Secrets
10. Prometheus Operator
11. Omada Controller
12. RBAC-Manager
13. Cilium

## Setup Instruction ##

1. Install Ubuntu 22.04.03 LTS (MaaS)
2. Install HAProxy and Keepalived (Ansible)
3. Setup k3s (Ansible)
4. Install ArgoCD (by Hand).
5. Deploy Argo AppProjekt, Application and Secret.
6. Watch the rest of the apps get installed.
