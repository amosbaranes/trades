from django.shortcuts import render, redirect, get_object_or_404
from redis import Redis
from .models import Item, TeamMembers

try:
    redis = Redis(host='redis', port=6379)
except Exception:
    pass


def member(request, pk):
    member_ = TeamMembers.objects.filter(id=pk)[0]
    return render(request, 'todo/member.html', {'member': member_})


def index(request):
    print('-'*50)
    print('-'*50)
    print(request.method)
    print('-'*50)
    print('-'*50)
    if request.method == 'POST':
        text_ = request.POST['item_text']
        print('='*50)
        print(text_)
        print('='*50)
        Item.objects.create(text=text_)

    items = Item.objects.all()
    return render(request, 'todo/index.html', {'items': items})


def draw(request):
    return render(request, 'todo/draw.html', {})

