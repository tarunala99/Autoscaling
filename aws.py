#!/usr/bin/env python
import os
from boto.ec2.connection import EC2Connection
import time
import requests

IMAGE='ami-08710c1f'
KEY_NAME='15319demo' 
INSTANCE_TYPE='m3.medium'
ZONE='us-east-1a'
SECURITY_GROUPS=['SSH_HTTP_MYSQL']

secret1=os.environ['AWS_SECRET_ACCESS_KEY']
access1=os.environ['AWS_ACCESS_KEY_ID']
# Create the EC2 instance 
print 'Starting the EC2 instance of type {0} with image {1}'.format(INSTANCE_TYPE, IMAGE)
conn= EC2Connection(access1,secret1)
SECURITY_GROUPS=conn.get_all_security_groups()
reservation=conn.run_instances(IMAGE,instance_type=INSTANCE_TYPE,key_name=KEY_NAME,placement=ZONE,security_groups=[SECURITY_GROUPS[-1]])
instance=reservation.instances[0]
time.sleep(10)

while not instance.update()=='running':
	time.sleep(3)
time.sleep(10)

print 'Started the load generator: '+str(instance.id)

instance.add_tag('Project','2.1')

load=instance.public_dns_name

IMAGE='ami-1eee9c09'
KEY_NAME='15319demo' 
INSTANCE_TYPE='m3.medium'
ZONE='us-east-1a'


# Create the EC2 instance 
print 'Starting the EC2 instance of type {0} with image {1}'.format(INSTANCE_TYPE, IMAGE)
conn= EC2Connection(access1,secret1)
SECURITY_GROUPS=conn.get_all_security_groups()
reservation=conn.run_instances(IMAGE,instance_type=INSTANCE_TYPE,key_name=KEY_NAME,placement=ZONE,security_groups=[SECURITY_GROUPS[-1]])
instance=reservation.instances[0]
time.sleep(10)

while not instance.update()=='running':
	time.sleep(3)
time.sleep(10)

print 'Started the load generator: '+str(instance.id)

instance.add_tag('Project','2.1')

data=instance.public_dns_name
f=open('pass.txt')

pan=f.readline()
id1=f.readline()
f.close()

time.sleep(250)
print "hello"
qwe=requests.post("http://"+str(load)+"/password?passwd="+str(pan)+"&andrewId="+str(id1))
print qwe

swq=requests.post("http://"+str(load)+"/test/horizontal?dns="+str(data))
print swq
##Working with the test

start_time=time.time()
end_time=time.time()
count=0
list=[]

while(count<=8):
	IMAGE='ami-1eee9c09'
	KEY_NAME='15319demo' 
	INSTANCE_TYPE='m3.medium'
	ZONE='us-east-1a'
	# Create the EC2 instance 
	print 'Starting the EC2 instance of type {0} with image {1}'.format(INSTANCE_TYPE, IMAGE)
	conn= EC2Connection(access1,secret1)
	SECURITY_GROUPS=conn.get_all_security_groups()
	reservation=conn.run_instances(IMAGE,instance_type=INSTANCE_TYPE,key_name=KEY_NAME,placement=ZONE,security_groups=[SECURITY_GROUPS[-1]])
	instance=reservation.instances[0]
	time.sleep(10)

	while not instance.update()=='running':
		time.sleep(3)
	time.sleep(10)
	print 'Started the load generator: '+str(instance.id)
	list.append(instance.public_dns_name)
	instance.add_tag('Project','2.1')
	end_time=time.time()
	count=count+1
for dat1 in list:
	swq=requests.post("http://"+str(load)+"/test/horizontal/add?dns="+str(dat1))
	print swq
	time.sleep(100)
