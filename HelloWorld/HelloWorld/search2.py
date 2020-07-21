# -*- encoding: utf-8 -*-
'''
@Filename    : search2.py
@Datetime    : 2020/07/17 17:56:40
@Author      : Joe-Bu
@version     : 1.0
'''

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf


def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']

    return render(request, "post.html", ctx)