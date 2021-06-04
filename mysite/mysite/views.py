from re import L
from mysite import serialize
from mysite.models import EmployeeModel
from mysite.serialize import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
class EmployeeTable(APIView):
    def get(self,request):
        empobj=EmployeeModel.objects.all()
        empserializeobj=EmployeeSerializer(empobj,many=True)
        return Response(empserializeobj.data)
    def post(self,request):
        serializeobj=EmployeeSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)

class EmployeeUpdate(APIView):
    def post(self,request,pk):
        try:
            empobj=EmployeeModel.objects.get(pk=pk)
        except:
            return Response("NOt Found")
        empserialize=EmployeeSerializer(empobj,data=request.data)
        if empserialize.is_valid():
            empserialize.save()
            return Response(empserialize.data)
        return Response(empserialize.errors) 

class EmployeeDelete(APIView):
    def get(self,request,pk):
        try:
            empobj=EmployeeModel.objects.get(pk=pk)
        except:
            return Response("NOt Found")
        empobj.delete()
        return Response(200)        