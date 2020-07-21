# -*- encoding: utf-8 -*-
'''
@Filename    : search.py
@Datetime    : 2020/07/17 17:14:05
@Author      : Joe-Bu
@version     : 1.0
'''

from django.http import HttpResponse
from django.shortcuts import render    # version2.0


# form
def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = 'You want this ... {}'.format(request.GET['q'])
    else:
        message = 'Blank form'

    return HttpResponse(message)
