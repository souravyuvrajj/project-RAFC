from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.urls import reverse
from feedback.models import Faculty,Course,Student,Takes,Teaches,Feedback,Attendance
import json
from django.contrib.auth.models import User


class MySeleniumTests(StaticLiveServerTestCase):
    def setUp(self):
        self.browser =webdriver.Chrome('feedback/functional_tests/chromedriver')

    def teardown(self):
        self.browser.close()

    def test_faculty_login(self):
        self.browser.get(self.live_server_url)

        test_faculty = Faculty.objects.create(f_id=101,name="ferdous",email="test@gmail.com",dept='cse',password="ferdous")
        user_faculty = User.objects.create_user(username=101, password="ferdous",email="test@gmail.com",first_name="ferdous")

        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys("101")
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys("ferdous")
        self.browser.find_element_by_name("action").click()
        self.assertTrue(self.browser.current_url, self.live_server_url +"/faculty")


    def test_admin_login(self):
        self.browser.get(self.live_server_url)


        user_admin = User.objects.create_user(username="admin", password="admin",email="test@gmail.com",first_name="admin")

        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys("admin")
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys("admin")
        self.browser.find_element_by_name("action").click()
        self.assertTrue(self.browser.current_url, self.live_server_url +"/admin")

    def test_student_login(self):
        self.browser.get(self.live_server_url)

        test_student = Student.objects.create(roll_no=160000,name="test",email="test@gmail.com",dept='cse',password="test")
        user_student = User.objects.create_user(username=160000, password="test",email="test@gmail.com",first_name="test")

        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys("160000")
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys("test")
        self.browser.find_element_by_name("action").click()
        self.assertTrue(self.browser.current_url, self.live_server_url +"/student")
