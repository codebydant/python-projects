from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
import datetime

"""
First view233
"""


def saludo(request):
    """testing intro message"""
    return HttpResponse("Hello World with Django")


def despedida(request):
    """testing output message"""
    return HttpResponse("Good by with Django")


def get_date(request):
    """testing dynamic message"""
    date_ = datetime.datetime.now()
    document_ = """<html>
    <body>
    <h1>
    date: {}
    </h1>
    </body>
    </html>
    """.format(date_)
    return HttpResponse(document_)


def calculate_futAge(request, age_, year_):
    """testing url parameters"""
    # current_age = 27
    period_ = year_ - datetime.datetime.now().year
    future_age = age_ + period_
    document_ = """<html>
    <body>
    <h1>
    In the year {} you will be {} years old!
    </h1>
    </body>
    </html>
    """.format(year_, future_age)

    return HttpResponse(document_)


def get_template(request):
    """testing template from external document"""
    doc_ext = open("C:\\Users\\Daniel\\Desktop\\ProyectosDjango\\Proyecto1\\Proyecto1\\templates\\template1.html")
    template_ = Template(doc_ext.read())
    doc_ext.close()

    name_ = "Daniel"
    year_ = datetime.datetime.now().year
    ctx_ = Context({'name': name_, 'date': year_, 'topics': ['topic 1', 'topic 2', 'topic 3', 'topic 4', 'topic 5']})
    document_ = template_.render(ctx_)
    return HttpResponse(document_)


def get_template_loader(request):
    """testing template loader from external document"""
    doc_ext = loader.get_template("template1.html")

    year_ = datetime.datetime.now().year
    document_ = doc_ext.render({'name': "Daniel", 'date': year_, 'topics': ['topic 1', 'topic 2', 'topic 3', 'topic 4', 'topic 5']})
    return HttpResponse(document_)


def get_template_shorcuts(request):
    year_ = datetime.datetime.now().year
    ctx_ = {'name': "Daniel", 'date': year_, 'topics': ['topic 1', 'topic 2', 'topic 3', 'topic 4', 'topic 5']}
    return render(request, "template1.html", ctx_)


def get_template_padre(request):
    return render(request, "base.html")


def get_template_child(request):
    return render(request, "child.html")
