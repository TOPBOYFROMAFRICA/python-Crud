from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='index'),
path('add', views.addStudent, name='addStudent'),
    path('addStudentRec',views.addStudentRec,name='addStudentRec'),
    path('delete_student/<int:id>',views.delete_student,name='delete_student'),
    path('update/<int:id>',views.update,name='update'),
path('updateStudent/<int:id>',views.updateStudent,name='updateStudent'),
]