# TestMongo
A MongoDB testing playground.

## Installation

### Bitnami MongoDB on AWS

1. Spin up an AWS EC2 instance by choosing the appropriate BitNami MongoDB AMI from this list https://bitnami.com/stack/mongodb/cloud/aws/amis

2. Download the .pem key.

3. git bash (install on computer if not already present) in the folder with the key and type:

```
chmod 400 keyname.pem
```

which gives the user permission to read the file (4) and no permissions (0) to the group and everyone else.

4. Connect to the aws instance using the following command:

```
ssh -i keyname.pem bitnami@aws_instance_public_dns
```

To remove the added ip from the known hosts list, use:

```
ssh-keygen -R server_ip_address
```

We also need the application login username and password. To get this, enter the following command when connected to the server:

```
cat ./bitnami_credentials
```

## Issuing commands

mongo admin is a tool used to manage the mongodb instance. It can be accessed after connecting to the ec2 server and entering:

```
mongo admin --username root --password PASSWORD
```

The user should be root, but either way you should have gotten it together with the application password.
