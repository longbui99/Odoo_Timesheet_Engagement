#!/bin/bash
set -e
source /etc/python3-venv/bin/activate
python3 /opt/odoo/.build/config_generator.py -e /opt/odoo/env/credentials.env