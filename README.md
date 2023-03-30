# ebs_resizing
Project describes how to resize the Elastic Block Storage automatically using CloudWatch


Project Description: The background of the project is to resizing the elastic block storage of EC2 instance in several scenarios such as when instance is running out of storage, to improve the performance for I/O operations, to add new application or service to the instance. When the storage reach at particular level of thresold point then it's going to send an alert through CloudWatch service, then CloudWatch service sends the notification to the Lambda function and also sends the Email to the user by SNS service. Here Lambda function uses for the extension of the EBS. 


AWS services which we are going to use:
  1) EC2 (Elastic Compute Cloud) instance
  2) CloudWatch
  3) SNS (Simple Notification Service)
  4) IAM (Identity and Access Management)
  
