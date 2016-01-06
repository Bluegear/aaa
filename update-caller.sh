#!/bin/bash

echo '- Remove old code'
rm -rf /var/www/django/triple-a

echo '- Unzip new core to target'
unzip /tmp/triple-a/triple-a.zip -d /var/www/django/triple-a

echo '- Activate virtualenv'
source /var/www/django/triple-a/venv/bin/activate
pip freeze
pip install -r /var/www/django/triple-a/requirements.txt

echo '- Change owner to apache'
chown -Rf apache:apache /var/www/django/triple-a/venv

echo '- Change owner to apache'
chown -Rf apache:apache /var/www/django/triple-a

echo '- Restart HTTPD'
`python manage.py runmodwsgi --user apache group apache --port 80 &`