# CI Spefication, or how to customizing the build
Most of the procedure can be modified for a project by simply copying and
adapting playbooks inside your project repository.

## Customizing the template
The most important thing to choose when you ll start to put your project under CI
is the ancestor container to spin a new container with.<br/>
This is done via the ``TEST_LXC_TEMPLATE`` environment variable:
A good value could be:
- gitlabrunner-python
- gitlabrunner-drupal

But any preexisting and stopped container present on your CI LXC node can be used as a template.

## Configuring your test suite
In your poject's git, place a ``ansible/playbooks/tests/test.yml`` ansible playbook file which looks like
[this one](./ansible/playbooks/lxc/lifecycle/standalone_test.yml)

## Skipping steps
You can skip each step of the procedure via the relevant **NO_XXX** environment variable:
- ``NO_CLEANUP``: Skip the cleanup step
- ``NO_TEST``: Skip the tests step
- ``NO_CREATE``: Skip the create step
- ``NO_CLEANUP``: Skip the cleanup step
- ``NO_SYNC``: Skip the synchronise code step
- ``NO_BUILD``: Skip the build step

## Changing the top level step executors (the lxc_{build,run,cleanup}.sh scripts)
Top level scripts paths can be overriden by changing their path via their relevant **XXX_SCRIPT** envionment variables:
- ``TEST_LXC_BUILD_SCRIPT``: script to exec at build step, default: [bin/lxc_build.sh](bin/lxc_build.sh)
- ``TEST_LXC_TEST_SCRIPT ``: script to exec at test step, default: [bin/lxc_test.sh](bin/lxc_test.sh)
- ``TEST_LXC_CLEANUP_SCRIPT``: script to exec at cleanup step , default: [bin/lxc_cleanup.sh](./bin/lxc_cleanup.sh)

## Changing the playbooks
- Playbooks can also be found (understand you can override them by placing an edited copy) in
    - ``$PROJECT_REPO/ansible/tests``
    - ``$PROJECT_REPO/.ansible/tests``
    - Example to override the **setup.step**, place a **setup.yml** playbook
      in ``$PROJECT/.ansible/playbooks/tests`` that overrides **lxc/setup.yml**.

Playbooks environment variables (space separated list of playbooks (filename)):
- ``TEST_LXC_CREATE_PLAYBOOKS``: playbooks to run at create step (**create.yml**)
- ``TEST_LXC_SYNC_CODE_PLAYBOOKS ``: playbooks to run at sync. code step (**sync_code**)
- ``TEST_LXC_SETUP_PLAYBOOKS``: playbooks to run at setup  step (**setup.yml**)
- ``TEST_LXC_TEST_PLAYBOOKS``: playbooks to run at test step (**test.yml**)
- ``TEST_LXC_CLEANUP_PLAYBOOKS``:  playbooks to run at cleanup step (**cleanup.yml**)
- If not overriden, each playbook will be seeked in this order:
    -  ``$project/.ansible/playbooks/tests``
    -  ``$project/ansible/playbooks/tests``
    -  ``$thisrepo/<default_location>``

## .gitlab-ci.yml Examples
- See [samples](./samples.md)

