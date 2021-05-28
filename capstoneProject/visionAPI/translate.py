from google.cloud import translate_v2 as translate
#import google.cloud 
#import translate_v2 as translate
#import translate as translate
import os
import getDbInfo
#import getDrugInfo
info = "나는 배가 지금 너무 많이 고프다"

os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', '/home/ec2-user/capstone/capstoneProject/visionAPI/My_First_Project-51cda441fdd3.json')
client = translate.Client()

def translate(info): 
    print(info)
    result = client.translate(info, target_language='en')
    print(result['translatedText'])
    return result['translatedText']


translate(info)

