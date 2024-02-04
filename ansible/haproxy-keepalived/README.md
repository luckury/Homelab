Source: https://github.com/rezabojnordi/kubernetes_ansible

```yaml
vim inventroy
[preinstall]
172.16.16.88  ansible_user=root
172.16.16.104   ansible_user=root
172.16.16.184  ansible_user=root
172.16.16.111  ansible_user=root
172.16.16.80  ansible_user=root

[master]
172.16.16.88  ansible_user=root
172.16.16.104   ansible_user=root
172.16.16.184  ansible_user=root

[worker]
172.16.16.111  ansible_user=root
172.16.16.80  ansible_user=root

[storage]
172.16.16.86  ansible_user=root


[init_cluster]
172.16.16.88  ansible_user=root

```
