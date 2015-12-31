from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'welcome_msg': 'Nice to meet you!'}
    return render(request, 'web/index.html', context)