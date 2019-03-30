# ENVIRON
Main variables that you can override in your ``.gitlab-ci.yml`` environment section to parameterize the build

All those variables are exported with same name to ansible
Additionnaly, you also have access to the [gitlab exported variables](https://docs.gitlab.com/ce/ci/variables/).

To be clear any variable under the RESTORE_, ARTIFACT_, GET_, CI_, GITLAB_, CUSTOM_, TEST_ prefixes are exported.
If you need to use gitlab variables, name them like ``CUSTOM_XXX``. If this really isnt convenient, redefine the ``TEST_FORWARDED_SHELL_VARS`` environ variable to something more appropriate.

## Common variables
| NAME                         | DESC                              |  DEFAULT or Example        |
| ---------------------------- | --------------------------------- |  -------------------------------            |
| GRUNNER_TOP_DIR              | root path of this repo                         | /srv/projects/gitlabrunner/project |
| TEST_COMMIT                  | commit that will be tested                     |  HEAD                          |
| TEST_COMMIT_REF_NAME         | branch/tag that will be tested                 |                                |
| TEST_SALTCALL_LOGLEVEL       | salt-call loglevel | info                      |                                |
| TEST_USE_MAKINASTATES        | is the project makinastates based              |  true                          |
| TEST_ORIGIN                  | from where to push sources inside the test env | gitlab ci host (localhost)     |
| TEST_ORIGIN_PATH             | sources to push inside the test env            | gitlab ci checkout root        |
| TEST_PROJECT_PATH            | where to push sources inside test env          | /srv/projects/project/project} |
| TEST_FORWARDED_SHELL_VARS    | regex for variables to export through the build procedure | ^(W\|GRUNNER_TOP_DIR\|(CUSTOM\|GITLAB\|ARTIFACT<br/>\|RESTORE\|GET\|TEST\|NO\|CI)_.*)$ |
| TEST_ENVIRONMENT_NAME| environment name where we are deploying, determine the vault filename to grab | $CI_ENVIRONMENT_NAME or default if undefined |

## CI Specific
| NAME                         | DESC                              |  DEFAULT or Example        |
| ---------------------------- | --------------------------------- |  -------------------------------            |
| NO_BUILD                     | Skip the build step            | not defined |
| NO_CREATE                    | Skip the create step           | not defined |
| NO_SYNC                      | Skip the synchronise code step | not defined |
| NO_SETUP                     | Skip the setup code step | not defined |
| NO_TEST                      | Skip the tests step            | not defined |
| NO_CLEANUP                   | Skip the cleanup step          | not defined |
| TEST_LXC_TEMPLATE            | container to take as ancestor     |  gitlabrunner-common                        |
| TEST_LXC_NAME                | name of the container to create   |  gci-$(get_random_slug 8)                   |
| TEST_LXC_BUILD_SCRIPT        | script to exec at build step      |  [bin/lxc_build.sh](bin/lxc_build.sh)       |
| TEST_LXC_TEST_SCRIPT         | script to exec at test step       |  [bin/lxc_test.sh](bin/lxc_test.sh)         |
| TEST_LXC_CLEANUP_SCRIPT      | script to exec at cleanup step    |  [bin/lxc_cleanup.sh](./bin/lxc_cleanup.sh) |
| TEST_LXC_HOST                | host to create containers on      |  10.5.0.1                                   |
| TEST_LXC_PATH                | path of the containers root       |  /var/lib/lxc                               |
| TEST_LXC_BACKING_STORE       | backing store for container       |  overlayfs                                  |
| TEST_LXC_TEST_PLAYBOOKS      | space separated abspaths to playbooks to run at test step       | [test.yml](../ansible/playbooks/lxc/lifecycle/test.yml) -> [sub](../ansible/playbooks/lifecycle/test.yml)        |
| TEST_LXC_CLEANUP_PLAYBOOKS   | space separated abspaths to playbooks to run at cleanup step    | [cleanup.yml](../ansible/playbooks/lxc/cleanup.yml)     |
| TEST_LXC_CREATE_PLAYBOOKS    | space separated abspaths to playbooks to run at create step     | [create.yml](../ansible/playbooks/lxc/create.yml) |
| TEST_LXC_SYNC_CODE_PLAYBOOKS | space separated abspaths to playbooks to run at sync. code step | [sync_code.yml](../ansible/playbooks/lxc/lifecycle/sync_code.yml) -> [sub](../ansible/playbooks/lifecycle/sync_code.yml) |
| TEST_LXC_SETUP_PLAYBOOKS     | space separated abspaths to playbooks to run at setup  step     | [setup.yml](../ansible/playbooks/lxc/lifecycle/setup.yml) -> [sub](../ansible/playbooks/lifecycle/setup.yml)       |

## CD Specific
| NAME                         | DESC                              |  DEFAULT or Example        |
| ---------------------------- | --------------------------------- |  -------------------------------            |
| NO_DEPLOY                | Skip entirely deploy steps | not defined |
| NO_SYNC                  | Skip the sync code step | not defined |
| NO_SETUP                 | Skip the setup code step | not defined |
| NO_DEPLOY_EXTRAS         | Skip the extra playbooks run step | not defined |
| TEST_SYNC_CODE_PLAYBOOKS | space separated abspaths to playbooks to run at sync. code step in deployed env| [sync_code.yml](../ansible/playbooks/lifecycle/sync_code.yml) |
| TEST_ENV_SETUP_PLAYBOOKS | space separated abspaths to playbooks to run at setup  step     | [env_setup.yml](../ansible/playbooks/lifecycle/env_setup.yml)       |
| TEST_ANSIBLE_VAULTS | vault location candidates | (.)ansible/vaults/${TEST_ENVIRONMENT_NAME}.yml, (.)ansible/vaults/${TEST_COMMIT_REF_NAME}.yml, (.)ansible/vaults/default.yml  |
| TEST_ANSIBLE_VAULT_PASSWORD | vault password if any | |

