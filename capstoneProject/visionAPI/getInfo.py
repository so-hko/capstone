import subprocess
from bs4 import BeautifulSoup
import requests
import time
def getImage():
    #url = "\"https://i-cf65ch.gskstatic.com/content/dam/cf-consumer-healthcare/bp-advil/en_US/products/advil-gel-caplets-new_0_0.png?auto=format\""
    
    url = "\"http://img.etoday.co.kr/pto_db/2016/10/20161017060044_956246_350_255.jpg\""

    #url = "http://ec2-18-217-179-233.us-east-2.compute.amazonaws.com:8000/visionAPI/image/"  
    print("curl " + url)
    subprocess.call("curl " + url + " > drug_image.jpg", shell=True)

def getLanguage():
    url = requests.get("http://ec2-18-217-179-233.us-east-2.compute.amazonaws.com:8000/visionAPI/lanCode/").text    
    getCode = BeautifulSoup(url, 'html.parser')
    print(type(getCode.get_text()))
    print(getCode.get_text().rstrip())
    return getCode.get_text().rstrip()

