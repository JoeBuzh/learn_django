import random
from django.shortcuts import render, HttpResponse

from app_book import models


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


def add_wuj(request):
    book_list = ['格局','态度','浪潮之颠','数学之美','平凡生活','见识']
    for x in book_list:
        book = models.Book.objects.create(
            title=x,
            price=random.randint(66, 88),
            publish=u'吴军',
            pub_date='2019-12-11'
        )
        book.save()
    
    return HttpResponse("<p>Add Dro.Wu 's Publications Success!</p>")


def get_wuj(request):
    books = models.Book.objects.filter(publish='吴军')
    for b in books:
        print(b.title)

    return HttpResponse("<p>Get Wuj's Publication Done.</p>")


def get_all(request):
    books = models.Book.objects.all()
    for book in books:
        print(book.title)
        print(book.publish)

    thisYear = models.Book.objects.filter(pub_date__year=2020).values_list()
    print('this year: {}'.format(thisYear))

    target = models.Book.objects.filter(title='Fortune')  # [0] == .first, [-1] == .last
    return HttpResponse("<p>all books: {}</p>".format(target[0].publish))