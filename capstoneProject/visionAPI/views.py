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
from . import translate
from . import getInfo

client = vision.ImageAnnotatorClient()
#path = '/home/ec2-user/capstone/capstoneProject/visionAPI/image/t.png'
#path = '/home/ec2-user/capstone/capstoneProject/visionAPI/image/게보린.jpg'

drugName = solve.extractDrugName()
class API():
    def DrugInfo():
        drugName = solve.extractDrugName()
        data = accessDB.getDrugInformation(drugName)
        data = list(data[0])
        return data

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
        data = format(API.sendDrugInfo())
        
        context = {
            'data' : data
        }
        
        return render(self,'visionAPI/home.html', context)
    
    def translate(self):
        code = getInfo.getLanguage()
        #print(code_test)
        #code = "en"
        data = API.DrugInfo()
        tmp = data
        #print(type(tmp))
        for i in range(0,5):
            #print(type(tmp))
            tmp[i] = str(translate.translation(data[i],code))
        
        col = ['name','ingredient','dosage','effect','caution','nation']
        tmp = ""
        for i in range(0,6):
            tmp = tmp + col[i] + ":" + data[i] + "@!#"
        
        data2 = tmp
        
        context = {
            'data2' : data2
        }
        return render(self, 'visionAPI/translate.html', context)
    

class getInfoFromAndroid():
    def getImage(self):
        return render(self, 'visionAPI/image.html', )
    def getLanCode(self):
        return render(self, 'visionAPI/lanCode.html',)
