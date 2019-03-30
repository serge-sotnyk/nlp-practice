# Avant de lancer la mig:

En user
```
cd /srv/projects/redmine_preprod/project/redmine
../rvm.sh bundle exec rake redmine:plugins:migrate NAME=dmsf VERSION=0 RAILS_ENV=production
../rvm.sh bundle exec rake redmine:plugins:migrate NAME=redmine_dmsf  VERSION=0 RAILS_ENV=production
../rvm.sh bundle exec rake redmine:plugins:migrate NAME=redmine_lightbox  VERSION=0 RAILS_ENV=production
cd plugins
rm -rf redmine_lightbox scrum2b redmine_dmsf
../rvm.sh bundle exec puma -e production -p 20020
```

