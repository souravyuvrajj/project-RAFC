from django.shortcuts import render,redirect
from .models import Faculty,Course,Student,Takes,Teaches,Feedback,Attendance
from django.views.decorators.http import require_POST
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.db.models import Avg
from django.http import JsonResponse
import csv

def login(request):
    if(request.user.username =='admin'):
        return redirect('adminpage')
    elif(request.user.username and Student.objects.filter(roll_no =request.user.username).exists()):
        return redirect('studentpage')
    elif(request.user.username and Faculty.objects.filter(f_id =request.user.username).exists()):
        return redirect('facultypage')
    elif request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        if(username=='admin'):
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('adminpage')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
        elif(Student.objects.filter(roll_no=username,password=password).exists()):
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('studentpage')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
        elif(Faculty.objects.filter(f_id=username,password=password).exists()):
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('facultypage')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def adminpage(request):
    if(request.user.username =='admin'):
        student_count = Student.objects.all().count()
        faculty_count = Faculty.objects.all().count()
        total_feedback = Takes.objects.all().count()
        feedback_given = Feedback.objects.all().count()
        if (total_feedback!=0):
            percent_given = int((feedback_given/total_feedback)*100)
        else:
            percent_given = False
        pending_feedback = total_feedback-feedback_given

        label =[]
        data = []
        faculty = Faculty.objects.all()
        for fac in faculty:
            if(Feedback.objects.filter(f_id=fac).exists()):
                label.append(fac.name)
                data.append(int(Feedback.objects.filter(f_id=fac).aggregate(Avg('average'))['average__avg']*10))
        context = {
            'student_count':student_count,
            'faculty_count':faculty_count,
            'percent_given':percent_given,
            'pending_feedback':pending_feedback,
            'label':label,
            'data':data,
        }
        return render(request,'admin/admin.html',context)
    else:
        return redirect('login')

def feedback_report(request,course_id = 'none'):
    if(request.user.username and Faculty.objects.filter(f_id =request.user.username).exists()):
        title = Course.objects.filter(course_id=course_id)[0].title
        fac = Faculty.objects.get(pk=request.user.username)
        course =Course.objects.get(pk=course_id)
        feedback = Feedback.objects.filter(f_id=fac,course_id=course)
        data = []
        data.append(int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('q1'))['q1__avg']*10))
        data.append(int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('q2'))['q2__avg']*10))
        data.append(int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('q3'))['q3__avg']*10))
        data.append(int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('q4'))['q4__avg']*10))
        data.append(int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('q5'))['q5__avg']*10))
        data.append(int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('q6'))['q6__avg']*10))
        data.append(int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('q7'))['q7__avg']*10))
        data.append(int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('q8'))['q8__avg']*10))
        data.append(int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('q9'))['q9__avg']*10))
        data.append(int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('q10'))['q10__avg']*10))
        data.append(int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('q11'))['q11__avg']*10))
        data.append(int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('q12'))['q12__avg']*10))
        data.append(int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('q13'))['q13__avg']*10))
        data.append(int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('q14'))['q14__avg']*10))
        data.append(int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('q15'))['q15__avg']*10))
        context = {
            'title':title,
            'data':data,
        }
        return render(request,'faculty/feedback_report.html',context)
    else:
        return redirect('login')

def studentpage(request):
    if(request.user.username and Student.objects.filter(roll_no =request.user.username).exists()):
        takes = Takes.objects.filter(roll_no=request.user.username)
        feedback = Takes.objects.filter(roll_no=request.user.username,flag = False)
        context = {
            'takes':takes,
            'feedback':feedback,
        }
        return render(request,'student/student.html',context)
    else:
        return redirect('login')

def facultypage(request):
    if(request.user.username and Faculty.objects.filter(f_id =request.user.username).exists()):
        fac = Faculty.objects.get(pk=request.user.username)
        teaches = Teaches.objects.filter(f_id =fac)
        avg_per_course ={}
        feedback_given = {}
        for t in teaches:
            if(Feedback.objects.filter(course_id=t.course_id).exists()):
                course_id =t.course_id.course_id
                course = Course.objects.get(pk = course_id)
                avg_per_course[Course.objects.get(pk = course_id)] = int(Feedback.objects.filter(f_id=fac,course_id=course).aggregate(Avg('average'))['average__avg']*10)
        context = {
            'avg_per_course':avg_per_course
        }
        return render(request,'faculty/faculty.html',context)
    else:
        return redirect('login')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')

def give_feedback(request,course_id='none'):
    if(request.user.username and Student.objects.filter(roll_no =request.user.username).exists()):
        if request.method == 'POST':
            if 'o1' in request.POST:
                o1 = request.POST['o1']
            if 'o2' in request.POST:
                o2 = request.POST['o2']
            if 'o3' in request.POST:
                o3 = request.POST['o3']
            if 'o4' in request.POST:
                o4 = request.POST['o4']
            if 'o5' in request.POST:
                o5 = request.POST['o5']
            if 'o6' in request.POST:
                o6 = request.POST['o6']
            if 'o7' in request.POST:
                o7 = request.POST['o7']
            if 'o8' in request.POST:
                o8 = request.POST['o8']
            if 'o9' in request.POST:
                o9 = request.POST['o9']
            if 'o10' in request.POST:
                o10 = request.POST['o10']
            if 'o11' in request.POST:
                o11 = request.POST['o11']
            if 'o12' in request.POST:
                o12 = request.POST['o12']
            if 'o13' in request.POST:
                o13 = request.POST['o13']
            if 'o14' in request.POST:
                o14 = request.POST['o14']
            if 'o15' in request.POST:
                o15 = request.POST['o15']
            if 'comment' in request.POST:
                comment = request.POST['comment']
            fid = Teaches.objects.filter(course_id=course_id)[0].f_id.f_id
            avg = (int(o1)+int(o2)+int(o3)+int(o4)+int(o5)+int(o6)+int(o7)+int(o8)+int(o9)+int(o10)+int(o11)+int(o12)+int(o13)+int(o14)+int(o15))/15
            fac = Faculty.objects.get(pk=fid)
            course =Course.objects.get(pk=course_id)
            feedback = Feedback(f_id=fac,course_id=course,q1=o1,q2=o2,q3=o3,q4=o4,q5=o5,q6=o6,q7=o7,q8=o8,q9=o9,q10=o10,q11=o11,q12=o12,q13=o13,q14=o14,q15=o15,comment=comment,average = avg)
            feedback.save()
            stud = Student.objects.get(pk=request.user.username)
            course =Course.objects.get(pk=course_id)
            t= Takes.objects.filter(roll_no=stud,course_id=course)[0]
            t.flag = True
            t.save()
            return redirect('studentpage')
        takes = Takes.objects.filter(roll_no=request.user.username)
        feedback = Takes.objects.filter(roll_no=request.user.username,flag = False)
        fac = Teaches.objects.get(course_id = course_id)
        print(fac.f_id.name )
        context={
        'takes':takes,
        'feedback':feedback,
        'course_id':course_id,
        'fac_name':fac.f_id.name,
        }
        return render(request,'student/feedback.html',context)
    else:
        return redirect('login')



def attendance_report(request,course_id = 'none'):
    if(request.user.username and Student.objects.filter(roll_no =request.user.username).exists()):
        takes = Takes.objects.filter(roll_no=request.user.username)
        feedback = Takes.objects.filter(roll_no=request.user.username,flag = False)
        title = Course.objects.filter(course_id=course_id)[0].title
        stud = Student.objects.get(pk = request.user.username)
        course = Course.objects.get(course_id=course_id)
        if (Attendance.objects.filter(course_id = course).exists()):
            total_classes =Attendance.objects.filter(course_id = course).distinct('date').count()
            attended_classes =  Attendance.objects.filter(course_id = course,roll_no = stud,P_A='present').distinct('date').count()
            absent_classes = total_classes-attended_classes
            percentage = int((attended_classes/total_classes)*100)

            context = {
                'takes':takes,
                'feedback':feedback,
                'title':title,
                'total_classes':total_classes,
                'attended_classes':attended_classes,
                'absent_classes':absent_classes,
                'percentage':percentage
            }
        else:
            context = {
                'takes':takes,
                'feedback':feedback,
                'title':title,
            }
        return render(request,'student/student_attendance_report.html',context)
    else:
        return redirect('login')



def addstudent(request):
    if request.method == 'POST':
        if request.FILES:
            file = request.FILES['file']
            decoded_file = file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file,delimiter=',')
            for row in reader:
                roll = row[0]
                name = row[1]
                email = row[2]
                dept = row[3]
                passwd = row[4]
                if User.objects.filter(username=roll).exists():
                    continue
                else:
                    user = User.objects.create_user(username=roll, password=passwd,email=email,first_name=name)
                    user.save()
                    student = Student(roll_no=roll,name=name,email=email,dept=dept,password=passwd)
                    student.save()
        else:
           if 'roll' in request.POST:
               roll = request.POST['roll']
           if 'name' in request.POST:
               name = request.POST['name']
           if 'email' in request.POST:
               email = request.POST['email']
           if 'dept' in request.POST:
               dept = request.POST['dept']
           if 'pass' in request.POST:
               passwd = request.POST['pass']
           if User.objects.filter(username=roll).exists():
               messages.error(request, 'Roll no already exists!!')
               return redirect('addstudent')
           else:
               user = User.objects.create_user(username=roll, password=passwd,email=email,first_name=name)
               user.save()
               student = Student(roll_no=roll,name=name,email=email,dept=dept,password=passwd)
               student.save()
    students = Student.objects.order_by('roll_no')
    context = {
       'students':students
    }
    return render(request,'admin/addstudent.html',context)


def addfaculty(request):
     if request.method == 'POST':
         if request.FILES:
             file = request.FILES['file']
             decoded_file = file.read().decode('utf-8').splitlines()
             reader = csv.reader(decoded_file,delimiter=',')
             for row in reader:
                 fid = row[0]
                 name = row[1]
                 email = row[2]
                 dept = row[3]
                 password = row[4]
                 if User.objects.filter(username=fid).exists():
                     continue
                 else:
                     user = User.objects.create_user(username=fid, password=password,email=email,first_name=name)
                     user.save()
                     faculty = Faculty(f_id=fid,name=name,email=email,password =password,dept=department)
                     faculty.save()
         else:
             if 'name' in request.POST:
                 name = request.POST['name']
             if 'f_id' in request.POST:
                 fid = request.POST['f_id']
             if 'dept' in request.POST:
                 department = request.POST['dept']
             if 'email' in request.POST:
                 email = request.POST['email']
             if 'pass' in request.POST:
                 password = request.POST['pass']
             if User.objects.filter(username=fid).exists():
                 messages.error(request, 'Faculy Id already exists!!')
                 return redirect('addfaculty')
             else:
                 user = User.objects.create_user(username=fid, password=password,email=email,first_name=name)
                 user.save()
                 faculty = Faculty(f_id=fid,name=name,email=email,password =password,dept=department)
                 faculty.save()
     facultys = Faculty.objects.order_by('f_id')
     context = {
         'facultys':facultys
     }
     return render(request,'admin/addfaculty.html',context)

def addcourse(request):
    if request.method == 'POST':
        if request.FILES:
            file = request.FILES['file']
            decoded_file = file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file,delimiter=',')
            for row in reader:
                cid=row[0]
                title = row[1]
                dept = row[2]
                if Course.objects.filter(course_id=cid).exists():
                    continue
                elif Course.objects.filter(title=title).exists():
                    continue
                else:
                    course = Course(course_id=cid,title=title,dept=dept)
                    course.save()
        else:
            if 'title' in request.POST:
                title = request.POST['title']
            if 'c_id' in request.POST:
                cid = request.POST['c_id']
            if 'dept' in request.POST:
                dept = request.POST['dept']
            if Course.objects.filter(course_id=cid).exists():
                messages.error(request, 'Course Id already exists!!')
                return redirect('addcourse')
            elif Course.objects.filter(title=title).exists():
                messages.error(request, 'Title already exists!!')
                return redirect('addcourse')
            else:
                course = Course(course_id=cid,title=title,dept=dept)
                course.save()
    courses = Course.objects.order_by('course_id')
    context = {
        'courses':courses
    }
    return render(request,'admin/addcourse.html',context)


def delfaculty(request,fac_id='none'):
     if fac_id!='none':
         User.objects.get(username = fac_id).delete()
         Faculty.objects.filter(f_id=fac_id).delete()
     facultys = Faculty.objects.order_by('f_id')
     context = {
         'facultys':facultys
     }
     return render(request,'admin/delfaculty.html',context)


def delstudent(request,student_id='none'):
    if student_id!='none':
        User.objects.get(username = student_id).delete()
        Student.objects.filter(pk=student_id).delete()

    students = Student.objects.order_by('roll_no')
    context = {
        'students':students
    }
    return render(request,'admin/delstudent.html',context)


def delcourse(request,course_id='none'):
    if course_id!='none':
        Course.objects.filter(pk=course_id).delete()
    courses = Course.objects.order_by('dept')
    context = {
        'courses':courses
    }
    return render(request,'admin/delcourse.html',context)

def takes(request,student_id='none',course_id='none',sem='none'):
    if student_id!='none' and course_id!='none' and sem!='none':
        Takes.objects.filter(roll_no=student_id,course_id =course_id,semester=sem).delete()
    else:
        if request.method == 'POST':
           if 'sem' in request.POST:
               sem = request.POST['sem']
           if 'c_id' in request.POST:
               cid = request.POST['c_id']
           if 'r_id' in request.POST:
               rid = request.POST['r_id']
           stud = Student.objects.get(pk=rid)
           course =Course.objects.get(pk=cid)
           if Takes.objects.filter(roll_no=stud,course_id=course).exists():
               messages.error(request, 'This Course is already taken by the student!!')
               return redirect('takes')
           else:
               takes = Takes(roll_no=stud,course_id=course,semester=sem)
               takes.save()
    takes = Takes.objects.order_by('roll_no')
    context = {
        'takes':takes
    }
    return render(request,'admin/takes.html',context)

def teaches(request,fac_id='none',course_id='none',sem='none'):
    if fac_id!='none' and course_id!='none' and sem!='none':
        Teaches.objects.filter(f_id=fac_id,course_id =course_id,semester=sem).delete()
    else:
        if request.method == 'POST':
           if 'sem' in request.POST:
               sem = request.POST['sem']
           if 'c_id' in request.POST:
               cid = request.POST['c_id']
           if 'f_id' in request.POST:
               fid = request.POST['f_id']
           fac = Faculty.objects.get(pk=fid)
           course =Course.objects.get(pk=cid)
           if Teaches.objects.filter(f_id=fac,course_id=course).exists():
               messages.error(request, 'This Course is already taught by this faculty!!')
               return redirect('teaches')
           else:
               teaches = Teaches(f_id=fac,course_id=course,semester=sem)
               teaches.save()
    teaches = Teaches.objects.order_by('f_id')
    context = {
        'teaches':teaches
    }
    return render(request,'admin/teaches.html',context)


def take_attendance(request):
    if request.method == 'POST':
        fac = Faculty.objects.get(pk=request.user.username)
        courses = Teaches.objects.filter(f_id=fac)
        studentlist = Takes.objects.filter(course_id=request.POST['course_id']).order_by('roll_no')
        i=0
        pa_list = []
        for student in studentlist:
            index = 'o'+str(i+1)
            if request.POST[index] == "1":
                p_a='present'
            else:
                p_a='absent'
            pa_list.append(p_a)
            stud = Student.objects.get(pk = student.roll_no.roll_no)
            cid = Course.objects.get(pk = request.POST['course_id'])
            if(Attendance.objects.filter(roll_no = stud,course_id=cid,date = request.POST['date']).first()):
                att = Attendance.objects.filter(roll_no = stud,course_id=cid,date = request.POST['date']).first()
                att.P_A = p_a
                att.save()
            else:

                attendance = Attendance(roll_no = stud,course_id=cid,P_A = p_a,date = request.POST['date'])
                attendance.save()
            i=+1

        stud_attend_list = zip(pa_list,studentlist)
        context = {
            'courses':courses,
            'currentid':request.POST['course_id'],
            'studattendlist':stud_attend_list,
            'date':request.POST['course_id']
        }
    else:
        fac = Faculty.objects.get(pk=request.user.username)
        courses = Teaches.objects.filter(f_id=fac)
        context = {
            'courses':courses,
        }
    return render(request,'faculty/take_attendance.html',context)

def take_attendance1(request):
    courseid = request.GET.get('course_id', None)
    date = request.GET.get('date', None)
    course =Course.objects.get(pk=courseid)
    studentlist = Takes.objects.filter(course_id=course).order_by('roll_no')
    studroll = []
    studname = []
    pa_list = []

    for student in studentlist:
        studroll.append(student.roll_no.roll_no)
        studname.append(student.roll_no.name)
        stud = Student.objects.get(pk = student.roll_no.roll_no)
        if(Attendance.objects.filter(roll_no = stud,course_id=course,date = date).exists()):
            pa_list.append(Attendance.objects.get(roll_no = stud,course_id=course,date = date).P_A)

    data={
    'pa_list':pa_list,
    'studentroll':studroll,
    'studentname':studname
    }
    return JsonResponse(data)
