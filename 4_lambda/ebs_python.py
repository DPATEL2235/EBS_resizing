import boto3    
   
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')    
    
    response = ec2.modify_volume(    
        VolumeId='volume_id of your ec2 instance',    
        Size='till you want to extend')  