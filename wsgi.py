#
# Conteudo do arquivo `wsgi.py`
#
import sys

sys.path.insert(0, "/var/www/flask1/flask-example")

from server import app as application
