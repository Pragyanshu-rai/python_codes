from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from student.models import Student
from student.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.models import User, auth
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
# Create your views here.

def none(request):
    
    return HttpResponse("None Page")

@csrf_exempt
def student_create(request):
    
    if request.method == "POST":
        json_data = request.body
        print("request body-", request.body)
        my_data_stream = BytesIO(json_data)
        print("Data Stream-", my_data_stream)
        python_data = JSONParser().parse(my_data_stream)
        print("Python Data-", python_data)
        serialized = StudentSerializer(data=python_data)
        if serialized.is_valid():
            serialized.save()
            res = {'msg':"Data saved"}
            print(res['msg'])
            res = JSONRenderer().render(res)
            return HttpResponse(res, content_type="application/json")
        print("serialize.errors-", serialized.errors)
        return JsonResponse(serialized.errors, safe=False)
    
    return redirect('none')

def student_detail(request, pk):
    
    st = Student.objects.get(id=pk)
    serialized = StudentSerializer(st)
    print(serialized.data)
    #json_data = JSONRenderer().render(serialized.data)
    #return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(serialized.data)

def students(request):
    
    st = Student.objects.all()
    serialized = StudentSerializer(st, many=True)
    print(serialized.data)
    json_data = JSONRenderer().render(serialized.data)
    return HttpResponse(json_data, content_type="application/json")
    #return JsonResponse(serialized.data, safe=False)

# class based studentapi view
@method_decorator(csrf_exempt, name="dispatch")
class StudentAPI(View):
    
    def get(self, request):
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id", None)
        print("id-", id)
        if id != None:
            st = Student.objects.get(id=id)
            ser = StudentSerializer(st)
            print(ser.data)
            return JsonResponse(ser.data, safe=False)
        st = Student.objects.all()
        ser = StudentSerializer(st, many=True)
        print(ser.data)
        return JsonResponse(ser.data, safe=False)
    
    def post(self, request):
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        print("python_data:",python_data)
        ser = StudentSerializer(data = python_data)
        if ser.is_valid():
            ser.save()
            res = {"msg":"Data Saved!"}
            print("res:", res)
            return JsonResponse(res, safe=False)
        return JsonResponse(res, safe=False)
    
    def put(self, request):
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        print("python_data:",python_data)
        st = Student.objects.get(id=python_data["id"])
        ser = StudentSerializer(st, data=python_data)
        if ser.is_valid():
            ser.save()
            res = {"msg":"Data Updated!"}
            return JsonResponse(res, safe=False)
        return JsonResponse(ser.errors, safe=False)
    
    def patch(self, request):
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        print("python_data:",python_data)
        st = Student.objects.get(id=python_data["id"])
        ser = StudentSerializer(st, data=python_data, partial=True)
        if ser.is_valid():
            ser.save()
            res = {"msg":"Partial Data Updated!"}
            return JsonResponse(res, safe=False)
        return JsonResponse(ser.errors, safe=False)
    
    def delete(self, request):
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        print("python_data:",python_data)
        st = Student.objects.get(id=python_data["id"])
        st.delete()
        res = {"msg":"Data Deleted!"}
        return JsonResponse(res, safe=False)

@method_decorator(csrf_exempt, name="dispatch")
class apisignup(View):
    
    def post(self, request):
        
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        print(python_data)
        
        if User.objects.filter(username=python_data['username']).exists():
            res = {"msg":"User Exists!"}
            return JsonResponse(res, safe=False)
        
        user = User.objects.create_user(username = python_data['username'], password = python_data['password'])
        user.save()
        res = {"msg":"User Registered!"}
        return JsonResponse(res, safe=False)
    
@method_decorator(csrf_exempt, name="dispatch")
class StudentAPI_Auth(APIView):# view class must inherit from APIView class in order to set authentications
    
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated] # must be authenticated for all operations
    permission_classes = [IsAuthenticatedOrReadOnly] # must be authenticated for all operations but read
    
    def get(self, request):
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id", None)
        print("id-", id)
        if id != None:
            try:
                st = Student.objects.get(id=id)
                ser = StudentSerializer(st)
                print(ser.data)
                return JsonResponse(ser.data, safe=False)
            except:
                return JsonResponse({"msg":"No such Data Exists!"}, safe=False)
        st = Student.objects.all()
        ser = StudentSerializer(st, many=True)
        print(ser.data)
        return JsonResponse(ser.data, safe=False)
    
    def post(self, request):
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        print("python_data:",python_data)
        ser = StudentSerializer(data = python_data)
        if ser.is_valid():
            ser.save()
            res = {"msg":"Data Saved!"}
            print("res:", res)
            return JsonResponse(res, safe=False)
        return JsonResponse(res, safe=False)
    
    def put(self, request):
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        print("python_data:",python_data)
        st = Student.objects.get(id=python_data["id"])
        ser = StudentSerializer(st, data=python_data)
        if ser.is_valid():
            ser.save()
            res = {"msg":"Data Updated!"}
            return JsonResponse(res, safe=False)
        return JsonResponse(ser.errors, safe=False)
    
    def patch(self, request):
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        print("python_data:",python_data)
        st = Student.objects.get(id=python_data["id"])
        ser = StudentSerializer(st, data=python_data, partial=True)
        if ser.is_valid():
            ser.save()
            res = {"msg":"Partial Data Updated!"}
            return JsonResponse(res, safe=False)
        return JsonResponse(ser.errors, safe=False)
    
    def delete(self, request):
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        print("python_data:",python_data)
        try:
            st = Student.objects.get(id=python_data["id"])
            st.delete()
        except:
            res = {"msg":"Data Does Not Exist!"}
            return JsonResponse(res, safe=False)
        res = {"msg":"Data Deleted!"}
        return JsonResponse(res, safe=False)

"""
# method based studentapi View

@csrf_exempt
def studentapi(request):
    
    if request.method == "GET":
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id", None)
        print("id-", id)
        if id != None:
            st = Student.objects.get(id=id)
            ser = StudentSerializer(st)
            print(ser.data)
            return JsonResponse(ser.data, safe=False)
        st = Student.objects.all()
        ser = StudentSerializer(st, many=True)
        print(ser.data)
        return JsonResponse(ser.data, safe=False)
    
    if request.method == "POST":
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        print("python_data:",python_data)
        ser = StudentSerializer(data = python_data)
        if ser.is_valid():
            ser.save()
            res = {"msg":"Data Saved!"}
            print("res:", res)
            return JsonResponse(res, safe=False)
        return JsonResponse(res, safe=False)
    
    if request.method == "PUT":
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        print("python_data:",python_data)
        st = Student.objects.get(id=python_data["id"])
        ser = StudentSerializer(st, data=python_data)
        if ser.is_valid():
            ser.save()
            res = {"msg":"Data Updated!"}
            return JsonResponse(res, safe=False)
        return JsonResponse(ser.errors, safe=False)
    
    if request.method == "PATCH":
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        print("python_data:",python_data)
        st = Student.objects.get(id=python_data["id"])
        ser = StudentSerializer(st, data=python_data, partial=True)
        if ser.is_valid():
            ser.save()
            res = {"msg":"Partial Data Updated!"}
            return JsonResponse(res, safe=False)
        return JsonResponse(ser.errors, safe=False)
    
    if request.method == "DELETE":
        stream = BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        print("python_data:",python_data)
        st = Student.objects.get(id=python_data["id"])
        st.delete()
        res = {"msg":"Data Deleted!"}
        return JsonResponse(res, safe=False)
    
    return redirect('students')
"""
