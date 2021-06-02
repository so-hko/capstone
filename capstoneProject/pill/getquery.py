from bs4 import BeautifulSoup
import requests

def getq():
    source = requests.get('http://ec2-18-217-179-233.us-east-2.compute.amazonaws.com:8000/visionAPI/etcinfoImage/').text
    pillquery = BeautifulSoup(source, 'html.parser')
    print(pillquery)
    #return pillquery.get_text().rstrip()
