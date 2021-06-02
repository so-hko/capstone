from django.shortcuts import render
from django.http import HttpResponse
import os, sys

sys.path.append('/home/ec2-user/capstone/capstoneProject/visionAPI')
from solve import extractDrugName
from accessDB import getImagePath


"""
class blog():
    def otcinfoImage(self):
        drugName = extractDrugName()
        image = getImagePath(drugName)
        imagePath = "/home/ec2-user/capstone/capstoneProject/blog/otcinfo_image/" + str(list(image))
        context = {
            'imagePath' : imagePath
         }
        return render(self, 'blog.otcinfoImage.html', imagePath)
    def etcinfoImage(self):
        return 0

    def pillImage(self):
        return 0
    """


from.models import OTCInfo, ETCInfo, Pill

def otcinfo(request):
    drugName = extractDrugName()
    image = getImagePath()
    imagePath = list(image[0])[0]
    context = { 'imagePath' : imagePath }
    return render(requeset, 'otcinfoImage.html',context)

def etcinfo(request):
    etcinfos = ETCInfo.objects
    return render(request, 'etcinfoImage.html', {'etcinfos' : etcinfos})

def pill(request):
    drugName = extractDrugName()
    #image = getImagePath(drugName)
    image = getImagePath()
    #imagePath = "/home/ec2-user/capstone/capstoneProject/blog/otcinfo_image" + str(list(image))
    #imagePath = "/home/ec2-user/capstone/capstoneProject/otc_image/메카인정.png"
    imagePath = list(image[0])[0]

    context = {
            'imagePath': imagePath
    }
    return render(request, 'pillImage.html', context)
    #pills = Pill.objects
    #return render(request, 'pillImage.html', {'pills' : pills})

