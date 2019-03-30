# Setup gitlab runner LXC CI nodes
The gitlab runner must be installed on compute node where to execute lxc containers.

## Setup and link the runner to gitlab
See [common setup](./install_runner.md)

## Setup each compute node for LXC CI
This will setup LXC
```sh
host=host.foo.net
bin/ansible-playbook-wrapper -i $host, \
  /srv/corpusops/corpusops.bootstrap/roles/corpusops.roles/services_virt_lxc/role.yml
```

This will setup Docker (opt)
```sh
host=host.foo.net
bin/ansible-playbook-wrapper -i $host, \
  /srv/corpusops/corpusops.bootstrap/roles/corpusops.roles/services_virt_docker/role.yml
```

## Drupal & Python templates
You can contruct templates via ansible playbooks we baked with this project:
```sh
host=localhost
for i in python drupal;do
  TEST_LXC_NAME=gitlabrunner-$i
  bin/ansible-playbook-wrapper -i $host, ansible/playbooks/lxc/create.yml \
    -e "TEST_LXC_HOST=$host TEST_LXC_NAME=$TEST_LXC_NAME"
  bin/ansible-playbook-wrapper -i $host, ansible/playbooks/lxc/provision/node_${i}.yml \
    -e "TEST_LXC_HOST=$host TEST_LXC_NAME=$TEST_LXC_NAME"
done
```
After provision, make sure the template is not running and in ``/var/lib/lxc/$container/config``: ``lxc.start.auto=0``
```sh
for i in gitlabrunner-lxc gitlabrunner-python;do
  lxc-stop -k -n $lxc
  sed -i -re "s/lxc.start.auto =.*/lxc.start.auto = 0/g" -i /var/lib/lxc/$lxc/config
done
```

