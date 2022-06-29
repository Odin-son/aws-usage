from chalice import Chalice
from chalicelib.storage_service import StorageService
from chalicelib.recognition_service import RecognitionService

import random


app = Chalice(app_name='capabilities')
app.debug = True

# aws s3 bucket name
storage_location = 'bucket.aws'
storage_service = StorageService(storage_location)
recognition_service = RecognitionService(storage_service)

@app.route('/demo-obj-detection', cors=True)
def demo_obj_detection():
    files = storage_service.list_files()
    images = [file for file in files if file['file_name'].endswith('.jpg')]
    image = random.choice(images)

    objects = recognition_service.detect_objects(image['file_name'])

    return {
        "imageName": image['file_name'],
        "imageUrl": image['url'],
        "objects": objects
    }
