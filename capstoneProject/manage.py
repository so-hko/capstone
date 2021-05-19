#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys



if __name__ == '__main__':
    """Run administrative tasks."""
    os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', '/home/ec2-user/capstone/capstoneProject/visionAPI/My_First_Project-51cda441fdd3.json')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capstoneProject.settings')
    #os.system("export GOOGLE_APPLICATION_CREDENTIALS='/home/ec2-user/capstone/capstoneProject/visionAPI/My_First_Project-51cda441fdd3.json'")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
