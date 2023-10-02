from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_edit, name='student_edit'),
    path('student/new/', views.student_new, name='student_new'),
]
