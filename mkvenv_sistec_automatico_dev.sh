#!/bin/bash
set -e
mkdir -p /srv/www/sistec_automatico/venv/
virtualenv -p /usr/bin/python3.9 /srv/www/sistec_automatico/venv/sistec_automatico_dev
source /srv/www/sistec_automatico/venv/sistec_automatico_dev/bin/activate
cd /srv/www/sistec_automatico/
pip install -U -r requirements.dev.txt
exit 0
