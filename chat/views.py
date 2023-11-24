from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Message, Room


def index(request):
    return render(request, "chat/index.html")


# def room(request, room):
#     username = request.GET.get('username')
#     room_details = Room.objects.get(name=room)
#     return render(request, 'room.html', {
#         'username': username,
#         'room': room,
#         'room_details': room_details
#     })

# def checkview(request, pk):
#     room = request.POST['room_name']
#     username = request.POST['username']

#     if Room.objects.filter(name=room).exists():
#         return redirect("room")
#     else:
#         new_room = Room.objects.create(name=room)
#         new_room.save()
#         return redirect("room")

# def send(request):
#     message = request.POST['message']
#     username = request.POST['username']
#     room_id = request.POST['room_id']

#     new_message = Message.objects.create(value=message, user=username, room=room_id)
#     new_message.save()
#     return HttpResponse('Message sent successfully')

# def getMessages(request, room):
#     room_details = Cha.objects.get(name=room)

#     messages = Message.objects.filter(room=room_details.id)
#     return JsonResponse({"messages":list(messages.values())})


def rooms(request, profile_id, pk):
    print(pk)
    print(request.user)
    
    print(profile_id)
    return render(request, 'chat/rooms.html')