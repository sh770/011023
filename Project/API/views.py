from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import ToDoList
from . serializers import ToDoListSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/received-messages/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of received messages'
        },
        {
            'Endpoint': '/add-message/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new message with data sent in post request'
        },
        {
            'Endpoint': '/delete-message/id/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting message'
        },
    ]    

    return Response(routes)

@api_view(['GET'])
def getAllList(request):
    list = ToDoList.objects.all()
    serializer = ToDoListSerializer(list,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postTodo(request):
    user = request.user
    todo = request.data['todo']
    addtodo = ToDoList.objects.create(user = user, todo = todo)
    serializer = ToDoListSerializer(addtodo)
    return Response(serializer.data)


@api_view(['GET'])
def getOneTodo(request, id):
    onetodo = ToDoList.objects.get(id = id)
    serializer = ToDoListSerializer(onetodo)
    return Response(serializer.data)



@api_view(['PUT'])
def putTodo(request, id):
    edittodo = ToDoList.objects.get(id = id)
    serializer = ToDoListSerializer(edittodo , data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delTodo(request,id):
    ToDoList.objects.get(id = id).delete()
    return Response("delete on todo")