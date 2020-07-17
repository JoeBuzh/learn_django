# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

def insertdb(request):
    '''
    Insert
    '''
    names = ['bzh', 'ty', 'bzm', 'bjw', 'lxm', 'tc']
    ages = [28, 27, 25, 59, 54, 20]
    for name, age in zip(names, ages):
        test = Test(name=name, age=age)
        test.save()

    return HttpResponse("<p>添加数据success!</p>")


def querydb(request):
    '''
    Query
    '''
    list_all = Test.objects.all()     # select * from ...
    res = Test.objects.filter(age=27)

    return HttpResponse("<h2>{0}</h2><p>{1}</p>".format(list_all, res))


def updatedb(request):
    '''
    Update
    '''
    person = Test.objects.get(name='bjw')
    person.name = '卜俊文'
    person.save()
    return HttpResponse("<p>修改成功</p>")


def deletedb(request):
    '''
    Delete
    '''
    p = Test.objects.get(name='tc')
    p.delete()
    return HttpResponse("<p>删除田畅??-->OK </p>")
