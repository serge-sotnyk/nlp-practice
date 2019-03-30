# SPEC
## The big picture
In CI mode (test our code)
```
    GITLAB <- HTTP -> gitlab runners nodes with LXC preconfigured -> container1
                               |                                         |
                               |- -- Ansible/SSH via compute node  ------|
```

In CD mode (deploy our code to an environment)
```
    GITLAB <- HTTP -> gitlab runner node accessible via ssh
                                 |
                                 \_ANSIBLE BASED DEPLOY
```

Where ever we have SSH or a local shell account, we can easily use ansible to execute remote tasks.
- Idea is:
    - to execute tests on volatile containers spinned on remote lxc-capable compute nodes via the gitlabrunner node.
    - deploy on any SSH targetable node where a gitlabrunner is installed via this project (so with makinastates & corpusops)

- Any part of the build process can easyly be changed and tweaked by a combination of:
    - Changing environment variables
        - Those env vars can even changed the scripts & playbooks executed during process.
    - Copying and editing playbooks in a well known place on the project source code repository should be sufficient
      to adapt small but well identified parts of the build process

## Test infra description (CI)
For more details, see [CI setup](./install_ci_runner.md) & [usage](./ci.md)

- We install a gitlabrunner somewhere
- This runner can connect as root via ssh to hosts than can spin lxc containers
  - To preconfigure lxc hosting, we use: [virt_lxc](https://github.com/corpusops/roles/tree/master/services_virt_lxc)
- As soon as we spin a lxc container we can control it via SSH
  - We use here [lxc_create](https://github.com/corpusops/lxc_create)
  - & [lxc_sshauth](https://github.com/corpusops/lxc_sshauth)
- In many playbooks, we will call [lxc_register](https://github.com/corpusops/roles/tree/master/lxc_register) to
  dynamically load the LXC container inside the current ansible inventory.
- We can then spin lxc containers and run our test suite on. All this work is done and configurable
  via well placed ansible playbooks and shell scripts that call them
  - Read (recursivly [this run script](./bin/lxc_run.sh).
    This will executes some phases.
    - 1. [lxc_build.sh](./bin/lxc_build.sh): create a container and prepare it for tests. <br/>
         It is in charge to call in order those playbooks:
        - [lxc/create.yml](./ansible/playbooks/lxc/create.yml): create a container from a template
        - [lxc/sync_code.yml](./ansible/playbooks/lxc/lifecycle/sync_code.yml): synchronise code inside the environment
           - itself calls: [lifecycle/sync_code.yml](./ansible/playbooks/lifecycle/sync_code.yml)
        - [lxc/setup.yml](./ansible/playbooks/lxc/lifecycle/setup.yml): run project setup procedure
           - itself calls: [lifecycle/setup.yml](./ansible/playbooks/lifecycle/setup.yml)
    - 2. [lxc_test.sh](./bin/lxc_test.sh): Call project tests.<br/>
        It is in charge to call in order those playbooks:
        - [lxc/test.yml](./ansible/playbooks/lxc/lifecycle/test.yml): run project tests
           - itself calls: [lifecycle/test.yml](./ansible/playbooks/lifecycle/test.yml)
    - 3. [lxc_cleanup.sh](./bin/lxc_cleanup.sh): cleanup test resources <br/>
         It is in charge to call in order those playbooks
        - [lxc/cleanup.yml](./ansible/playbooks/lxc/cleanup.yml): remove whatever we did on the baremetal.
          Barely, and for now, this resumes at dropping the test container.

### Services activated on templates:
- memcached
- mysql:
  - root password: secret
  - db0 -> db9, user & password are the same as the database.
- elasticsearch:
  - http://127.0.0.1:9200
  - no restriction
- redis
- pgsql
  - local user postgres is superuser
  - db0 -> db9, user & password are the same as the database
- mongodb (**TODO**)
  - db0 -> db9, user & password are the same as the database
- selenium, firefox, xvfb

## Deploy infra description (CD)
For more details, see [CD setup](./install_cd_runner.md) & [usage](./cd.md)

The steps ran via the gitlabrunner (ssh) on CD nodes are as follows:
- [deploy.sh](./bin/deploy.sh): launch & control the build process
     It is in charge to call by default in order those playbooks:
    - [sync_code.yml](./ansible/playbooks/lifecycle/sync_code.yml): synchronise code inside the environment
    - [env_setup.yml](./ansible/playbooks/lifecycle/env_setup.yml): run project setup procedure

- Secrets are distributed via an ansible vault file checked in
  the source code and loaded via the ``TEST_DEPLOY_ENVIRONMENT`` environment variable.
  For more details, see [CD setup](./cd.md)
Eg:

- commity
- and in your related job in gitlab.yml


