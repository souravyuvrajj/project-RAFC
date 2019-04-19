from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name ='login'),
    path('admin', views.adminpage,name ='adminpage'),
    path('student', views.studentpage,name ='studentpage'),
    path('faculty', views.facultypage,name ='facultypage'),
    path(r'attendance_report/?<course_id>', views.attendance_report,name ='attendance_report'),
    path(r'feedback_report/?<course_id>', views.feedback_report,name ='feedback_report'),
    path(r'give_feedback/?<course_id>', views.give_feedback,name ='give_feedback'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('addfaculty',views.addfaculty,name='addfaculty'),
    path('addstudent',views.addstudent,name='addstudent'),
    path(r'delstudent/?<student_id>',views.delstudent,name='delstudent'),
    path('delcourse',views.delcourse,name='delcourse'),
    path(r'delcourse/?<course_id>',views.delcourse,name='delcourse'),
    path('delfaculty',views.delfaculty,name='delfaculty'),
    path(r'delfaculty/?<fac_id>',views.delfaculty,name='delfaculty'),
    path('delstudent',views.delstudent,name='delstudent'),
    path(r'takes/?<student_id>?<course_id>?<sem>',views.takes,name='takesdlt'),
    path('takes',views.takes,name='takes'),
    path(r'teaches/?<fac_id>?<course_id>?<sem>',views.teaches,name='teachesdlt'),
    path('teaches',views.teaches,name='teaches'),
    path('logout',views.logout,name='logout'),
    path('take_attendance',views.take_attendance,name='take_attendance'),
    path(r'take_attendance1/',views.take_attendance1,name='take_attendance1'),
]
