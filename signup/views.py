from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from passlib.hash import pbkdf2_sha256
import json


# Create your views here.

