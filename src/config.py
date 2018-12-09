__author__ = 'sp'

import os


DEBUG = True
ADMINS = frozenset([
    os.environ.get('PYTHON_EMAIL')
])
