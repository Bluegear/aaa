#!/usr/bin/env python

import os
import time
import subprocess

#
# For people who have question why i comment this, I found problem about environment.
#
# EXTRACTED='/tmp/bank-cash-in-report'
# ENV='/var/www/html/env'
# PUBLIC='/var/www/html/bank_cash_in_report'

# def extract_code():
#     return subprocess.call('unzip %s/bank-cash-in-report.zip -d %s' % (EXTRACTED, PUBLIC), shell=True)

# def belong_to_apache(target):
#     return subprocess.call('chown -Rf apache:apache %s' % target, shell=True)

# def update_virtualenv():
#     return subprocess.call('source %s/bin/activate && pip install -r %s/requirements.txt' % (ENV, PUBLIC), shell=True)

# def deploy_project_config():
#     return subprocess.call('cp %s/bank_cash_in_report.conf /etc/httpd/conf.d' % (PUBLIC), shell=True)

# def collecting_static_files():
#     subprocess.call('cd %s' % (PUBLIC), shell=True)
#     return subprocess.call('source %s/bin/activate && %s/bin/python2.7  %s/manage.py collectstatic --noinput' % (ENV, ENV, PUBLIC), shell=True)

# def synchronize_db():
#     subprocess.call('cd %s' % (PUBLIC), shell=True)
#     return subprocess.call('source %s/bin/activate && %s/bin/python2.7  %s/manage.py syncdb --noinput' % (ENV, ENV, PUBLIC), shell=True)

# def remove_previous():
#     return subprocess.call('rm -rf %s' % (PUBLIC), shell=True)

# if __name__=='__main__':

#     print remove_previous()

#     print extract_code()
#     print belong_to_apache(PUBLIC)

#     print update_virtualenv()
#     print collecting_static_files()
#     print synchronize_db()
#     print belong_to_apache(ENV)

#     print deploy_project_config()

print subprocess.call('/bin/bash /tmp/triple-a/update-caller.sh', shell=True)