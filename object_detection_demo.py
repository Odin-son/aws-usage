from storage_service import StorageService
from recognition_service import RecognitionService

storage_service = StorageService()
recognition_service = RecognitionService()

# aws s3 bucket name
bucket_name = 'bucket.aws'

for file in storage_service.get_all_files(bucket_name):
    if file.key.endswith('.jpg'):
        print(file.key + ' detected from image' + ':')
        labels = recognition_service.detect_objects(file.bucket_name, file.key)

        for label in labels:
            print('-- ' + label['Name']+': '+str(label['Confidence']))

