from django.db import models

from student.models import Student
class Course(models.Model):
   course_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   duration = models.PositiveIntegerField()


   def __str__(self):
        return self.course_name

class coding_course(models.Model):
   course_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   duration = models.PositiveIntegerField()

   def __str__(self):
        return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)


class coding_Question(models.Model):
    coding_course=models.ForeignKey(coding_course,on_delete=models.CASCADE)
    coding_marks=models.PositiveIntegerField()
    coding_question=models.CharField(max_length=600)
    coding_answer=models.CharField(max_length=200)


class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

class coding_Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    coding_exam = models.ForeignKey(coding_course,on_delete=models.CASCADE)
    coding_marks = models.PositiveIntegerField()
    coding_date = models.DateTimeField(auto_now=True)

class codearea(models.Model):
    code_area=models.CharField(max_length=1000)
    input_area=models.CharField(max_length=1000)
    output=models.CharField(max_length=1000)
    def __str__(self):
        return self.output

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    message=models.TextField(max_length=500)
    def __str__(self):
        return self.name


