# Bootstrap the cluster with ArgoCD

This are the only manifests you will have to deploy manually. After that ArgoCD will take over.

> Only requirements are: Bash and a valid kubeconfig.

1. Edit the `approject-homelab.yml` && `application-homelab.yml`.
2. Crate a token and edit the `secret-homelab-repo.yml`.
3. Run `chmod +x setup.sh && ./setup.sh`.
4. Done.