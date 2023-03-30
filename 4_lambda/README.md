IN last phase we are going to use lambda function for the expansion of the ebs. For that we need to create the role for the lambda function to get the authority of changes in EC2 instance's storage. 

Step 1: Creating the role for lambda function with having two policies in it. First is AmazonEC2FullAccess and                    AmazonEBSCSIDriverPolicy. (screenshot lambda_policy)

Step 2: Creating the lambda function with the unique name and having existing role which we created just before it. We are going with the python as a language

Step 3: In the function overview with the lambda function, we have two field trigger and destination. So here in the trigger we are going to select sns and existing topic which we used in cloudwatch for the trigger this lambda function (screenshot lambda_overview)

Step 4: In lambda function we need few line of code which expand the ebs of our ec2 instance and that python file is ebs_python.py(4_lambda\ebs_python.py)

