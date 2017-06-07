import boto3
import json
import logging


vpc_id="vpc-32b1fe55"
subnet_id="subnet-a02b94e9"
DbName="testDatabase"
Storage_size=10
instance_size="db.t1.micro "
user_name="test"
user_pwd="Test123"
Vpc_SecurityGroupIds=[
        'sg-4038d03b'
    ]
 Engine="aurora"
db_identifier="ezekiel-test-instance"

print ("Creating an DB 2 INSTANCE")

try:
	print("Processing request to create a DB")

	rds=boto3.client('rds')
	rds_response=rds.create_db_instance(DbName,db_identifier,Storage_size,Engine,user_name,user_pwd,Vpc_SecurityGroupIds)
except Exception as  e:
	print("THE FOLLOWING ERROR OCCURED"+e)
	return rds_response

####TEST