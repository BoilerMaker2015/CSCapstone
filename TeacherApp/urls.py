from django.conf.urls import url
from . import views
app_name = "TeacherApp"
urlpatterns = [
    url(r'^teacher/index', views.index, name = "index" ),  # define the homepage for teacherapp
    url(r'^teacherForm/', views.getTeacherForm, name = 'TeacherForm'),   # show the Teacher form to fill out the information for creating a teacher.
    url(r'^submitTeacher/', views.submitTeacher, name = 'submitTeacher'),  # after hitting the submit button on teacher form
    url(r'^teacher/teachClass', views.teachClass, name = 'teachClass'), 
    url(r'^class/student/(?P<classId>\d+)/remove/(?P<studentId>\d+)', views.removeStudent, name = 'removeStudent'),
    url(r'^class/student/(?P<classId>\d+)/add/', views.addStudent, name = 'addStudent'), 
    url(r'^class/add/', views.addClass, name = 'addClass'), 
    url(r'^class/', views.viewStudents, name = 'viewStudents'), 
 
] 