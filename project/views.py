from django.shortcuts import HttpResponse


def first_page(request):
    return HttpResponse("Hello world")
