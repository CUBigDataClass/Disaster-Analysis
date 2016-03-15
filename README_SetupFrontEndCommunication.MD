# Real-time disaster analysis using Twitter ( Frontend )

Since the backend is based on BSON ( Binary JSON ) and the language used to communicate with the backend is python ( Apache Spark ), it would be good to have a server based on python / javascript as well. Since python functions can be called easily if the framework is based on python, prefer to use Python Flask. To make it easier, plan is to use AngularJS in future on the frontend (client side) where as use python for the server.

### Objective 1:

Click of a button get the number of Tweets available in the MongoDB database.

### Objective 2:

Click of a button with a parameter, figure out number of times the text appeared in the collected information.

### Objective 3:

Try plotting a graph of the number of times a parameter occured against the dates it occured.


The following can be ignored if Flask was to be used directly!!
<!-- * Installing Apache / httpd ( https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html )

`sudo yum install httpd`

* Turning on the Apache / httpd Server during boot

`chkconfig httpd on`

* Start the Apache/httpd Server

```
/etc/init.d/httpd start
or
sudo service httpd start
``` 


* Allowing communication on incoming port 80 and 443 ( https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html#adding-security-group-rule )

* Installing mod_wsgi ( An apache module which can host any Python WSGI application).

`sudo yum install mod_wsgi` -->

* Installing Flask ( http://flask.pocoo.org/ )

` pip install Flask `

<!-- * Create a directory for Flask Application (http://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/)

Creating a directory and using symbolic link to point to another directory. Do this from Disaster-Analysis Directory too

```
mkdir flaskapp
sudo ln -sT ~/Disaster-Analysis/flaskapp /var/www/html/flaskapp
```

Add apache user to ec2-user group to give privileges same as ec2-user. Also execute access to the home directory. (https://serverfault.com/questions/571229/im-unable-to-symlink-a-directory-into-var-www-html - Try different methods and none of them worked. Took almost 2 hours to get it working :P)

```
sudo usermod -aG ec2-user apache
sudo chmod g+x /home/ec2-user
```

```
Other things tried: 

```
setsebool httpd_enable_homedirs 1

```
Editted the http

```
sudo vi /etc/httpd/conf/httpd.conf
```
<Directory />
    Options FollowSymLinks
    AllowOverride None
    Options Indexes FollowSymLinks Includes ExecCGI
    Allow from all
</Directory>
```


To enable the server to use the same virtual environment

Modify the file

`
sudo vi /home/ec2-user/Disaster-Analysis/flaskapp
`

with the following information

```
import sys
import os
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir("/home/ec2-user/Disaster-Analysis/venv/lib/python2.7/site-packages")
# Add the app's directory to the PYTHONPATH
#sys.path.append("/home/ec2-user/Disaster-Analysis/flaskapp")

# Activate your virtual env
activate_env=os.path.expanduser("/home/ec2-user/Disaster-Analysis/venv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

sys.path.insert(0, '/var/www/html/flaskapp')


from flaskapp import app as application

``` -->

* Installing libraries for Flask
	- Bootstrap
	- Triangle ( To resolve issue between the template of AngularJS and Flask)
	- repoze.lru (Import error observed)
```
pip install flask-bootstrap
pip install flask-triangle
pip install repoze.lru
```

* Installing npm and bower
```
sudo yum install nodejs npm --enablerepo=epel
mkdir /home/ec2-user/Disaster-Analysis/flaskapp/static
cd /home/ec2-user/Disaster-Analysis/flaskapp/static
bower install angularjs --save
```
* Place for storing all the templates
```
mkdir /home/ec2-user/Disaster-Analysis/flaskapp/templates
```

<!-- * To get the error log populated in Apache wsgi: Updated flaskapp.wsgi
```
import sys
import os
import site
import logging

site.addsitedir("/home/ec2-user/Disaster-Analysis/venv/lib/python2.7/site-packages")
activate_env=os.path.expanduser("/home/ec2-user/Disaster-Analysis/venv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/html/flaskapp')
from flaskapp import app as application
from werkzeug.debug import DebuggedApplication
application = DebuggedApplication(application, True)
``` -->

Start MongoDB in background with a logfile

```
mongod --fork --logpath log_mongodb --dbpath data/
```

* MongoDB Commands:

```
Count number of tweets that have no geolocation.
db.Tweets.find({geo: { $ne: null } }).count()

Shows all Indexes
db.Tweets.getIndexes()

Creating an Index
db.Tweets.createIndex({"text":1})

Creating Text Index for Text Query:
db.Tweets.createIndex({"text":"text"})

Text Query:
db.Tweets.find({$text: { $search: "Ivory"} })
```
