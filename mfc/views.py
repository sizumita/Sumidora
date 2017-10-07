from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# Create your views here.
from .models import *


def mfc(request,**kwargs):
    q = kwargs['name']
    mfcb = MfcBet.objects.filter(name=q)
    return render(request, 'mfc.html',
                  {'mfcb' : mfcb,
                   'name' : q
                   },dict(kwargs))
#
# def playerview(request,**kwargs):
#     q = kwargs['name']
#     mfcb = MfcBet.objects.filter(name=q)
#     mfcf = MfcBet.objects.filter(name=q)

def mfcfight(request,**kwargs):
    q = kwargs['name']
    mfcf = MfcFight.objects.filter(player1=q)
    return render(request, 'mfcf.html',
                  {'mfcf' : mfcf,
                   'name' : q},dict(kwargs))