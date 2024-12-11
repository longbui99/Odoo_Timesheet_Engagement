#!/bin/bash
set -e
bash /opt/odoo/.init/entrypoint.sh
source /etc/python3-venv/bin/activate
python3 /opt/odoo/base/odoo/odoo-bin --proxy-mode -c /opt/odoo/.config/odoo.conf --logfile /var/log/odoo/odoo.log