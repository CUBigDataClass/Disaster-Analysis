`sudo yum update`
`sudo yum install git`

- https://docs.mongodb.org/manual/tutorial/install-mongodb-on-amazon/

`sudo vi /etc/yum.repos.d/mongodb-org-3.2.repo`

- Updating Yum with the MongodB Repository

```
[mongodb-org-3.2]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/amazon/2013.03/mongodb-org/3.2/x86_64/
gpgcheck=0
enabled=1
```
- Installing MongoDB

`sudo yum install -y mongodb-org`

- Follow README.MD

- To Download apache spark:

`wget http://d3kbcqa49mib13.cloudfront.net/spark-1.6.0-bin-hadoop2.6.tgz`

- Unzip downloaded contents:

`tar -xvf spark-1.6.0-bin-hadoop2.6.tgz`

- Incase build failed due to java, install java development package:

`sudo yum install java-devel`
