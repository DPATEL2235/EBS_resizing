After the Succesfull installion of the CloudWatch agent into ec2 instance we need to create the alert of the EBS using CloudWatch serive of AWS. SO for that need to follow the below steps

Step 1: Selecting the metric from thr CWagent namespace(screentshot: cw_cwagent)

Step 2: Selecting the metric which has the path '/' and 'disk use for percent' as per (screenshot cw_path_metric)

Step 3: In the statistic selecting Maximum because we want the ebs thresold value to more than 80%. Period is just for after howmany minutes you want to send agent to check the storage.

Step 4: In the notification section we need to create the new topic with help of SNS service of the AWS which has been shown in the 3_sns folder.
