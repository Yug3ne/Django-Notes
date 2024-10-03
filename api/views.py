from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import status


from api.models import Note
from api.serializer import NoteSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def notes(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        # serailize the data to come out as json format
        serialzer = NoteSerializer(notes, many=True)
        return Response(serialzer.data)
    
    elif request.method == 'POST':
        # deserialzie the data
        serialzer = NoteSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PATCH', 'DELETE'])    
def singleNote(request, slug):
    try:
        note = Note.objects.get(slug=slug)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serialize = NoteSerializer(note, data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_200_OK )
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    