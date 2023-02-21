from django.shortcuts import render
def wishes(request):
    return render(request,'FirstApp/wishes.html')