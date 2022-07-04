# amazon rekognition usage

![](https://d1.awsstatic.com/product-marketing/Rekognition/Streaming-video-feature.d94ac284c8b4a250ea0b467f52e0cb60b4c30175.png)

1. install package
```
$ pip install awscli
$ awscli --version
```

2. set up parameters
```
$ aws configure
$ cat ~/.aws/config
$ cat ~/.aws/credentials
```

3. in `object_detection_demo.py`, change the string value for the s3-bucket name
```python
# aws s3 bucket name
bucket_name = 'bucket.aws'
```

4. run `object_detection_demo.py`
```bash
$ python object_detection_demo.py
```