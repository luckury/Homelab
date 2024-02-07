# Ansible/HAProxy-Keepalived #

This role installs and configures HAProxy and Keepalived as a service on your debian based hosts to load balance Kubernetes API and HTTP/S traffic.

## Prerequesits ##

- A Failober IP (VIP)
- Inventory file with a group called  `cpn_nodes` and `worker_nodes`
