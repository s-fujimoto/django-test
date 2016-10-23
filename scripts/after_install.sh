#!/bin/sh

pip install -r /tmp/requirements.txt
python /var/lib/project/manage.py migrate
