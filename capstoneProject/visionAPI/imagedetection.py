"""Detects text in the file."""
from google.cloud import vision
import io
client = vision.ImageAnnotatorClient()
path = 'C:\\Users\\USER\\Desktop\\textmining\\image\\게보린.jpg'

def imagedetection(path):
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    price_candidate = []
    card_number_candidate = []
    date_candidate = []

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')

    for text in texts:
        content = text.description
        content = content.replace(',','')
        print('\n"{}"'.format(content))


    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return content