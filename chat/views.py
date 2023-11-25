from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Message, Room
from profiles.models import Profile
from django.urls import reverse_lazy


def index(request):
    return render(request, "chat/index.html")


def room(request, pk, profile_id):
    print(pk)
    print(profile_id)
    get_profile = Profile.objects.get(id=pk)
    test2 = str(request.user)
    print(test2)
    print(get_profile)
    room = str(get_profile) + test2
    room_details = Room.objects.get(name=room)
    print(room_details)

    context = {
        "profile_id": profile_id,
        "pk": pk,
        "room": room_details.name,
        "username": request.user,
        "room_details": room_details
    }
    return render(request, 'chat/rooms.html', context)


# BUG: When you send a message, send not found error
def send(request):

    if request.method == 'POST':
        message = request.POST['message']
        username = request.user
        room_id = request.POST['room_id']
        
        new_message = Message.objects.create(value=message, user=username, room=room_id)
        new_message.save()
    return HttpResponse('Message sent successfully')

# def getMessages(request, room):
#     room_details = Cha.objects.get(name=room)

#     messages = Message.objects.filter(room=room_details.id)
#     return JsonResponse({"messages":list(messages.values())})


def rooms(request, pk, profile_id):
    get_profile = Profile.objects.get(id=pk)
    
    test2 = str(request.user)
    room = str(get_profile) + test2
    
    if Room.objects.filter(name=room).exists():
       print("room exists")
       return redirect('room', pk=pk, profile_id=profile_id)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        print("room created")

    return redirect('room', pk=pk, profile_id=profile_id)