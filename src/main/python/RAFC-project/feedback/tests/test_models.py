from django.test import TestCase
from feedback.models import Faculty,Course,Student,Takes,Teaches,Feedback,Attendance

class TestModels(TestCase):

    def setUp(self):
        self.course1 = Course.objects.create(course_id=900,title='course1',dept='cse')
        self.faculty1 = Faculty.objects.create(f_id=160,name="testf",email="test@gmail.com",dept='cse',password="test")
        self.student1 = Student.objects.create(roll_no=160000,name="tests",email="test@gmail.com",dept='cse',password="test")

    def test_course_content(self):
        self.assertEqual(self.course1.title,'course1')

    def test_student_content(self):
        self.assertEqual(self.student1.name,'tests')

    def test_faculty_content(self):
        self.assertEqual(self.faculty1.name,'testf')


    def test_takes_content(self):
        takes1 = Takes.objects.create(roll_no = self.student1,course_id=self.course1,semester=6,flag=True)
        self.assertEqual(takes1.roll_no.roll_no,160000)
        self.assertEqual(takes1.course_id.course_id,900)

    def test_teaches_content(self):
        teaches1 = Teaches.objects.create(f_id = self.faculty1,course_id=self.course1,semester=6)
        self.assertEqual(teaches1.f_id.f_id,160)
        self.assertEqual(teaches1.course_id.course_id,900)

    def test_attendance_content(self):
        attendance1 = Attendance.objects.create(roll_no = self.student1,course_id=self.course1,P_A='present')
        self.assertEqual(attendance1.roll_no.roll_no,160000)
        self.assertEqual(attendance1.course_id.course_id,900)
        self.assertEqual(attendance1.P_A,"present")
