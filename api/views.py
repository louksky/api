from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Messeages_HSerializer

from .models import Messeages_H
# Create your views here.

@api_view(['GET'])
def api_views(request):
	api_routes = {

		'API please login '
		'Write message':'/msg-write/',
		'Get all messages of logged user':'msg-list',
		'Get all unread messages of logged user':'un-msg-list',
		'Read one message':'msg-read/id/',
		'Delete one message':'msg-delete/id/',

		'EXAMPLE : ':{
			
        "id": 6,
        "title": "To Asaf Louk",
        "slug": "",
        "message_content": "Hi asaf",
        "creation_date": "2020-10-22",
        
        "user_sender": 1,
        "user_receiver": 1
    
		}
		}

	return Response(api_routes)


#create/write view
@api_view(['POST'])
def msg_write(request):
	serializer = Messeages_HSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

#list view all messages
@api_view(['GET'])
def msg_List(request):
	msgs = Messeages_H.objects.filter(user_receiver=request.user).order_by('-id')
	serializer = Messeages_HSerializer(msgs, many=True)
	return Response(serializer.data)


#list view all messages unread !! >> unread msgs
@api_view(['GET'])
def msgunread_List(request):
	msgs = Messeages_H.objects.filter(user_receiver=request.user,is_read=False).order_by('-id')
	serializer = Messeages_HSerializer(msgs, many=True)
	return Response(serializer.data)


#Read message set msg.is_read to true
@api_view(['GET'])
def msg_read(request,pk):
	
		
	msg = Messeages_H.objects.get(id=pk)
	serializer = Messeages_HSerializer(msg, many=False)
	msg.is_read = True
	msg.save()
	return Response(serializer.data)

#Delete msg 
@api_view(['DELETE'])
def msg_delete(request, pk):
	msg1 = Messeages_H.objects.filter(id=pk,user_receiver=request.user)
	msg2 = Messeages_H.objects.filter(id=pk,user_sender=request.user)

	if  msg1:
		msg1.delete()
	else:
		if  msg2:
			msg2.delete()
			

	return Response('Message deleted ...')




