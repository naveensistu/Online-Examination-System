from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from exam import models as QMODEL
from teacher import models as TMODEL
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import CapturedImage
import sys

#for showing signup/login button for student
code_list=["hello world"]

def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'student/studentclick.html')

def student_signup_view(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    return render(request,'student/studentsignup.html',context=mydict)

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_dashboard_view(request):
    dict={
    
    'total_course':QMODEL.Course.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    'total_coding_course':QMODEL.coding_course.objects.all().count(),
    'total_coding_question':QMODEL.coding_Question.objects.all().count(),
    }
    return render(request,'student/student_dashboard.html',context=dict)

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_exam_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student/student_exam.html',{'courses':courses})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_coding_exam_view(request):
    coding_courses = QMODEL.coding_course.objects.all()
    return render(request,'student/student_coding_exam.html',{'coding_courses':coding_courses})


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def face_access(request):
    return render(request,"student/face_access.html")

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def coding_face_access(request):
    return render(request,"student/coding_face_access.html")


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def take_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    total_questions=QMODEL.Question.objects.all().filter(course=course).count()
    questions=QMODEL.Question.objects.all().filter(course=course)
    total_marks=0
    for q in questions:
        total_marks=total_marks + q.marks
    
    return render(request,'student/take_exam.html',{'course':course,'total_questions':total_questions,'total_marks':total_marks})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def take_coding_exam_view(request,pk):
    coding_course=QMODEL.coding_course.objects.get(id=pk)
    total_coding_question=QMODEL.coding_Question.objects.all().filter(coding_course=coding_course).count()
    questions=QMODEL.coding_Question.objects.all().filter(coding_course=coding_course)
    total_coding_marks=0
    for q in questions:
        total_coding_marks=total_coding_marks + q.coding_marks
    
    return render(request,'student/take_coding_exam.html',{'coding_course':coding_course,'total_coding_question':total_coding_question,'total_coding_marks':total_coding_marks})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def start_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    questions=QMODEL.Question.objects.all().filter(course=course)
    if request.method=='POST':
        pass
    response= render(request,'student/start_exam.html',{'course':course,'questions':questions})
    response.set_cookie('course_id',course.id)
    return response


login_required(login_url='studentlogin')
@user_passes_test(is_student)
def view_all_coding_question(request,pk):
    coding_course=QMODEL.coding_course.objects.get(id=pk)
    questions=QMODEL.coding_Question.objects.all().filter(coding_course=coding_course)
    if request.method=='POST':
        pass 
    response= render(request,'student/view_all_coding_questions.html',{'coding_course':coding_course,'questions':questions})
    response.set_cookie('course_id',coding_course.id)
    return response


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def start_coding_exam_view(request,pk):
    coding_course=QMODEL.coding_course.objects.get(id=pk)
    questions=QMODEL.coding_Question.objects.all().filter(coding_course=coding_course)
    
    if request.method=='POST':
        
        pass
        
        
    response= render(request,'student/start_coding_exam.html',{'coding_course':coding_course,'questions':questions})
    response.set_cookie('course_id',coding_course.id)
    return response

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def calculate_marks_view(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course=QMODEL.Course.objects.get(id=course_id)
        
        total_marks=0
        questions=QMODEL.Question.objects.all().filter(course=course)
        for i in range(len(questions)):
            
            selected_ans = request.COOKIES.get(str(i+1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks = total_marks + questions[i].marks
        student = models.Student.objects.get(user_id=request.user.id)
        result = QMODEL.Result()
        result.marks=total_marks
        result.exam=course
        result.student=student
        result.save()

        return HttpResponseRedirect('view-result')

'''
@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def coding_part(request):
    if request.method=="POST":
        code_area=request.POST.get("code_area")
        input_area=request.POST.get("input_area")
        output=request.POST.get("output")
        result=QMODEL.codearea.objects.create(code_area=code_area,input_area=input_area,output=output)
        result.save()
        return HttpResponse("Successfully submitted")
''' 

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def runcode(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
            code_list.append(output)
            print(code_list)

        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        

    res = render(request,'student/start_coding_exam.html',{"code":code_part,"input":y,"output":output})
    return res


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def calculate_coding_marks_view(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course=QMODEL.coding_course.objects.get(id=course_id)
        
        total_marks=0
        questions=QMODEL.coding_Question.objects.all().filter(coding_course=course)
        check=QMODEL.codearea.objects.all()
        for i in range(len(questions)):
            selected_ans = code_list[0]
            actual_answer = questions[i].coding_answer
            print(actual_answer)
            print(selected_ans)
            if selected_ans == actual_answer:
                total_marks = total_marks + questions[i].coding_marks
        print(total_marks)
        student = models.Student.objects.get(user_id=request.user.id)
        result = QMODEL.coding_Result()
        result.coding_marks=total_marks
        result.coding_exam=course
        result.student=student
        result.save()
        return HttpResponseRedirect('view-coding-result')
    else:
        return HttpResponse('hello')
        
    




@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def view_result_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student/view_result.html',{'courses':courses})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def view_coding_result_view(request):
    course=QMODEL.coding_course.objects.all()
    return render(request,'student/view_coding_result.html',{'course':course})


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def check_marks_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    student = models.Student.objects.get(user_id=request.user.id)
    results= QMODEL.Result.objects.all().filter(exam=course).filter(student=student)
    return render(request,'student/check_marks.html',{'results':results})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def check_coding_marks_view(request,pk):
    coding_course=QMODEL.coding_course.objects.get(id=pk)
    student = models.Student.objects.get(user_id=request.user.id)
    coding_Result= QMODEL.coding_Result.objects.all().filter(coding_exam=coding_course).filter(student=student)
    return render(request,'student/check_coding_marks.html',{'coding_Result':coding_Result})



@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_marks_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student/student_marks.html',{'courses':courses})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_coding_marks_view(request):
    coding_course=QMODEL.coding_course.objects.all()
    return render(request,'student/student_coding_marks.html',{'coding_course':coding_course})


@csrf_exempt
def save_image(request):
    if request.method == 'POST':
        captured_image_data = request.POST.get('captured_image_data')
        captured_image = CapturedImage(image_data=captured_image_data)
        captured_image.save()
        return redirect('take-exam')
    return render(request, 'student/face_access.html')


    
