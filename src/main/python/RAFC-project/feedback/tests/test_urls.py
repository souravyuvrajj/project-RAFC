from django.urls import reverse
from django.utils import timezone
from django.test import TestCase


from django.urls import reverse,resolve
from feedback.views import login,adminpage,studentpage,facultypage,attendance_report,give_feedback,addcourse,addfaculty,addstudent

class TestUrls(TestCase):
    def test_list_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func,login)

    def test_admin_url_is_resolved(self):
        url = reverse('adminpage')
        self.assertEquals(resolve(url).func,adminpage)

    def test_student_url_is_resolved(self):
        url = reverse('studentpage')
        self.assertEquals(resolve(url).func,studentpage)

    def test_faculty_url_is_resolved(self):
        url = reverse('facultypage')
        self.assertEquals(resolve(url).func,facultypage)

    def test_addcourse_url_is_resolved(self):
        url = reverse('addcourse')
        self.assertEquals(resolve(url).func,addcourse)

    def test_addfaculty_url_is_resolved(self):
        url = reverse('addfaculty')
        self.assertEquals(resolve(url).func,addfaculty)

    def test_addstudent_url_is_resolved(self):
        url = reverse('addstudent')
        self.assertEquals(resolve(url).func,addstudent)
