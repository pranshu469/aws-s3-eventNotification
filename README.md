# aws-s3-eventNotification

User Data Ingestion – Processing file in a branched workflow

1.	In this architecture, user uploads a CSV file to S3 bucket and we have configured an EventBridge rule for PUT event for suffix .csv
2.	EventBridge rule will trigger Step functions workflow where we have a branched sequence workflow of Lambda function execution.
3.	Lambda 1 : Convert the CSV file to JSON and store them in the same S3 bucket under a folder created by timestamps. For eg: 2024/05/29/1716967027.json
4.	Lambda 2 : It will store the metadata of the file, like PUT object event, timestamp, file size, etc to the DynamoDB table.
5.	If the upload is successful we’ll notify admin user that the file is uploaded to DynamoDB table successfully.
6.	However, if there is an error in uploading file to DynamoDB, we’ll notify user of failed event via SNS topic.

Architecture Diagram : https://github.com/pranshu469/aws-s3-eventNotification/blob/main/architecture.png


 
