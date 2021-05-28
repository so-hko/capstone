# -*- coding: utf-8 -*-
"""Detects text in the file."""
from google.cloud import vision
import io
import os

os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', '/home/ec2-user/capstone/capstoneProject/visionAPI/My_First_Project-51cda441fdd3.json')

client = vision.ImageAnnotatorClient()
#path = '/home/ec2-user/capstone/capstoneProject/visionAPI/image/t.png'
def imagedetection():
    path = "/home/ec2-user/capstone/capstoneProject/visionAPI/drug_image.jpg"
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    price_candidate = []
    card_number_candidate = []
    date_candidate = []
    detectedText = []
    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')

    for text in texts:
        content = text.description
        content = content.replace(',','')
        print('\n"{}"'.format(content))
        detectedText.append(content)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return detectedText[0]

