# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
# Create your views here.
from .models import *
from django.db.models import Q,Sum


def toppage(request):
    if request.method == 'POST':
        q = request.POST['name']

        return render(request, 'jump.html',
                      {
                       'name' : q,
                       })

    return render(request,'toppage.html')



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
        return render(request, 'promfc.html',
                      {'mfcb': mfcb,
                       'name': q,
                       'next': nextpage,
                       'old': old
                       }, dict(kwargs))
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
        return render(request, 'promfcf.html',
                      {'mfcf': mfcf,
                       'name': q,
                       'page': page,
                       'pages': pages,
                       'next': nextpage,
                       'old': old,
                       'param': param_value}, dict(kwargs))
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
    uuid = request.GET.get('type')
    if type != 'bet':
        wins = 0
        lose = 0
        playerprize = 0
        if param_value != "pro":
            mfcf = MfcFight.objects.filter(Q(player1=q)|Q(uuid1=uuid)).distinct()
            mfcf2 = MfcFight.objects.filter(Q(player2=q)|Q(uuid2=uuid)).distinct()
            fight = MfcFight.objects.filter(Q(player1=q) | Q(player2=q)|Q(player2=q)|Q(uuid2=uuid)).distinct().order_by('-datetime')[0:20]
        else:
            mfcf = MfcproFight.objects.filter(Q(player1=q)|Q(uuid1=uuid)).distinct()
            mfcf2 = MfcproFight.objects.filter(Q(player2=q)|Q(uuid2=uuid)).distinct()
            fight = MfcproFight.objects.filter(Q(player1=q) | Q(player2=q)|Q(player2=q)|Q(uuid2=uuid)).distinct().order_by('-datetime')[0:20]



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
        if param_value == 'pro':
            return render(request, 'proplayerdata.html',
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
        profits = profit / (win + lose)
        if param_value == 'pro':
            return render(request,'proplayerbet.html',
                          {
                              "name" : q,
                              "profit" : profit,
                              "bet" : bet,
                              'num' : num,
                              "mony" : mony,
                              'win' : win,
                              'lose' : lose,
                              'type' : type,
                              "param" : param_value,
                              'profits' : profits
                          },dict(kwargs))
        else:
            return render(request, 'playerbet.html',
                          {
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
                          }, dict(kwargs))




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



    try:
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

    except:
        return render_to_response('eroor.html')

    if param_value == 'pro':
        return render(request,'profight_data.html',
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
    else:
        return render(request, 'fight_data.html',
                      {'fight': fight,
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
                       },
                      dict(kwargs))



def ranking(request):
    param_values = request.GET.get("mode")
    type = request.GET.get('type')
    if param_values == 'bet':
        if type == 'pro':
            model = MfcproBet.objects.all().values("name").annotate(bet=Sum('bet')).order_by('-bet')[0:100]
            title = 'Bet金額のランキング（１から１００位まで）'
            sub = '総Bet金額'
            unit = '円'
        else:
            model = MfcBet.objects.all().values("name").annotate(bet=Sum('bet')).order_by('-bet')[0:100]
            title = 'Bet金額のランキング（１から１００位まで）'
            sub = '総Bet金額'
            unit = '円'
    elif param_values == 'profit':
        if type == 'pro':
            model = MfcproBet.objects.all().values("name").annotate(bet=Sum('profit')).order_by('-bet')[0:100]
            title = '獲得金額のランキング（１から１００位まで）'
            sub = '総獲得金額'
            unit = '円'
        else:
            model = MfcBet.objects.all().values("name").annotate(bet=Sum('profit')).order_by('-bet')[0:100]
            title = '獲得金額のランキング（１から１００位まで）'
            sub = '総獲得金額'
            unit = '円'
    elif param_values == 'Ra':
        """Recover amount=回収金額"""
        if type == 'pro':
            model = MfcproBet.objects.all().values("name").annotate(bet=(Sum('profit')/Sum('bet')*100)).order_by('-bet')[0:100]
            title = '回収率のランキング（１から１００位まで）'
            sub = '回収率'
            unit = '%'
        else:
            model = MfcBet.objects.all().values("name").annotate(bet=(Sum('profit')/Sum('bet')*100)).order_by('-bet')[0:100]
            title = '回収率のランキング（１から１００位まで）'
            sub = '回収率'
            unit = '%'

    else:
        model = MfcBet.objects.all().values("name").annotate(bet=Sum('bet')).order_by('-bet')[0:100]
        title = 'Bet金額のランキング（１から１００位まで）'
        sub = '総Bet金額'
        unit = '円'
    id = 1
    for x in model:
        x.update({ 'id' : id})
        id = id + 1



    if type == 'pro':
        return render(request,'proranking.html',
                      {
                          'model' : model,
                          "title" : title,
                          'sub' : sub,
                          'unit' : unit
                      })
    else:
        return render(request,'ranking.html',
                      {
                          'model' : model,
                          "title" : title,
                          'sub' : sub,
                          'unit' : unit
                      })



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
        for x in fight1:
            if x.uuid1 == x.winner:
                player1win = player1win + 1
                player2lose = player2lose + 1
            else:
                player2win = player2win + 1
                player1lose = player1lose + 1

        for x in fight2:
            if x.uuid1 == x.winner:
                player2win = player2win + 1
                player1lose = player1lose + 1
            else:
                player1win = player1win + 1
                player2lose = player2lose + 1
    else:
        fight1 = MfcFight.objects.filter(player1=player1, player2=player2)
        fight2 = MfcFight.objects.filter(player1=player2, player2=player1)
        for x in fight1:
            if x.uuid1 == x.winner:
                player1win = player1win + 1
                player2lose = player2lose + 1
            else:
                player2win = player2win + 1
                player1lose = player1lose + 1

        for x in fight2:
            if x.uuid1 == x.winner:
                player2win = player2win + 1
                player1lose = player1lose + 1
            else:
                player1win = player1win + 1
                player2lose = player2lose + 1

    return render(request,'pvpinfo.html',{
        'p1w' : player1win,
        'p1l' : player1lose,
        'p2w' : player2win,
        'p2l' : player2lose,
        'p1' : player1,
        'p2' : player2,
    })

