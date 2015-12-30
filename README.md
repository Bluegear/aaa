## Prerequisite on Dev
1. python 2.7
1. pip

## How to start server after check out
1. Clone source code from https://github.com/Bluegear/as
1. Run following commands 
1. `pip install virtualenv`
1. `virtualenv -p /usr/bin/python2.7 venv`
1. `source venv/bin/activate`
1. `pip install -r requirements.txt`
1. `python manage.py migrate`
1. Run `python manage.py createsuperuser` and supply these values.
    -- username: admin
    -- email: admin@as.com
    -- password: pass99word


## Issues with dependencies installation
1. Error occur while installing mod_wsgi on mac OSX, For detail see https://github.com/GrahamDumpleton/mod_wsgi/issues/50#issuecomment-115378767
    - Run command `xcode-select --install`
    - Run `pip install -r requirements.txt` again.

## After pull request developer should runs these commands.
1. pip install -r requirements.txt
1. python manage.py migrate

## Prerequisite on Alpha/Staging
1. install pip if not exists
1. `pip install virtualenv`
1. `virtualenv -p /usr/bin/python2.7 venv`
1. install httpd if not exists
    - `yum install httpd`
    - `systemctl start httpd`
    - `systemctl enable httpd`
    - `rm -f /etc/httpd/conf.d/welcome.conf`
1. `yum install httpd-devel`
1. `yum install gcc`
1. `yum install python-devel`

## Pre deploy scripts
1. Enter project directory
1. source venv/bin/activate
1. `pip install -r requirements.txt`
1. `python manage.py migrate`
1. Create directory 'static' if not exists.
1. `python manage.py collectstatic`
1. For first deploy run `python manage.py createsuper` then supply admin username, email and password

## Run Service on Alpha/Staging
1. `python manage.py runmodwsgi --user apache group apache --port 80 &`
