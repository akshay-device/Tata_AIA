from .models import tata_rec
from .serializers import tataRecSer
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST', 'DELETE'])
def rec_list(request):
    if request.method == 'GET':
        data = tata_rec.objects.all()
        Form = request.query_params.get('Form', None)
        Method = request.query_params.get('Method', None)
        if Form is not None:
            data = data.filter(Form__icontains=Form)
        elif Method is not None:
            data = data.filter(Method__icontains=Method)
        data_serializer = tataRecSer(data, many=True)
        return JsonResponse(data_serializer.data, safe=False)

    elif request.method == 'POST':
        print(request.body)
        valid_data = request.data
        rec_serializer = tataRecSer(data=valid_data)
        if rec_serializer.is_valid():
            rec_serializer.save()
            return JsonResponse(rec_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(rec_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

