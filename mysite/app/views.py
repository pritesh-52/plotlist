from django.shortcuts import render


def index(request):
    return render(request,"index.html")


def category(request):
    return render(request,"category.html")


def listing(request):
    return  render(request,"listing.html")

def contact(request):
    return render(request,"contact.html")