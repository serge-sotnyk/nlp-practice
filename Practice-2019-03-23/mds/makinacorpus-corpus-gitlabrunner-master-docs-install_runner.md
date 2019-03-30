# Common setup for runners
- The idea is to use a special playbook that will install via ansible (so locally or remotely a runner on the
  target host. This will also register the runner against the gitlab instance.

# Prerequisites
- The install path is not mandatory, but if you install somewhere else,
  adapt your commands accordingly and make sure that corpusops.bootstrap:
    - ansible-playbook is inside your $PATH
    - cops_gci_vars role variables are overriden
-  install/update corpusops

    ```sh
    git clone /srv/corpusops/corpusops.bootstrap
    /srv/corpusops/corpusops.bootstrap/bin/install.sh
    ```

- install/update corpusops

    ```sh
    /srv/corpusops/corpusops.bootstrap/bin/install.sh -C -s
    ```

- clone this repo

    ```sh
    git clone https://github.com/makinacorpus/corpus-gitlabrunner.git \
      /srv/ansible/corpus-gitlabrunner
    ```

- Define the variables file describing your infra.
  You can use as you want the regular ways of defining variables inside your ansible
  inventory via command line variables, inline cli variables files, inventory,
  group, or host variables.

## Ansible variables for runners setup
- CF [ansible/playbooks/roles/cops_gci_vars/defaults/main.yml](../ansible/playbooks/roles/cops_gci_vars/defaults/main.yml)
- All those variables (from a role) can be overidden
  by standard ansible configurations, like in inventory or variables files that you will pick in the cli by eg:

    ```sh
	mkdir local
	$EDITOR local/mycirunner.yml
    bin/ansible-playbook-wrapper -e @local/mycirunner.yml ansible/playbooks/cops_install_runner.yml
    ```

## example variables with configuring a runner for Shell executor
```yaml
cops_gci_register_token: "xxx"
cops_gci_url: "https://gitlab.foo.net"
cops_gci_runner_config:
  runners:
    - name: "{{ansible_fqdn}}"
      tag_list:
        - "{{ansible_fqdn}}"
        - "lxc_python"
        - "makina-states"
```

## example variables with configuring a runner for docker executor
```yaml
cops_gci_register_token: "xxx"
cops_gci_url: "https://gitlab.foo.net"
cops_gci_runner_config:
  runners:
    - name: '{{ansible_fqdn}} (docker)'
      executor: docker
      tag_list: ["{{ansible_fqdn}}", "docker"]
      docker_image: "corpusops/ubuntu:16:04"
```

## example pillar with configuring a runner for SSH executor
```yaml
cops_gci_register_token: "xxx"
cops_gci_url: "https://gitlab.foo.net"
cops_gci_runner_config:
  runners:
    "zzz.makina-corpus.net (via {{ansible_fqdn}})":
      executor: "ssh"
      tag_list:
        - "zzz.makina-corpus.net"
        - "lxc_python"
        - "makina-states"
      ssh_user: "root"
      ssh_host: "zzz.makina-corpus.net"
      ssh_identity_file: "/home/gitlab-runner/.ssh/id_rsa"
```

## Install project (will also install corpusops)
You may not configure runners, in this case gitlab runner wont be installed,
only corpusops will.
This can be useful to grab the scripts to setup LXC compute nodes controlled by a distant runner.

