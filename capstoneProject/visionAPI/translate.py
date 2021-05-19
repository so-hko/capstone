from google.cloud import translate_v2 as translate
#import google.cloud 
#import translate_v2 as translate
#import translate as translate
import os

os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', '/home/ec2-user/capstone/capstoneProject/visionAPI/My_First_Project-51cda441fdd3.json')


client = translate.Client()
result = client.translate('두통을 해결해줄 수 있다.', target_language='en')
print(result['translatedText'])
