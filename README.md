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
- install pip if not exists
- pip install virtualenv
- install httpd if not exists
    - yum install httpd
    - systemctl start httpd
    - systemctl enable httpd
    - rm -f /etc/httpd/conf.d/welcome.conf