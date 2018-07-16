# -*- coding: utf-8 -*-

from django.http import HttpResponse
def submit1(request):
    return


from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

