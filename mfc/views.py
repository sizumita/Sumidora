# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
# Create your views here.
from .models import *
from django.db.models import Q,Sum



def mfcbet(request,**kwargs):
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
        url = 'promfc.html'
    else:
        mfcb = MfcBet.objects.filter(Q(name=q)).distinct().order_by('-id')[pages:page]
        url = 'mfc.html'
    parameter = {
        'mfcb' : mfcb,
        'name' : q,
        'page' : page,
        'pages' : pages,
        'next' : nextpage,
        'old' : old
    }
    return render(request, url,parameter,dict(kwargs))



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
        url = 'promfcf.html'
    else:
        mfcf = MfcFight.objects.filter(Q(player1=q) | Q(player2=q)).distinct().order_by('-datetime')[pages:page]
        url = 'mfcf.html'
    parameter = {
                    'mfcf' : mfcf,
                   'name' : q,
                   'page': page,
                   'pages': pages,
                   'next': nextpage,
                   'old': old,
                   'param' : param_value
                 }
    return render(request, url,parameter,dict(kwargs))



def playerview(request, **kwargs):
    q = kwargs['name']
    param_value = request.GET.get("mode")
    type = request.GET.get('type')
    uuid = type
    if type != 'bet':
        wins = 0
        lose = 0
        playerprize = 0
        if param_value != "pro":
            mfcfight = MfcFight.objects.filter(Q(player1=q)|Q(uuid1=uuid)).distinct()
            mfcf2 = MfcFight.objects.filter(Q(player2=q)|Q(uuid2=uuid)).distinct()
            fight = MfcFight.objects.filter(Q(player1=q) | Q(player2=q)|Q(player2=q)|Q(uuid2=uuid)).distinct().order_by('-datetime')[0:20]
        else:
            mfcfight = MfcproFight.objects.filter(Q(player1=q)|Q(uuid1=uuid)).distinct()
            mfcf2 = MfcproFight.objects.filter(Q(player2=q)|Q(uuid2=uuid)).distinct()
            fight = MfcproFight.objects.filter(Q(player1=q) | Q(player2=q)|Q(player2=q)|Q(uuid2=uuid)).distinct().order_by('-datetime')[0:20]



        for x in mfcfight:
            if x.winner == x.uuid1:
                wins += 1
                playerprize = round(playerprize + x.prize)
            else:
                lose += 1
        for x in mfcf2:
            if x.winner != x.uuid1:
                wins += 1
            else:
                lose += 1
                playerprize = round(playerprize + x.prize)
        total = wins + lose + playerprize
        if total > 0:
            score = round(playerprize / (wins + lose) * 0.001)
            kd = round((wins / lose),2)
            playerprize = playerprize - (wins + lose)*10000
        else:
            return render_to_response("eroor.html")
        url = 'playerdata.html'
        param_value = str(param_value)
        url = param_value + url
        url = url.lstrip('None')
        parameter = {
                        'kd' : kd,
                       'wins' : wins,
                       'lose' : lose,
                       'prize' : playerprize,
                       'score' : score,
                       'fight' : fight,
                       'param' : param_value,
                       'name' : q,
                       'type' : type
                     }
        return render(request, url,parameter,dict(kwargs))

    else:
        profit = 0
        bet = 0
        num = 0
        win = 0
        lose = 0
        if param_value == 'pro':
            mfc = MfcproBet.objects.filter(name=q)
            url = 'proplayerbet.html'
        else:
            mfc = MfcBet.objects.filter(name=q)
            url = 'playerbet.html'
        for x in mfc:
            profit += x.profit
            bet = bet + x.bet
            num += 1
            if x.win == 1:
                win += 1
            else:
                lose += 1
        mony = profit / bet * 100
        profits = profit / (win + lose)
        parameter = {
                          "name": q,
                          "profit": profit,
                          "bet": bet,
                          'num': num,
                          "mony": mony,
                          'win': win,
                          'lose': lose,
                          'type': type,
                          "param": param_value,
                          'profits': profits
                      }
        url = 'playerbet.html'
        return render(request, url,parameter,dict(kwargs))




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
        url = 'fight_data.html'
    else:
        fight = MfcproFight.objects.filter(id=q)
        bet = MfcproBet.objects.filter(fight_id=q).order_by("-bet")
        for x in fight:
            old = MfcproFight.objects.filter(player1=x.player1, player2=x.player2)
            olds = MfcproFight.objects.filter(player1=x.player2, player2=x.player1)
        url = 'profight_data.html'



    try:
        for x in old:
            if x.winner == x.player1:
                winner1 += 1
                lose2 += 1
            else:
                winner2 = winner2 + 1
                lose1 += 1
        for x in olds:
            if x.winner == x.player1:
                winner1 += 1
                lose2 += 1
            else:
                winner2 += 1
                lose1 += 1

    except:
        return render_to_response('eroor.html')

    alls = winner1 + winner2


    for x in fight:
        if x.winner == x.player1:
            player1 = '勝ち'
            prize1 = x.prize
        else:
            player2 = '勝ち'
            prize2 = x.prize

    parameter = {'fight': fight,
     'bet': bet,
     'player1': player1,
     'player2': player2,
     'pr1': prize1,
     'pr2': prize2,
     'winner1': winner1,
     'winner2': winner2,
     'lose1': lose1,
     'lose2': lose2,
     'alls': alls,
     'param': param_value
     }


    return render(request, url,parameter,dict(kwargs))



def ranking(request):
    param_values = request.GET.get("mode")
    type = request.GET.get('type')
    if param_values == 'bet':
        if type == 'pro':
            title = 'Bet金額のランキング（１から１００位まで）'
            sub = '総Bet金額'
            unit = '円'
            model = MfcproBet.objects.all().values("name").annotate(bet=Sum('bet')).order_by('-bet')[0:100]
        else:
            model = MfcBet.objects.all().values("name").annotate(bet=Sum('bet')).order_by('-bet')[0:100]
    elif param_values == 'profit':
        sub = '総獲得金額'
        unit = '円'
        title = '獲得金額のランキング（１から１００位まで）'
        if type == 'pro':
            model = MfcproBet.objects.all().values("name").annotate(bet=Sum('profit')).order_by('-bet')[0:100]
        else:
            model = MfcBet.objects.all().values("name").annotate(bet=Sum('profit')).order_by('-bet')[0:100]
    elif param_values == 'Ra':
        title = '回収率のランキング（１から１００位まで）'
        sub = '回収率'
        unit = '%'
        """Recover amount=回収金額"""
        if type == 'pro':
            model = MfcproBet.objects.all().values("name").annotate(bet=(Sum('profit')/Sum('bet')*100)).order_by('-bet')[0:100]
        else:
            model = MfcBet.objects.all().values("name").annotate(bet=(Sum('profit')/Sum('bet')*100)).order_by('-bet')[0:100]
    else:
        model = MfcBet.objects.all().values("name").annotate(bet=Sum('bet')).order_by('-bet')[0:100]
        title = 'Bet金額のランキング（１から１００位まで）'
        sub = '総Bet金額'
        unit = '円'
    id = 1
    for x in model:
        x.update({ 'id' : id})
        id += 1


    parameter = {
                  'model' : model,
                  "title" : title,
                  'sub' : sub,
                  'unit' : unit,
                  }
    if type == 'pro':
        url = 'proranking.html'
    else:
        url = 'proranking.html'
    return render(request,url,parameter)



def playerfightview(request):
    player1win = 0
    player2win = 0
    player1lose = 0
    player2lose = 0
    player1 = request.GET.get("p1")
    player2 = request.GET.get("p2")
    mode = request.GET.get('mode')
    if mode == 'pro':
        fight1 = MfcproFight.objects.filter(player1=player1,player2=player2)
        fight2 = MfcproFight.objects.filter(player1=player2,player2=player1)
    else:
        fight1 = MfcFight.objects.filter(player1=player1, player2=player2)
        fight2 = MfcFight.objects.filter(player1=player2, player2=player1)

    for x in fight1:
        if x.uuid1 == x.winner:
            player1win += 1
            player2lose += 1
        else:
            player2win += 1
            player1lose += 1

    for x in fight2:
        if x.uuid1 == x.winner:
            player2win += 1
            player1lose += 1
        else:
            player1win += 1
            player2lose += 1
    parameter = {
        'p1w' : player1win,
        'p1l' : player1lose,
        'p2w' : player2win,
        'p2l' : player2lose,
        'p1' : player1,
        'p2' : player2,
    }
    url = 'pvpinfo.html'
    return render(request,url,parameter)

