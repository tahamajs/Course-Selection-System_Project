from builtins import callable

from django.core.management import execute_from_command_line
from delete_migrations import *
from fix_migrations import *
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

commands = [
    lambda: delete_migrations(yes=True),
    fix_migrations,
    'makemigrations',
    'migrate',
    'initadmin',
]

for cmd in commands:
    if callable(cmd):
        cmd()
    elif type(cmd) is str:
        execute_from_command_line([cmd, ])
