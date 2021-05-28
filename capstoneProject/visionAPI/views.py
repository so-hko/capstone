from django.shortcuts import render
import requests
# Create your views here.
"""Detects text in the file."""
from google.cloud import vision
import io
import os
import subprocess
from . import solve
from . import accessDB

client = vision.ImageAnnotatorClient()
#path = '/home/ec2-user/capstone/capstoneProject/visionAPI/image/t.png'
path = '/home/ec2-user/capstone/capstoneProject/visionAPI/image/게보린.jpg'

detectedText = []
class API():
    def sendDrugInfo():
        drugName = solve.extractDrugName()
        data = accessDB.getDrugInformation(drugName)
        #print(data)
        data = list(data[0])
        col = ['name','ingredient','dosage','effect','caution','nation']
        str = ""
        for i in range(0,6):
            str = str + col[i] + ":" + data[i] + "@!#"
        return str

    def home(self):
        data = API.sendDrugInfo()
        
        context = {
            'data' : data
        }
        
        return render(self,'visionAPI/home.html', context)
    

class getInfoFromAndroid():
    def getImage(self):
        return render(self, 'visionAPI/image.html', )
    def getLanCode(self):
        return render(self, 'visionAPI/lanCode.html',)
