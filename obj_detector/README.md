### Detecting object from bucket (S3)
---
![obj-detector](https://user-images.githubusercontent.com/33476636/176391630-8874826d-aa0a-4f09-a59a-1dd4486dbb00.png)

1. before starting, identify AWS configuration
```
$ cat ~/.aws/config
$ cat ~/.aws/credentials
```
creating a group [IAM](https://us-east-1.console.aws.amazon.com/iamv2) if initial setup is required
```
$ aws configuare
```

2. related libraries installation
```
$ pip install boto3, chalice
```

3. create [Amazon S3 bucket](https://s3.console.aws.amazon.com/s3) and modify code below

in `capabilities/app.py:11`,
```
# aws s3 bucket name
storage_location = 'bucket.aws'
```

4. chalice depolyment
```
$ cd capabilities
$ chalice depoly
Creating deployment package.
Creating IAM role: capabilities-dev-api_handler
Creating lambda function: capabilities-dev
Creating Rest API
Resources deployed:
- Lambda ARN: arn:aws:lambda:us-east-1:<UID>:function:capabilities-dev
- Rest API URL: https://<UID>.execute-api.us-east-1.amazonaws.com/api/
```