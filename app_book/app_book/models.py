# -*- encoding: utf-8 -*-
'''
@Filename    : models.py
@Datetime    : 2020/07/20 16:56:23
@Author      : Joe-Bu
@version     : 1.0
'''

from django.db import models


class Book(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)
    pub_date = models.DateField(default='2018-5-22')
    author = models.ManyToManyField("Author")


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    gender_choice = (
        (0, 'male'),
        (1, 'female'),
        (2, 'secret'),
    )
    gender = models.SmallIntegerField(choice=gender_choice)
    tel = models.CharField(max_lenght=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()
    
