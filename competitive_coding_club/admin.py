from django.contrib import admin

# Register your models here.
from .models import Student,DailyAssesments1,WeeklyAssesments,MonthlyAssesments,DiscussionForum,clinks,Status
admin.site.register(Student)
admin.site.register(DailyAssesments1)
admin.site.register(WeeklyAssesments)
admin.site.register(MonthlyAssesments)
admin.site.register(DiscussionForum)
admin.site.register(clinks)
admin.site.register(Status)