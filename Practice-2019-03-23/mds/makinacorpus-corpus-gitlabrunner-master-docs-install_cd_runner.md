# Setup a CD runner
The CD runners only requirement is to provide a shell/ssh executor based gitlabrunner.

## Setup a vault for the environment on your project
You will need to add a vault environment file inside the project code source repo.<br/>
See the appropriate section in [CD](./cd.md)

## Setup the vault passphrase
You will need to write the vault passphase<br/>
See the appropriate section in [CD](./cd.md)

## Setup and link the runner to gitlab
See [common setup](./install_runner.md)

## example pillar with configuring a runner for Shell executor
```yaml
cops_gci_register_token: "xxx"
cops_gci_url: "https://gitlab.foo.net"
cops_gci_runner_config:
  runners:
    - name: "zzz.foo.net"
      executor: "shell"
      tag_list: ["{{ansible_fqdn}}"]

```

## example pillar with configuring a runner for SSH executor
```yaml
cops_gci_register_token: "xxx"
cops_gci_url: "https://gitlab.foo.net"
cops_gci_runner_config:
  runners:
    - name: "{{ansible_fqdn}} (CI)"
      executor: "ssh"
      tag_list: ["{{ansible_fqdn}}"]
      ssh_user: "root"
      ssh_host: "zzz.makina-corpus.net"
      ssh_identity_file: "/home/users/gitlabrunner-user/.ssh/id_rsa"
```


