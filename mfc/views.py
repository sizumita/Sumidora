# -*- coding: utf-8 -*-
from django.http import Http404
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
    mfcf = MfcFight.objects.filter(player1=q)
    mfcf2 = MfcFight.objects.filter(player2=q)

    return render(request, 'mfcf.html',
                  {'mfcf' : mfcf,
                   'mfcfs' : mfcf2,
                   'name' : q},dict(kwargs))

def fightdata(request,**kwargs):
    q = kwargs['name']
    try:
        if int(q) < 24 :
            return render(request,"eroor.html")
    except:
        return render(request,"eroor.html")
    param_value = request.GET.get("q")
    player1 = '負け'
    player2 = '負け'
    winner1 = 0
    winner2 = 0
    lose1 = 0
    lose2 = 0
    prize1 = 0
    prize2 = 0
    if param_value != "pro":
        fight = MfcFight.objects.filter(id=q)
        bet = MfcBet.objects.filter(fight_id=q)
        for x in fight:
            old = MfcFight.objects.filter(player1=x.player1, player2=x.player2)
            olds = MfcFight.objects.filter(player1=x.player2, player2=x.player1)
    else:
        fight = MfcproFight.objects.filter(id=q)
        bet = MfcproBet.objects.filter(fight_id=q)
        for x in fight:
            old = MfcproFight.objects.filter(player1=x.player1, player2=x.player2)
            olds = MfcproFight.objects.filter(player1=x.player2, player2=x.player1)




    for x in old:
        if x.winner == x.player1:
            winner1 = winner1 + 1
            lose2 = lose2 + 1
        else:
            winner2 = winner2 + 1
            lose1 = lose1 + 1

    for x in olds:
        if x.winner != x.player1:
            winner1 = winner1 + 1
            lose2 = lose2 + 1
        else:
            winner2 = winner2 + 1
            lose1 = lose1 + 1

    alls = winner1 + winner2


    for x in fight:
        if x.winner == x.player1:
            player1 = '勝ち'
            prize1 = x.prize
        else:
            player2 = '勝ち'
            prize2 = x.prize



    return render(request,'fight_data.html',
                  {'fight' : fight,
                   'bet' : bet,
                   'player1' : player1,
                   'player2' : player2,
                   'pr1' : prize1,
                   'pr2' : prize2,
                   'winner1' : winner1,
                   'winner2' : winner2,
                   'lose1' : lose1,
                   'lose2' : lose2,
                   'alls' : alls
                   },
                  dict(kwargs))



