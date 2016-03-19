#WSGI is basically a protocol defined so that Python application can
#communicate with a web-server and thus be used as web-application outside of CGI.
#reference: http://pymbook.readthedocs.org/en/latest/flask.html
import sys
import os
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir("/home/ec2-user/Disaster-Analysis/venv/lib/python2.7/site-packages")
# Add the app's directory to the PYTHONPATH
#sys.path.append("/home/ec2-user/Disaster-Analysis/flaskapp")

# Activate your virtual env
activate_env=os.path.expanduser("/home/ec2-user/Disaster-Analysis/venv/bin/activate_this.py")
#execfile(activate_env)
execfile(activate_env, dict(__file__=activate_env))

#adds /var/www/html/flaskapp to first indice of path
sys.path.insert(0, '/var/www/html/flaskapp')

from flaskapp import app as application
