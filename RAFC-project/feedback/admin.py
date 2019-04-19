from django.contrib import admin

# Register your models here.
from .models import Faculty,Course,Student,Takes,Teaches,Feedback,Attendance


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('f_id', 'name', 'email', 'dept', 'password')
    list_display_links = ('f_id', 'name')
    list_filter = ('dept',)
    list_per_page = 25

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'title', 'dept',)
    list_display_links = ('course_id', 'title')
    list_filter = ('dept',)
    list_per_page = 25

class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'email', 'dept', 'password')
    list_display_links = ('roll_no', 'name')
    list_filter = ('dept',)
    list_per_page = 25

class TakesAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'course_id', 'semester','flag')
    list_display_links = ('roll_no', 'course_id')
    list_filter = ('roll_no','course_id','semester')
    list_editable = ('flag',)
    list_per_page = 25

class TeachesAdmin(admin.ModelAdmin):
    list_display = ('f_id', 'course_id', 'semester')
    list_display_links = ('f_id', 'course_id')
    list_filter = ('f_id','course_id','semester')
    list_per_page = 25

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('f_id', 'course_id', 'average')
    list_display_links = ('f_id', 'course_id')
    list_filter = ('f_id','course_id','average')
    list_per_page = 25

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'course_id', 'date','P_A')
    list_display_links = ('roll_no',)
    list_filter = ('roll_no', 'course_id', 'date')
    list_per_page = 25

admin.site.register(Faculty,FacultyAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Takes,TakesAdmin)
admin.site.register(Teaches,TeachesAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Attendance,AttendanceAdmin)
