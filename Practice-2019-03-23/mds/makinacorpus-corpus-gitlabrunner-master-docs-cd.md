# CD Deployment
The idea is to add a gitlab runner in any envionment where the deployment needs to be done and have a procedure in place to deliver our code.

## Configuring your deployment procedure
Additonnaly to CI, you can configure CD on your project.
On those environments, we execute [deploy.sh](../bin/deploy.sh)<br/>
which in turn call at least:
 - [sync_code.yml](../ansible/playbooks/lifecycle/sync_code.yml)
 - [env_setup.yml](../ansible/playbooks/lifecycle/env_setup.yml)

Those 3 steps can like all parts of the build process be controlled and changed <br/>
- via environment variabes
    - ``TEST_SYNC_CODE_PLAYBOOKS``: playbooks to run at sync. code step (**sync_code**)
    - ``TEST_ENV_SETUP_PLAYBOOKS``: playbooks to run at deploy time (**env_setup**)
    - ``TEST_DEPLOY_PLAYBOOKS``: additionnal arbitrary playbooks to run at **deploy time** (none by default)
- or directly changing the call from ``deploy.sh`` to another script in the ``.gitlab-ci.yml`` file.


If you do not want to change the procedure but only one, for a phase,
as for CI place an edited copy of the related playbook either in:
- ``.ansible/playbooks``
- ``ansible/playbooks``


## Skipping steps
You can skip each step of the procedure via the relevant **NO_XXX** environment variable:
- ``NO_DEPLOY``: Skip totally deploy script
- ``NO_SYNC``: Skip the synchronise code step
- ``NO_SETUP``: Skip the setup step
- ``NO_DEPLOY_EXTRAS``: Skip the extra deployed playbooks


## Vault files to distribute secret variables to CD environments
Idea is not to use gitlab variables as they are not encrypted and therefore not secured (at least less).

NOTE: This is the way we distribute saltstack pillars for makinastates based deployments

### Install ansible
You will need to have under the hood a working ansible, at least ``2.2``.

### Use corpusops embedded ansible
- Refer to [install_runner.md#install corpusops](docs/install_runner.md# install corpusops)

#### alternate way
A quickier and reliable way to have one is to make a dedicated virtualenv for it.
Don't forget to add his few system requirements (some devel packages and compilers):
- EG: [Debian](https://github.com/corpusops/corpusops.bootstrap/blob/master/requirements/os_packages.Debian)
- EG: [Redhat](https://github.com/corpusops/corpusops.bootstrap/blob/master/requirements/os_packages.redhat)

Then
```sh
virtualenv ~/ansible
. ~/ansible/bin/activate
pip install --upgrade ansible
```

### Create/Edit a vault for an environment
- The vault password can be mentioned via ``TEST_ANSIBLE_VAULT_PASSWORD``.
- A vault can be unencrypted, it's just an ansible variable file, afterall, and the ``default.yml`` is
  a good candidate not to be encrypted.

Environment vaults must be checked either in:
- ``.ansible/vaults/staging.yml``
- ``ansible/vaults/staging.yml``

For makinastates based deployments:
- The pillar awaiten variable name is ``makinastates_pillar``
- The ``makinastates_pillar`` variable content, <br>
  if it is defined as an non empty string, <br/>
  will be rendered inside ``$TEST_PROJECT_PATH/../pillar/init.sls``<br/>
  A vault content could looks like:
  ```yaml
  ---
  makinastates_pillar: |
           ---
           foo: bar
           makina-projects.foo:
              data:
                  bat: 2
  ```

- Create a vault
```sh
ansible-vault create .ansible/vaults/staging.yml
```

- Edit a vault
```sh
ansible-vault edit .ansible/vaults/staging.yml
```

Remember that the editor used by ansible vault is controlled via the ``$EDITOR`` environment variable.

- Dont forget to add, commit and push this vault file
- Remember tthat the ``TEST_ANSIBLE_VAULTS`` environmnent variable controls the vault location candidates search path (``(.)ansible/vaults/${TEST_ENVIRONMENT_NAME}.yml``, ``(.)ansible/vaults/${TEST_COMMIT_REF_NAME}.yml``, ``(.)ansible/vaults/default.yml`` by default)

### Setup the CD node access to the environment related ansible vault file
For the Vault to be decoded, you will need to add the password somewhere on the CD node.

For this you need to:
- Login on the node
- write as the gitlabrunner process owner user inside ``~/.ansiblevaultpassword.${TEST_ENVIRONMENT_NAME OR TEST_COMMIT_REF_NAME}`` the clear password to access to the vault

EG:
```sh
ssh mystaging
sudo su
# or su
echo "SuperSecret" > ~/.ansiblevaultpassword.staging
chmod 600 ~/.ansiblevaultpassword.staging
```

## .gitlab-ci.yml Examples
- See [Samples](./samples.md)


