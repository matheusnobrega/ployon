from django.shortcuts import render
from .models import Room

# rooms = [
#     {'id':1, 'name':'Let\'s learn greek!'},
#     {'id':2, 'name':'Enuma elish in the original'},
#     {'id':3, 'name':'Aramaic for beginners!'},
# ]

def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms':rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    return render(request, 'base/room.html', {'room':room})
