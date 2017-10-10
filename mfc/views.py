# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# Create your views here.
from .models import *
from pprint import pprint
from django.db.models import Q

# for x in mfcb:
#     num = x.profit
#     mony = round((mony + num))
#
# for x in mfcpb:
#     num = x.profit
#     mony = round((mony + num))
#
# for x in mfcb:
#     num = x.bet
#     usemony = round((usemony + num))
#
# for x in mfcpb:
#     num = x.bet
#     usemony = round((usemony + num))








def mfc(request,**kwargs):
    q = kwargs['name']
    page = 1
    param_value = request.GET.get("page")
    try:
        param_value = int(param_value)
        nextpage = param_value + 1
        if param_value == 1:
            old = 1
        else:
            old = param_value - 1
        page = param_value * 20
        pages = page - 20
    except:
        pages = 0
        page = 20
        old = 1
        nextpage = 2
    param_values = request.GET.get("mode")
    if param_values == 'pro':
        mfcb = MfcproBet.objects.filter(Q(name=q)).distinct().order_by('-id')[pages:page]
    else:
        mfcb = MfcBet.objects.filter(Q(name=q)).distinct().order_by('-id')[pages:page]
    return render(request, 'mfc.html',
                  {'mfcb' : mfcb,
                   'name' : q,
                   'page' : page,
                   'pages' : pages,
                   'next' : nextpage,
                   'old' : old
                   },dict(kwargs))


def mfcfight(request,**kwargs):
    page = 1
    param_values = request.GET.get("page")
    if param_values:
        param_values = int(param_values)
        nextpage = param_values + 1
        if param_values == 1:
            old = 1
        else:
            old = param_values - 1
        page = param_values * 20
        pages = page - 20

    else:
        page = 20
        pages = 0
        nextpage = 2
        old = 1
    q = kwargs['name']
    param_value = request.GET.get("mode")
    if param_value == 'pro':
        mfcf = MfcproFight.objects.filter(Q(player1=q) | Q(player2=q)).distinct().order_by('-datetime')[pages:page]
    else:
        mfcf = MfcFight.objects.filter(Q(player1=q) | Q(player2=q)).distinct().order_by('-datetime')[pages:page]
    return render(request, 'mfcf.html',
                  {'mfcf' : mfcf,
                   'name' : q,
                   'page': page,
                   'pages': pages,
                   'next': nextpage,
                   'old': old,
                   'param' : param_value},dict(kwargs))



def playerview(request, **kwargs):
    q = kwargs['name']
    param_value = request.GET.get("mode")
    type = request.GET.get('type')
    if type != 'bet':
        wins = 0
        lose = 0
        playerprize = 0
        if param_value != "pro":
            mfcf = MfcFight.objects.filter(player1=q)
            mfcf2 = MfcFight.objects.filter(player2=q)
            fight = MfcFight.objects.filter(Q(player1=q) | Q(player2=q)).distinct().order_by('-datetime')[0:20]
        else:
            mfcf = MfcproFight.objects.filter(player1=q)
            mfcf2 = MfcproFight.objects.filter(player2=q)
            fight = MfcproFight.objects.filter(Q(player1=q) | Q(player2=q)).distinct().order_by('-datetime')[0:20]



        for x in mfcf:
            if x.winner == x.uuid1:
                wins = wins + 1
                playerprize = round(playerprize + x.prize)
            else:
                lose = lose + 1
        for x in mfcf2:
            if x.winner != x.uuid1:
                wins = wins + 1
            else:
                lose = lose + 1
                playerprize = round(playerprize + x.prize)
        all = wins + lose + playerprize
        if all > 0:
            score = round(playerprize / (wins + lose) * 0.001)
            kd = round((wins / lose),2)
            playerprize = playerprize - (wins + lose)*10000
        else:
            return render_to_response("eroor.html")
        return render(request, 'playerdata.html',
                      {'kd' : kd,
                       'wins' : wins,
                       'lose' : lose,
                       'prize' : playerprize,
                       'score' : score,
                       'fight' : fight,
                       'param' : param_value,
                       'name' : q,
                       'type' : type},dict(kwargs))

    else:
        profit = 0
        bet = 0
        num = 0
        win = 0
        lose = 0
        if param_value == 'pro':
            mfc = MfcproBet.objects.filter(name=q)
        else:
            mfc = MfcBet.objects.filter(name=q)
        for x in mfc:
            profit = profit + x.profit
            bet = bet + x.bet
            num = num + 1
            if x.win == 1:
                win = win + 1
            else:
                lose = lose + 1
        mony = profit / bet * 100
        return render(request,'playerbet.html',
                      {
                          "name" : q,
                          "profit" : profit,
                          "bet" : bet,
                          'num' : num,
                          "mony" : mony,
                          'win' : win,
                          'lose' : lose,
                          'type' : type,
                          "param" : param_value
                      },dict(kwargs))








def fightdata(request,**kwargs):
    q = kwargs['number']
    try:
        if int(q) < 24 :
            return render(request,"eroor.html")
    except:
        return render_to_response("eroor.html")
    param_value = request.GET.get("mode")
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
        bet = MfcBet.objects.filter(fight_id=q).order_by("-bet")
        for x in fight:
            old = MfcFight.objects.filter(player1=x.player1, player2=x.player2)
            olds = MfcFight.objects.filter(player1=x.player2, player2=x.player1)
    else:
        fight = MfcproFight.objects.filter(id=q)
        bet = MfcproBet.objects.filter(fight_id=q).order_by("-bet")
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
                   'alls' : alls,
                   'param' : param_value
                   },
                  dict(kwargs))









def ranking(requset,**kwargs):
    q = kwargs['name']
    model = MfcBet.objects.filter(name=q).only('profit').count()

