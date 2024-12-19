# Automate configuring EC2 Server Instances 


# Technologies used
  Python: boto library
  AWS

# Project Description:
  Write a Python script that automates adding environment tags to all EC2 Server instances


# Motivation of project
Assuming we have 20 servers created in one region which are used as production servers and another 10 servers created in a different region which are used as development servers. Adding environment tags one after the other may be time consuming and therefore With the use of python script it is easier to add tags to these servers.

# Steps
Get all instances from a region and save them in a list

create an empty list

      my_instance_ids = []

Use the for loop to loop through the instances and grab the instanceId and append them in the empty list




Add tags to the instances

Use the boto resource to create tags for the instances Id




