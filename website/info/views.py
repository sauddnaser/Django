from django.shortcuts import render

def tea_info(request):
    return render(request, 'info.html')