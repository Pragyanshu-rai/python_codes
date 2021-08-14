from django.contrib import admin
from django.urls import path, re_path
from . import views
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('', views.err, name="api"),
    # path('student-api-get-token/', obtain_auth_token),
    path('student-api-get-token/', TokenObtainPairView.as_view(), name="get-token"),
    path('student-api-refresh-token/', TokenRefreshView.as_view(), name="refresh-token"),
    path('student-api-verify-token/', TokenVerifyView.as_view(), name="verify-token"),
    path('student-api/', views.student_api.as_view(), name="s_api"),
    path('course-api/', views.course_api.as_view(), name="c_api"),
    path('student-api-signup/', views.student_create, name="api-signup"),
]

# urlpatterns += [
#  re_path(r'(?P<path>.*)', views.err, name="Err_404")
# ]