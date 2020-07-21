from django.shortcuts import render, HttpResponse

from app01 import models


def add_book1(request):
    book = models.Book(
        title='QI Konws',
        price=99,
        publish='BZH',
        pub_date='2020-7-20'
    )
    book.save()

    return HttpResponse("<p>Method1 数据添加成果</p>")


def add_book2(request):
    book = models.Book.objects.create(
        title='Fortune',
        price=88,
        publish='TY',
        pub_date='2020-7-20'
    )
    book.save()

    return HttpResponse("<p>Method2 数据添加成果</p>")
