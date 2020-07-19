#import django
#django.setup()

from  comon import  *


SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'e^9s8q1bp*n$g@wrs46)0#!*g4@2dw1d8v=*=tu_iv-483h=^u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
