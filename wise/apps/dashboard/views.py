from django.shortcuts import render

def index(request):
    return render(request, "pages/home.html")

def about(request):
    return render(request, "pages/about.html")

def transactions_view(request):
    return render(request, "pages/transactions.html")
