Step 1: Creating ec2 instance with the name of dhrumil_ec2_2 (screenshot ec2_name). Having the EBS of 8 GB intially.

Step 2: Assigning the new role to the ec2 instance, having a policy of CloudWatchAgentPolicy. 
        Name of the assign role is dhrumil_ec2_ebs(screenshot ec2_role)
Reason - This policy helps the ec2 instance to control the permission and access to Amazon Cloudwatch logs and matric data.

Step 3: Get connect with the EC2 instance's command line interface for the installation of Cloudwatch agent.
Reason - Agent collect the metrics on the EC2 instance CPU usage, memory usage, disk utilization and system level metrics. 
         It also collects the log data of EC2 instance. This log includes files from OS, applications and custom log files.

Step 4: Initally we need to install cloud watch agent using 'yum install' command
        Command - sudo yum install -y amazon-cloudwatch-agent

Step 5: After the installation of cloudwatch agent we need to configure the CloudWatch agent by creating configuration file.
        Command - sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard

Step 6: Starting the CloudWatch agent after the successful creation of configuration file. 
        Command - sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/path/to/your/config.json
        Here the path of the Configuration file is /opt/aws/amazon-cloudwatch-agent/bin

After Successfully installation of CloudWatch agent, it will start collecting metrics and logs from the EC2 instance sends to the Cloud agent.

Step 7: Just for the confirmation of agent is working or not we can run below command.(Screenshot ec2_agent_confirmation)
        Command: sudo systemctl status amazon-cloudwatch-agent
