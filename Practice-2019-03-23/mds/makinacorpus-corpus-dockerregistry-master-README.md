# Makina-States bases docker registry
This provides a docker distribution (registry v2) docker image based on makina-states.<br/>
This registry embeds a daemon that implements registry V2 tokens, (cesanta/docker_auth).<br/>
The registry won't allow any anonymous configuration.

You will certainly need to read the official documentation around the docker registry.<br/>
Pay attention that you need to access your registry with a DNS name and a valid SSL certificate.<br/>
This certicate must be signed by an authority (even if you generates this authority).<br/>
Other setup will make you go in troubles.<br/>
You can of course follow the SSL certificate generation snippet bellow.

## Code organization
This registry is based via makina-states, a deployment framework based on saltstack.<br/>
***Please read this*** [documentation](http://makina-states.readthedocs.org/usage_docker/images.html#initialise-your-dev-environment) ***FIRST***

We separate the project codebase from any persistent data that is needed to be created along any container.<br/>
For this we use two root separates folders:
 - one for the clone of the codebase: ***${PROJECT}***
 - and one for the persistent data: ***${DATA}***

Specific to this image:

    ${DATA}/ca
        any ssl generated certificates
    ${DATA}/go
        if binary are built: build results
    ${DATA}/docker-auth
        if binary are built: cesenta/docker-auth codebase
    ${DATA}/registry
        if binary are built: registry codebase
    ${VOLUME}/data/images
        where the images are stored (autocreated)
    ${VOLUME}/data/www_dir
        reverse proxy docroot       (autocreated)
    ${VOLUME}/data/images
        where the images are stored (autocreated)
    ${VOLUME}/data/www_dir
        reverse proxy docroot       (autocreated)

## Download and initialise the layout
```bash
export REPO_URL="https://github.com/makinacorpus/corpus-dockerregistry.git"
export PROJECT="${WORKSPACE}/myproject" # where you want to put the code
export DATA="${PROJECT}_data"           # where you want to put the data
export VOLUME="${DATA}/volume"          # where you want to put the docker volume
mkdir -p "${DATA}" "${VOLUME}"
git clone "${REPO_URL}" "${PROJECT}"
```
- [base doc](http://makina-states.readthedocs.org/usage_docker/images.html#download-and-initialize-the-layout) from makina-states

### OPTIONAL: Generate a SSL certificate for test purposes
- **YOU NEED A CERTIFICATE TO RUN THIS IMAGE**
- [base doc](http://makina-states.readthedocs.org/usage_docker/images.html#optionnal-generate-a-a-certificate-with-a-custom-authority-for-testing-purposes) from makina-states

## Configure the image via the salt PILLAR
You need then to fill the pillar to:
  - setup a domain to serve for the registry (the virtualhost name)
  - the SSL certificate informations
  - The users ACLS for the registry, see [official doc from cesenta](https://github.com/cesanta/docker_auth/blob/master/examples/reference.yml)

```bash
mkdir -p "${VOLUME}/configuration"
cp .salt/PILLAR.sample "${VOLUME}/configuration/pillar.sls"
sed -re "s/makina-projects.projectname/makina-projects.registry/g"\
  -i "${VOLUME}/configuration/pillar.sls"
$EDITOR "${VOLUME}/configuration/pillar.sls" # Adapt to your needs
```

Edit at least:
  - domain
  - certificate key and bundle (content)
      (maybe by concatening the content of
       project_data/ca/ca/${domain}.bundle.crt
       & ca/${domain}.${domain}-key.pem
  - list of http users and password to allow and their acls
  - You can remove what is not overriden if you want.

Example configuration/pillar.sls
```yaml
makina-projects.registry:
  data:
    users:
      admin:
        password: test1
      readonly:
        password: test2
    acl:
      # Admin has full access to everything.
      - {match: {account: "admin"}, actions: ["*"]}
      # User "readonly" can pull stuff.
      - {match: {account: "readonly"}, actions: ["pull"]}
      # Access is denied by default.
    # the domain serving your registry
    domain: "registryh.docker.tld"
    # the SSL certicate(incuding the intermediaries)
    ssl_cert: |
        -----BEGIN CERTIFICATE-----
        MIIDMjCCAhoCCQDvVm1SttCzxTANBgkqhkiG9w0BAQsFADBZMQswCQYDVQQGEwJG
        ...
        ugItmnXoVCkHHrZvydXC/zxah21lfVtA05xB8zsieLyLmsy8lH2exftnpM3QgMAp
        G9S8ZWex
        -----END CERTIFICATE-----
        -----BEGIN CERTIFICATE-----
        MIIDhTCCAm2gAwIBAgIJAKWNQ8MgC28RMA0GCSqGSIb3DQEBCwUAMFkxCzAJBgNV
        ...
        S17wzmffRktued3rJ+efBUvegdnbJG1nxT51znLy5mlLAD37OCf2DgqlGyL1UcEr
        XhidyUpZcJ4Fr2koosQZ8z20j2tXDanhbSi1osJ6yQi8rjRdJZeCMwA=
        -----END CERTIFICATE-----
    # the relevant SSL key
    ssl_key: |
      -----BEGIN RSA PRIVATE KEY-----
      MIIEpQIBAAKCAQEAzzBVPJvbMXFBN1mErd+T3QDUpvI6YvJt3JJjBptvcke1X9Si
      ...
      fFwSDE8arfpgbAfrtYgWjd0248GRV46iE1BuE4uuZ41XQ9J9DILzjMk=
      -----END RSA PRIVATE KEY-----
```

## Allow users to connect to the registry via ssh

## Build & Run

- [Base documentation](http://makina-states.readthedocs.org/usage_docker/images.html#build-run)

***Be sure to have completed the initial configuration (SSL, PILLAR) before launching the container.***
You may not need to **build** the image, you can directly download it from the docker-hub.
```bash
docker pull makinacorpus/registry
# or docker build -t makinacorpus/registry .
```
Run
```bash
docker run -ti -v "${VOlUME}":/srv/projects/registry/data makinacorpus/registry
```

The image exposes some volumes that you may want to attach In production mode:
 - /srv/projects/registry/data
 - /var/logs/circus
 - /var/logs/bind

## Hack this image
See:
- [doc/Hack.md](doc/Hack.md)
- [doc/Registry.md](doc/Registry.md)




