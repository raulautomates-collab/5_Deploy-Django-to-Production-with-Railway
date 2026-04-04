#!bin/bash

source /opt/venv/bin/activate
cd /ASSHOLE

python manage.py sendtestemail --admins
python manage.py migrate --no-input
python manage.py auto_admin
python manage.py collectstatic  --no-input
export RUNTIME_PORT=8080

gunicorn DEPLOYMENT.wsgi:applicatio --bind 0.0.0.0:$RUNTIME_PORT



