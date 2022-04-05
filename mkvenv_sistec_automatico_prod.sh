#!/bin/bash
set -e
mkdir -p /srv/www/sistec_automatico/venv/
virtualenv -p /usr/bin/python3.9 /srv/www/sistec_automatico/venv/sistec_automatico_prod
source /srv/www/sistec_automatico/venv/sistec_automatico_prod/bin/activate
cd /srv/www/sistec_automatico/
pip install -U -r requirements.prod.txt
exit 0
