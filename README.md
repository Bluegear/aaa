# Development Note

## Prerequisite on your local environment
1. python 3.4
1. pip

## How to start server after check out
1. Clone source code from https://github.com/Bluegear/as
1. Run following commands 
1. `pip3 install virtualenv`
1. `virtualenv -p python3.4 venv` (On windows using : `virtualenv —python=3.4 venv`)
1. `source venv/bin/activate` (On windows using : `venv/Script/activate.bat`)
1. For Mac OSX run `xcode-select --install` to avoid installation error with mod_wsgi.
1. For Mac OSX run `CFLAGS=-I/usr/include/apr-1 pip install mod_wsgi` to compile/install mod_wsgi first.
1. For Windows Please refer to https://github.com/GrahamDumpleton/mod_wsgi/blob/master/win32/README.rst
1. `pip install -r requirements.txt`
1. `python manage.py migrate`
1. Run `python manage.py createsuperuser` and supply these values.
    -- username: admin
    -- email: admin@as.com
    -- password: pass99word

## After pull request developer should runs these commands.
1. `source venv/bin/activate`
1. `pip install -r requirements.txt`
1. `python manage.py migrate`

## Adding dependencies
1. `source venv/bin/activate`
1. `pip install <python package>`
1. `pip freeze > requirements.txt`

## Adding Model that represent database table
1. Make change to your models.
1. run `python manage.py makemigrations`
1. run `python manage.py migrate`
1. Commit and push your changes.

# CI/CD Note

## Prerequisite on Alpha/Staging
1. install pip if not exists
1. `pip3 install virtualenv`
1. `virtualenv -p python3.4 venv`
1. install http\d if not exists
    - `yum install httpd`
    - `systemctl start httpd`
    - `systemctl enable httpd`
    - `rm -f /etc/httpd/conf.d/welcome.conf`
1. `yum install httpd-devel`
1. `yum install gcc`
1. `yum install python-devel`

## Pre deploy scripts
1. Enter project directory
1. `source venv/bin/activate`
1. `pip install -r requirements.txt`
1. `python manage.py migrate`
1. Create directory 'static' if not exists.
1. `python manage.py collectstatic`
1. For first deploy run these commands.
    - Make sure that project directory belong to user and group 'apache'
    - `python manage.py createsuper` then supply admin username, email and password
    - `chown apache db.sqlite3`
    - `chgrp apache db.sqlite3`
    - `chmod 774 db.sqlite3`

## Run Service on Alpha/Staging
1. `python manage.py runmodwsgi --user apache group apache --port 80 &`
