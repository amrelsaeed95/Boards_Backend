from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse
from django.db.models import Count  
from rest_framework.views import APIView 
from .serializers import BoardSerializer, TopicSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework import status  
from rest_framework import generics
from rest_framework import viewsets 



class BoardViewset(viewsets.ModelViewSet):
	queryset = Board.objects.all()  
	serializer_class = BoardSerializer 








# PURE DJANGO
# def boards_list(request):
# 	boards = Board.objects.all()
# 	data = {'Results': list(boards.values("pk","name","description"))}
# 	return JsonResponse(data)




# class BoardList(generics.ListCreateAPIView):
# 	queryset = Board.objects.all()
# 	serializer_class = BoardSerializer






# REST CBV
# class BoardList(APIView):
# 	def get(self,request):
# 		boards = Board.objects.all()
# 		data = BoardSerializer(boards, many=True).data
# 		return Response(data)

# 	def post(self,request):
# 		serializer = BoardSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class BoardTopics(generics.ListCreateAPIView):
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer  









# REST CBV
# class BoardTopics(APIView):
# 	def get(self, request, board_id):
# 		board = get_object_or_404(Board, pk=board_id)
# 		topics = board.topics.order_by('-created_dt').annotate(comments=Count('posts'))
# 		data = TopicSerializer(topics,many=True).data
# 		return Response(data)

# 	def post(self,request,board_id):
# 		serializer = TopicSerializer(data=request.data)
# 		topic_details = request.data
# 		if serializer.is_valid():
# 			topic = serializer.save()
# 			post_serializer = PostSerializer(data={
# 				"message": topic_details["message"],
# 				"topic":topic.pk,
# 				"created_by":topic.created_by,
# 				"created_dt":topic.created_dt,
# 				"updated_by":topic.updated_by,
# 				"updated_dt":topic.updated_dt
# 				})
# 			if post_serializer.is_valid():
# 				post_serializer.save()
# 			else:
# 				print("post not valid")
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class BoardDetails(APIView):
# 	def get(self, request, board_id):
# 		board = get_object_or_404(Board,pk=board_id)
# 		data = BoardSerializer(board).data  
# 		return Response(data)




# class BoardDetails(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Board.objects.all()
# 	serializer_class = BoardSerializer
# 	lookup_field = 'id'




# PURE DJANGO
# def board_topics(request, board_id):
# 	board = get_object_or_404(Board,pk=board_id)
# 	topics = board.topics.order_by('-created_dt').annotate(comments=Count('posts'))

# 	data = {'results': {
# 	    'name': board.name,
# 	    'description': board.description
# 	},'topics': list(topics.values('pk','subject','board','created_by','created_dt'))
# 	}
# 	return JsonResponse(data)



