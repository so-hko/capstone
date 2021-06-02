from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
import os, sys
import requests
"""
sys.path.append('/home/ec2-user/capstone/capstoneProject/visionAPI')
from solve import extractDrugName
from accessDB import getImagePath
"""

class sendImage():
    def otcinfoImage(self):
        """
        drugName = extractDrugName()
        image = getImagePath(drugName)
        imagePath = "/home/ec2-user/capstone/capstoneProject/blog/otcinfo_image/" + str(list(image))
        context = {
                'imagePath' : imagePath
         }
        return render(self, 'sendInfo.otcinfoImage.html', imagePath)
        """
        return 0
    def etcinfoImage(self):
        return render(self, 'sendInfo.etcInfoImage.html')
    def pillImage(self):
        return 0
