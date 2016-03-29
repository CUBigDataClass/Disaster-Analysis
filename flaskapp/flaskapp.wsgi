import sys
import os
import site
import logging

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir("/home/ec2-user/Disaster-Analysis/venv/lib/python2.7/site-packages")
# Add the app's directory to the PYTHONPATH
#sys.path.append("/home/ec2-user/Disaster-Analysis/flaskapp")

# Activate your virtual env
activate_env=os.path.expanduser("/home/ec2-user/Disaster-Analysis/venv/bin/activate_this.py")
#execfile(activate_env)
execfile(activate_env, dict(__file__=activate_env))

logging.basicConfig(stream=sys.stderr)

sys.path.insert(0, '/var/www/html/flaskapp')


from flaskapp import app as application
from werkzeug.debug import DebuggedApplication
application = DebuggedApplication(application, True)
