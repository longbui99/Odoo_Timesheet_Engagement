#!/bin/bash
source /etc/python3-venv
/opt/odoo/base/odoo/odoo-bin -c /opt/odoo/.config/odoo.conf -u sample -i sample -d longbui --stop-after-init