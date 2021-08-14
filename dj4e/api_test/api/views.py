# public libraries
# from functools import partial
from django.shortcuts import redirect
from django.http import JsonResponse
from django.utils.decorators import method_decorator
# from django.views import View
from rest_framework.views import APIView
from io import BytesIO

from django.contrib.auth.models import User
# from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# private libraries
# from api.APIUtils import makeStudent
from .serializers import StudentSerializer
from .models import Course, Student

# instructions to use the api
instructions = "api-endpoint https://127.0.0.1:8000/student-api-signup for user registeration (username, password, gender(m/f), roll, branch, section, year) "


def err(request):
    return JsonResponse({"MSG": instructions}, safe=False)

# for user signup


@csrf_exempt
def student_create(request):

    global instructions

    if request.method == "POST":

        try:
            python_data = JSONParser().parse(BytesIO(request.body))
            print("Data Sent:", python_data, type(python_data))
            ser = StudentSerializer(data=python_data)
            if ser.is_valid():
                ser.save()
                print("saved")
                return JsonResponse(ser.data, safe=False)

            else:
                return JsonResponse(ser.errors, safe=False)

        except Exception as msg:
            print(msg)
            return JsonResponse({"ERR": ser.errors}, safe=False)

    return JsonResponse({"MSG": instructions}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class student_api(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        try:
            # print("User:", request.user)
            python_data = JSONParser().parse(BytesIO(request.body))
            print("Data Recieved:", python_data)

            if "roll" in python_data.keys():

                st = Student.objects.get(roll=python_data["roll"])
                ser = StudentSerializer(st)
                print("student Data:", ser.data)

                return JsonResponse(ser.data, safe=False)

            else:

                st = Student.objects.all()
                ser = StudentSerializer(st, many=True)
                print("students Data:", ser.data)

                return JsonResponse(ser.data, safe=False)

        except Exception as error:

            print("Exception:", error)
            # print("Serializer error messages:", ser.error_messages)
            print("Serializer errors:", ser.errors)

            return JsonResponse({"ERR": ser.errors}, safe=False)

        # return JsonResponse({"MSG":instructions}, safe=False)

    def put_patch(self, request):

        try:
            python_data = JSONParser().parse(BytesIO(request.body))
            print("Data Sent:", python_data, type(python_data))
            user = User.objects.get(
                username=python_data["user"].pop("username"))
            print(python_data)
            st = Student.objects.get(user_id=user.id)
            ser = StudentSerializer(st, data=python_data, partial=True)
            print(ser.initial_data)
            if ser.is_valid():
                ser.save()
                print("Data Saved")
                print("Saved Data:", ser.data)
                return JsonResponse(ser.data, safe=False)

            else:
                # print("Serializer error messages:", ser.error_messages)
                print("Serializer errors:", ser.errors)
                return JsonResponse({"ERR": ser.errors}, safe=False)

        except Exception as error:
            print("Exception:", error)
            # print("Serializer error messages:", ser.error_messages)
            print("Serializer errors:", ser.errors)
            return JsonResponse({"ERR": ser.errors}, safe=False)

        # return JsonResponse({"MSG PUT-PATCH":instructions}, safe=False)

    def put(self, request):
        print("in-put")
        return self.put_patch(request)

    def patch(self, request):
        print("in-patch")
        return self.put_patch(request)


@method_decorator(csrf_exempt, name="dispatch")
class course_api(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        return redirect(request, err)

    def post(self, request):

        try:

            python_data = JSONParser().parse(BytesIO(request.body))
            username = request.user
            user = User.objects.get(username=username)
            student = Student.objects.get(user=user)
            # makes sure that there is no duplicate entry
            if Course.objects.filter(student=student, **python_data).exists():
                return JsonResponse({"ERR": "Duplicate Entry"}, safe=False)

            course = Course.objects.create(student=student, **python_data)
            course.save()
            ser = course.get_dict()
            print("Data Recieved:", python_data)
            print("Data Saved", ser)
            return JsonResponse(ser, safe=False)

        except Exception as error:

            print("Exception:", error)
            return JsonResponse({"ERR": error}, safe=False)

    def put(self, request):

        return JsonResponse({"ERR":"Course Once Assigned Cannot Be Altered"}, safe=False)

    def patch(self, request):

        return JsonResponse({"ERR":"Course Once Assigned Cannot Be Altered"}, safe=False)

    def delete(self, request):

        try:

            python_data = JSONParser().parse(BytesIO(request.body))
            print(python_data)
            username = request.user
            user = User.objects.get(username=username)
            st = Student.objects.get(user=user)
            print(st.__str__())
            try:

                course = Course.objects.get(student_id=st.id, c_code=python_data['c_code'])
                data = course.get_dict()
                print("data deleted", data)
                course.delete()
                return JsonResponse({"MSG":"Data Deleted", "Data":data}, safe=False)
            
            except Exception as ex:
                
                print(ex)
                return JsonResponse({"ERR":"Data Does Not Exist!"}, safe=False)
        
        except Exception as ex:
          
          print(ex)
          return JsonResponse({"ERR":ex}, safe=False)

