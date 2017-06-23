# coding=utf-8
from django.shortcuts import render


# Create your views here.
from django.shortcuts import render_to_response

from main.models import *


def index(request):
    args = {
        'slider': Kabar.objects.all()[0:3],
        'news': Kabar.objects.all()[3:5],
        'kabar':Kabar.objects.all()[0:10],
        'protocol':Protocol.objects.all(),
        'atestation':Atestation.objects.all()[0:6],
        'NPA':Npa.objects.all()[0:6]
    }
    return render(request, 'base.html',args)


def news(request):
    args = {
        'slider': Kabar.objects.all()[0:3],

        'first': Kabar.objects.all()[0:2],
        'second':Kabar.objects.all()[2:6],
        'protocol':Protocol.objects.all(),
    }
    return render_to_response('news.html',args)


def article(request, p1):
    args = {
        'protocol':Protocol.objects.all(),
        'article':Kabar.objects.get(id = p1)
    }
    return render_to_response('article.html', args)


def acts(request):
    args = {
        'protocol':Protocol.objects.all(),
        'npa':Npa.objects.all()
    }
    return render_to_response('acts.html',args)


def act(request, p1):
    args = {
        'protocol':Protocol.objects.all(),
        'article':Npa.objects.get(id = p1)
    }
    return render_to_response('act.html',args)


def nmo(request):
    args = {
        'protocol':Protocol.objects.all(),
        'npa':Education.objects.filter(category='НМО')
    }
    return render_to_response('nmo.html', args)


def nmo1(request, p1):
    args = {
        'protocol':Protocol.objects.all(),
        'article':Education.objects.get(id = p1)
    }
    return render_to_response('nmo1.html',args)


def pdmo(request):
    args = {
        'protocol':Protocol.objects.all(),
        'npa':Education.objects.filter(category='ПДМО')
    }
    return render_to_response('pdmo.html', args)


def pdmo1(request, p1):
    args = {
        'protocol':Protocol.objects.all(),
        'article':Education.objects.get(id = p1)
    }
    return render_to_response('pdmo1.html',args)


def attestation(request):
    args = {
        'protocol':Protocol.objects.all(),
        'npa':Atestation.objects.all()
    }
    return render_to_response('attestation.html', args)


def attestation1(request, p1):
    args = {
        'protocol':Protocol.objects.all(),
        'article':Atestation.objects.get(id=p1)
    }
    return render_to_response('attestation1.html',args)


def protocol(request, p1):
    args = {
        'protocol':Protocol.objects.all(),
        'article':Protocol.objects.get(id=p1)
    }
    return render_to_response('protocol.html', args)


def about(request):
    args = {
        'protocol':Protocol.objects.all(),
    }
    return render_to_response('about.html', args)
