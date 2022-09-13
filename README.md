ansible-role-node-exporter
=========

Install and enable the prometheus node-exporter daemon via Ansible.

The node-exporter will be downloaded from [github.com](https://github.com/prometheus/node_exporter/releases)
and installed.

Example Playbook
----------------

```{yml}
- hosts: all
  roles:
     - role: node-exporter
```
