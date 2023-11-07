from django.shortcuts import render, redirect
from .common import validations as vl, commit
from .models import *


def login_page(request):
    equal_login = True
    if request.method == 'POST':
        login_data = CountUser.objects.filter(login=request.POST['login'])
        if not login_data:
            equal_login = False
        if not request.POST['password'] or not request.POST['login']:
            equal_login = True
        if request.POST['password'] and request.POST['login'] and equal_login:
            return redirect(reverse('main_page'), permanent=True)
    return render(request, 'meeter/index_login.html', {'title': 'Login', 'equal_login': equal_login})


def register_page(request):
    valid, check = True, False
    if request.method == 'POST':
        qwery_data = request.POST
        valid = vl.valid_register(qwery_data)
        if valid:
            check = True
        if check:
            commit.commit_login(qwery_data)
            return redirect(reverse('login_page'), permanent=True)
    return render(request, 'meeter/index_register.html', {'title': 'Register', 'valid': valid})


def main_page(request):
    data = StatusUser.objects.all().order_by('-pk')
    return render(request, 'meeter/index_main.html', {'title': 'Main', 'data': data})


def about_page(request, user_slug):
    data = StatusUser.objects.get(slug=user_slug)
    return render(request, 'meeter/index_about.html', {'title': 'About', 'data': data})


def create_page(request):
    valid = True
    if request.method == 'POST':
        qwery_data = request.POST
        commit.commit_profile(qwery_data)
        return redirect(reverse('main_page'), permanent=True)
    return render(request, 'meeter/index_create.html', {'title': 'Create'})
