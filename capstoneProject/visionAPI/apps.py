from django.apps import AppConfig
import os
import subprocess

class VisionapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visionAPI'

    def ready(self):
        #TODO: When my codes to run on startup;
        os.system("export GOOGLE_APPLICATION_CREDENTIALS='/home/ec2-user/capstone/capstoneProject/visionAPI/My_First_Project-51cda441fdd3.json'")
        pass

