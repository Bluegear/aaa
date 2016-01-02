from django.shortcuts import render


def index(request):
    context = {'welcome_msg': 'Nice to meet you!'}
    return render(request, 'mcweb/index.html', context)



