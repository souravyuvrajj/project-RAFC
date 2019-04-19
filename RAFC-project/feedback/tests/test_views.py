from django.test import TestCase,Client
from django.urls import reverse
from feedback.models import Faculty,Course,Student,Takes,Teaches,Feedback,Attendance
import json
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render,redirect


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_admin = User.objects.create_user(username="admin", password="test",email="test@gmail.com",first_name="test")
        self.test_student = Student.objects.create(roll_no=160000,name="test",email="test@gmail.com",dept='cse',password="test")
        self.test_student2 = Student.objects.create(roll_no=160002,name="test",email="test@gmail.com",dept='cse',password="test")
        self.user_student = User.objects.create_user(username=160000, password="test",email="test@gmail.com",first_name="test")
        self.test_faculty = Faculty.objects.create(f_id=160,name="test",email="test@gmail.com",dept='cse',password="test")
        self.user_faculty = User.objects.create_user(username=160, password="test",email="test@gmail.com",first_name="test")
        self.test_course = Course.objects.create(course_id="cs120",title="test",dept="cse")
        self.test_course2 = Course.objects.create(course_id="cs122",title="test",dept="cse")
        self.test_takes = Takes.objects.create(roll_no=self.test_student,course_id=self.test_course,semester="1")
        self.test_teaches = Teaches.objects.create(f_id=self.test_faculty,course_id=self.test_course,semester="1")

    def test_project_login_GET(self):
        response = self.client.get(reverse('login'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')

    def test_project_adminpage_GET(self):
        response = self.client.get(reverse('adminpage'))

        self.assertEquals(response.status_code,302)

    def test_project_admin_login_POST(self):
        admin_login = self.client.login(username="admin", password="test")
        self.assertTrue(admin_login)
        response = self.client.post(reverse('login'))

    def test_project_admin_page_POST(self):
        response = self.client.get(reverse('login'),{
        "username":'admin',"password":'admin'
        })
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"login.html")

    def test_project_admin_invalid_page_POST(self):
        response = self.client.get(reverse('login'),{
        "username":'admin',"password":'admin1'
        })
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"login.html")

    def test_project_student_page_POST(self):
        response = self.client.get(reverse('login'),{
            "username":160000,"password":'test'
        })
        self.assertEquals(response.status_code,200)


    def test_project_faculty_page_POST(self):
        response = self.client.get(reverse('login'),{
            "username":160,"password":'test'
        })
        self.assertEquals(response.status_code,200)

    def test_project_login_POST(self):
        user_login = self.client.login(username=160000, password="test")
        self.assertTrue(user_login)
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code,302)

    def test_project_invalid_login_POST(self):
        student_login = self.client.login(username="invalid", password="test")
        self.assertFalse(student_login)
        response = self.client.get(reverse('login'))
        self.assertTrue(response.status_code,302)

    def test_add_student_view(self):
        user_count = User.objects.count()
        student_count = Student.objects.count()
        response = self.client.post(reverse('addstudent'),{
        'roll':"160001",'name':"test",'email':"test@gmail.com",'dept':"cse",'pass':"test"
        })
        self.assertEquals(response.status_code,200)
        self.assertEqual(User.objects.count(), user_count+1)
        self.assertEqual(Student.objects.count(), student_count+1)
        self.assertTemplateUsed(response,"admin/addstudent.html")

    def test_add_existing_student_view(self):
        user_count = User.objects.count()
        student_count = Student.objects.count()
        response = self.client.post(reverse('addstudent'),{
        'roll':"160000",'name':"test",'email':"test@gmail.com",'dept':"cse",'pass':"test"
        })
        self.assertEquals(response.status_code,302)
        self.assertEqual(User.objects.count(), user_count)
        self.assertEqual(Student.objects.count(), student_count)

    def test_add_faculty_view(self):
        user_count = User.objects.count()
        faculty_count = Faculty.objects.count()
        response = self.client.post(reverse('addfaculty'),{
        'f_id':"161",'name':"test",'email':"test@gmail.com",'dept':"cse",'pass':"test"
        })
        self.assertEquals(response.status_code,200)
        self.assertEqual(User.objects.count(), user_count+1)
        self.assertEqual(Faculty.objects.count(), faculty_count+1)
        self.assertTemplateUsed(response,"admin/addfaculty.html")

    def test_add_existing_faculty_view(self):
        user_count = User.objects.count()
        faculty_count = Faculty.objects.count()
        response = self.client.post(reverse('addfaculty'),{
        'f_id':"160",'name':"test",'email':"test@gmail.com",'dept':"cse",'pass':"test"
        })
        self.assertEquals(response.status_code,302)
        self.assertEqual(User.objects.count(), user_count)
        self.assertEqual(Faculty.objects.count(), faculty_count)

    def test_add_course_view(self):
        course_count = Course.objects.count()
        response = self.client.post(reverse('addcourse'),{
        'c_id':"cs121",'title':"test1",'dept':"cse"
        })
        self.assertEquals(response.status_code,200)
        self.assertEqual(Course.objects.count(), course_count+1)
        self.assertTemplateUsed(response,"admin/addcourse.html")

    def test_add_existing_course_view(self):
        course_count = Course.objects.count()
        response = self.client.post(reverse('addcourse'),{
        'c_id':"cs121",'title':"test",'dept':"cse"
        })
        self.assertEquals(response.status_code,302)
        self.assertEqual(Course.objects.count(), course_count)

    def test_add_existing_course_view1(self):
        course_count = Course.objects.count()
        response = self.client.post(reverse('addcourse'),{
        'c_id':"cs120",'title':"test1",'dept':"cse"
        })
        self.assertEquals(response.status_code,302)
        self.assertEqual(Course.objects.count(), course_count)

    def delete_faculty(self):
        faculty_count = Faculty.objects.count()
        response = self.client.get(reverse('delfaculty',args=[160]))
        self.assertEqual(Faculty.objects.count(), faculty_count-1)

    def delete_student(self):
        student_count = Studnet.objects.count()
        response = self.client.get(reverse('delstudent',args=[160000]))
        self.assertEqual(Student.objects.count(), student_count-1)

    def delete_course(self):
        course_count = Course.objects.count()
        response = self.client.get(reverse('delcourse',args=['cs120']))
        self.assertEqual(Course.objects.count(), course_count-1)

    def test_add_takes_view(self):
        takes_count = Takes.objects.count()
        response = self.client.post(reverse('takes'),{
        'c_id':"cs122",'r_id':160002,'sem':1
        })
        self.assertEquals(response.status_code,200)
        self.assertEqual(Takes.objects.count(), takes_count+1)
        self.assertTemplateUsed(response,"admin/takes.html")

    def delete_takes(self):
        takes_count = Takes.objects.count()
        response = self.client.get(reverse('takesdlt',args=[160002,'cs122',1]))
        self.assertEqual(Takes.objects.count(), takes_count-1)

    def test_add_teaches_view(self):
        teaches_count = Teaches.objects.count()
        response = self.client.post(reverse('teaches'),{
        'c_id':"cs122",'f_id':160,'sem':1
        })
        self.assertEquals(response.status_code,200)
        self.assertEqual(Teaches.objects.count(), teaches_count+1)
        self.assertTemplateUsed(response,"admin/teaches.html")

    def delete_teaches(self):
        teaches_count = Teaches.objects.count()
        response = self.client.get(reverse('teachesdlt',args=[160,'cs120',1]))
        self.assertEqual(Teaches.objects.count(), teaches_count-1)
