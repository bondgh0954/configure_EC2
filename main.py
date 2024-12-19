import boto3 as bt

client = bt.client('ec2')
resource = bt.resource('ec2')
instance_info = client.describe_instances()

res = instance_info['Reservations']
my_instance_ids = []

for ins in res:
    instances = ins['Instances']
    for ids in instances:
        my_instance_ids.append(ids['InstanceId'])

response = resource.create_tags(
    Resources=my_instance_ids,
    Tags=[
        {
            'Key': 'Name',
            'Value': 'Production'
        },
    ]
)

