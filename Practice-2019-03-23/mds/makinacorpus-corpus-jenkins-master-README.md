Install Procedure
-------------------

- Create the jenkins master with:
    - https://github.com/makinacorpus/corpus-jenkins

- Install plugins:
    - ssh slave
    - git plugin
    - ssh agent plugin
    - Parameterized Trigger Plugin
    - Build Pipeline Plugin
    - Delivery Pipeline Plugin
    - Build With Parameters
    - Role Strategy Plugin
    - Job Restrictions Plugin
    - Rebuild
    - EnvInject
    - Cobertura Plugin
    - xunit

- For now, Update Git Parameter plugin from: https://github.com/makinacorpus/corpus-jenkins/releases/tag/plugins
  to enable ssh agent forwarding upon git parameter enablement

- Configure security
    - local bdd
    - create admin user
    - goto manage role
        - admin: all
        - readonly: read + read
    - goto assign role
        - assign admin to admin user
        - assign readonly to any other users
        - in projects, assign role to project user
    - goto security
        - activate
        - disable self register
        - role based strategy

- Create a slave:
    - https://github.com/makinacorpus/corpus-slave
    - In the pillar configure the master /root/.ssh/id_rsa.pub in the ssh_keys

- Create a credentials on jenkins
    - user: jenkins
    - sshkey: master sshkey

- Add this credential to the agent plugin

- Create a slave on jenkins:
    - hostname
    - credential above
    - launch slave via ssh:
        - workspace: /srv/projects/jenkinsslave/data/builds

