from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def hello(request):
    return HttpResponse('Hello WOrld.')


def hiwe(request):
    content = {}
    content['bzh'] = 'Hello BZH!!!'
    content['ty'] = 'Hello TY!!!'
    return render(request, 'bzh.html', content)


def hicourse(request):
    list0 = ['Python', 'Mysql', 'Shell']
    skill_dict = {
        'level0': 'str',
        'level1': 'list',
        'level2': 'class'
    }
    now = datetime.now()
    name = 12
    link_str = r"<a href='https://www.runoob.com/'>Click</a>"
    return render(
        request, 
        'demo1.html', 
        {"course_list": list0, "skill": skill_dict, "time": now, "link": link_str, "name": name})


def case0(request):
    return render(request, 'case0.html')