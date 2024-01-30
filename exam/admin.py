from django.contrib import admin

# Register your models here.
from .models import Course,coding_course,Question,coding_Question,Result,coding_Result,Contact

admin.site.register(Course)
admin.site.register(coding_course)
admin.site.register(Question)
admin.site.register(coding_Question)
admin.site.register(Result)
admin.site.register(coding_Result)
admin.site.register(Contact)

