from django.shortcuts import render

rooms = [
    {'id':1, 'name':'Let\'s learn greek!'},
    {'id':2, 'name':'Enuma elish in the original'},
    {'id':3, 'name':'Aramaic for beginners!'},
]

def home(request):
    return render(request, 'base/home.html', {'rooms':rooms})

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    return render(request, 'base/room.html', {'room':room})
