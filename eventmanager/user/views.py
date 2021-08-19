from django.shortcuts import render

def mainPageView(request):
    return render(request,"mainpage.html")

def loginView(request):
    return render(request,'login.html')
