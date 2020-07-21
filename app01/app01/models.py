# -*- encoding: utf-8 -*-
'''
@Filename    : models.py
@Datetime    : 2020/07/20 16:56:23
@Author      : Joe-Bu
@version     : 1.0
'''

from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.CharField(max_length=32)
    pub_date = models.DateField(default='2020-2-2')