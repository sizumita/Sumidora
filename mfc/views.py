# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# Create your views here.
from .models import *
from pprint import pprint

def mfc(request,**kwargs):
    q = kwargs['name']
    mfcb = MfcBet.objects.filter(name=q)
    return render(request, 'mfc.html',
                  {'mfcb' : mfcb,
                   'name' : q
                   },dict(kwargs))

def playerview(request, **kwargs):
    wins = 0
    lose = 0
    mony = 0
    usemony = 0
    i = []
    q = kwargs['name']
    mfcb = MfcBet.objects.filter(name=q)
    mfcpb = MfcproBet.objects.filter(name=q)
    mfcf = MfcFight.objects.filter(player1=q) #USE
    mfcf2 = MfcFight.objects.filter(player2=q) #USE
    mfcpf = MfcproFight.objects.filter(player1=q)#USE
    mfcpf2 = MfcproFight.objects.filter(player2=q)#USE

    for x in mfcb:
        num = x.profit
        mony = mony + num

    for x in mfcpb:
        num = x.profit
        mony = mony + num

    for x in mfcb:
        num = x.bet
        usemony = usemony + num

    for x in mfcpb:
        num = x.bet
        usemony = usemony + num

    for x in mfcf:
        if x.winner == x.uuid1:
            wins = wins + 1
        else:
            lose = lose + 1

    kd = wins / lose
    return render(request, 'playerdata.html',
                  {'kd' : kd,
                   'wins' : wins,
                   'lose' : lose,
                   'mony' : mony,
                   'usemony' : usemony,
                   'name' : q},dict(kwargs))



def mfcfight(request,**kwargs):
    q = kwargs['name']
    mfcf = MfcFight.objects.filter(player1=q),MfcFight.objects.filter(player2=q)
    print(mfcf)
    return render(request, 'mfcf.html',
                  {'mfcf' : mfcf,
                   'name' : q},dict(kwargs))