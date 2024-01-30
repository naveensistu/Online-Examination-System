from django.urls import path
from student import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('studentclick', views.studentclick_view),
path('studentlogin', LoginView.as_view(template_name='student/studentlogin.html'),name='studentlogin'),
path('studentsignup', views.student_signup_view,name='studentsignup'),
path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),
path('student-exam', views.student_exam_view,name='student-exam'),
path('student-coding-exam', views.student_coding_exam_view,name='student-coding-exam'),

path('take-exam/<int:pk>', views.take_exam_view,name='take-exam'),
path('take-coding-exam/<int:pk>', views.take_coding_exam_view,name='take-coding-exam'),

path('start-exam/<int:pk>', views.start_exam_view,name='start-exam'),
path('start-coding-exam/<int:pk>', views.start_coding_exam_view,name='start-coding-exam'),
path('start-coding-exam/<int:pk>', views.start_coding_exam_view,name='start-coding-exam'),
path('view-all-coding-question/<int:pk>', views.view_all_coding_question,name='view-all-coding-question'),

path('coding-face-access',views.coding_face_access,name='coding-face-access'),

path('face-access',views.face_access,name='face-access'),
path('save-image',views.save_image,name="save-image"),

path('calculate-marks', views.calculate_marks_view,name='calculate-marks'),
path('calculate-coding-marks', views.calculate_coding_marks_view,name='calculate-coding-marks'),

path('view-result', views.view_result_view,name='view-result'),
path('view-coding-result', views.view_coding_result_view,name='view-coding-result'),

path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),
path('check-coding-marks/<int:pk>', views.check_coding_marks_view,name='check-coding-marks'),

path('student-marks', views.student_marks_view,name='student-marks'),
path('student-coding-marks', views.student_coding_marks_view,name='student-coding-marks'),
path('runcode',views.runcode,name='runcode'),
]