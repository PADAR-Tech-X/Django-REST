from rest_framework.response import Response
from rest_framework.decorators import api_view
from reg.models import Students
from .serializers import StudentsSerializer

@api_view(['GET'])
def getData(request):
    students = Students.objects.all()
    serializer = StudentsSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = StudentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)