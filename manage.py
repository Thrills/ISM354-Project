#!/usr/bin/env python
import os
import sys

sys.path.append('/home/rga.stb.sun.ac.za/17640776/djangoinstall/lib/python3.3/site-packages/django/contrib/admin/templates')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProjectX.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
