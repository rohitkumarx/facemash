import random
import math
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from .models import *

def play(request):
    language = 'en'
    session_language = 'en'
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    try:
        contestants = FaceMash.objects.all()
        contestant_1 = random.choice(contestants)
        contestant_2 = random.choice(contestants)
        while contestant_1 == contestant_2:
            contestant_2 = random.choice(contestants)
        args = {'contestant_1': contestant_1, 'contestant_2' :  contestant_2, 'language':language}
    except IndexError:
        error = True
        args = {'error': error}
    return render(request, 'facemash.html', args)

def increment(request, winner_id, losser_id):
    win = FaceMash.objects.get(pk=winner_id)
    losse = FaceMash.objects.get(pk=losser_id)

    w = win.ratings
    l = losse.ratings
    
    qw = 10**(w/100)
    ql = 10**(l/100)

    ew = qw / (qw + ql)
    el = ql / (qw + ql)

    sw = 1
    sl = 0

    k = 32

    w_new = w + k * (sw - ew)
    l_new = l + k * (sl - el)

    win.ratings = "%.2f" % w_new
    losse.ratings = "%.2f" %l_new

    win.save()
    losse.save()

    return HttpResponseRedirect('/')

def language(request, language='en'):

    response = HttpResponse("Setting language to {}".format(language))

    response.set_cookie('lang', language)

    return response

