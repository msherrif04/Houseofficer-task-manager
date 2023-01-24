from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, BedSerializer
from .models import Bed, Task

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint':'/beds/',
            'method':'GET',
            'body': None,
            'description': 'Returns an array of beds with tasks'
        },
        {
            'Endpoint':'/beds/id/',
            'method':'GET',
            'body': None,
            'description': 'Returns a single bed with details'
        },
        {
            'Endpoint':'/beds/id/tasks/',
            'method':'GET',
            'body': None,
            'description': 'Returns all tasks for specified bed'
        },
        {
            'Endpoint':'/beds/create/',
            'method':'POST',
            'body':{'number':"",'name':"",'ward':""},
            'description': 'Creates new bed with data sent in post request'
        },
        {
            'Endpoint':'/beds/delete/',
            'method':'DELETE',
            'body':None,
            'description': 'deletes an existing bed '
        },
        {
            'Endpoint':'/beds/update/',
            'method':'PUT',
            'body':{'number':"",'name':"",'ward':""},
            'description': 'Updates an exisiting task with data sent in post request'
        },

        {
            'Endpoint':'/tasks/',
            'method':'GET',
            'body': None,
            'description': 'Returns an array of tasks'
        },
        {
            'Endpoint':'/tasks/completed/',
            'method':'GET',
            'body': None,
            'description': 'Returns an array of completed tasks'
        },
        {
            'Endpoint':'/tasks/pending/',
            'method':'GET',
            'body': None,
            'description': 'Returns an array of incomplete tasks'
        },
        {
            'Endpoint':'/tasks/id/',
            'method':'GET',
            'body': None,
            'description': 'Returns a single task object'
        },
        {
            'Endpoint':'/tasks/create/',
            'method':'POST',
            'body':{'task':"",'complete':"", 'bed':""},
            'description': 'Creates new task with data sent in post request'
        },
        {
            'Endpoint':'/tasks/update/',
            'method':'PUT',
            'body':{'task':"",'complete':"", 'bed':""},
            'description': 'Updates an exisiting task with data sent in post request'
        },
        { 
            'Endpoint':'/tasks/delete/',
            'method':'DELETE',
            'body':None,
            'description': 'Deletes an existing task'}
    ]
    return Response(routes)

@api_view(['GET'])
def getBeds(request):
    beds = Bed.objects.all()
    serializer = BedSerializer(beds, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getBedDetails(request,pk):
    beds = Bed.objects.get(id=pk)
    serializer = BedSerializer(beds, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def getBedTasks(request,pk):
    tasks = Task.objects.filter(bed=pk)
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addBed(request):
    data = request.data

    bed = Bed.objects.create(
        number = data['number'],
        name = data['name'],
        ward = data['ward']
    )
    serializer =  BedSerializer(bed)
    return Response(serializer.data)

@api_view(['PUT'])
def updateBed(request, pk):
    data = request.data
    bed = Bed.objects.get(id=pk)
    
    serializer =  BedSerializer(bed, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteBed(request,pk):
    bed = Bed.objects.get(id=pk)
    bed.delete()
    return Response('Bed removed')








@api_view(['GET'])
def getTasks(request):
    beds = Task.objects.all()
    serializer = TaskSerializer(beds, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getPendingTasks(request):
    beds = Task.objects.filter(complete = False)
    serializer = TaskSerializer(beds, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getCompletedTasks(request):
    beds = Task.objects.filter(complete = True)
    serializer = TaskSerializer(beds, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addTask(request):
    data = request.data

    task = Task.objects.create(
        task = data['task'],
        complete = data['complete'],
        bed = data['bed']
    )
    serializer =  TaskSerializer(task)
    return Response(serializer.data)

@api_view(['PUT'])
def updateTask(request, pk):
    data = request.data
    task = Task.objects.get(id=pk)
    
    serializer =  TaskSerializer(task, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Task removed')