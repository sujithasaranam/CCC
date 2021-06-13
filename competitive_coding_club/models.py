from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Student(models.Model):
    CATEGORY=(
        ('SEEKER(LEVEL 1)','SEEKER(LEVEL 1)'),
        ('PRACTITIONER(LEVEL 2)','PRACTITIONER(LEVEL 2)'),
        ('CHALLENGER(LEVEL 3)','CHALLENGER(LEVEL 3)'),
        ('PERFORMER(LEVEL 4)','PERFORMER(LEVEL 4)'),)
    YEAR=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    )
    username=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=10,null=True)
    yearOfStudy=models.CharField(max_length=5,null=True,choices=YEAR)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
    total_marks=models.IntegerField(default=0)

    def __str__(self):
        return self.username



class WeeklyAssesments(models.Model):
    #uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    CATEGORY=(
        ('SEEKER(LEVEL 1)','SEEKER(LEVEL 1)'),
        ('PRACTITIONER(LEVEL 2)','PRACTITIONER(LEVEL 2)'),
        ('CHALLENGER(LEVEL 3)','CHALLENGER(LEVEL 3)'),
        ('PERFORMER(LEVEL 4)','PERFORMER(LEVEL 4)'),)
    auto_increment_id = models.AutoField(primary_key=True)
    heading=models.CharField(max_length=200,null=True)
    problem = models.TextField(null=True)
    des= models.TextField(null=True)
    marks=models.IntegerField()
    flag=models.CharField(max_length=1, default='W', editable=False)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
    inp1=models.TextField(null=True,blank=True)
    outp1=models.TextField(null=True,blank=True)
    inp2=models.TextField(null=True,blank=True)
    outp2=models.TextField(null=True,blank=True)
    max_marks=models.IntegerField(default=0)
    tcs=models.IntegerField(default=0)

    def __int__(self):
        return self.auto_increment_id

class MonthlyAssesments(models.Model):
    #uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    CATEGORY=(
        ('SEEKER(LEVEL 1)','SEEKER(LEVEL 1)'),
        ('PRACTITIONER(LEVEL 2)','PRACTITIONER(LEVEL 2)'),
        ('CHALLENGER(LEVEL 3)','CHALLENGER(LEVEL 3)'),
        ('PERFORMER(LEVEL 4)','PERFORMER(LEVEL 4)'),)
    auto_increment_id = models.AutoField(primary_key=True)
    heading=models.CharField(max_length=200,null=True)
    problem = models.TextField(null=True)
    des= models.TextField(null=True)
    marks=models.IntegerField()
    flag=models.CharField(max_length=1, default='M', editable=False)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
    inp1=models.TextField(null=True,blank=True)
    outp1=models.TextField(null=True,blank=True)
    inp2=models.TextField(null=True,blank=True)
    outp2=models.TextField(null=True,blank=True)
    max_marks=models.IntegerField(default=0)
    tcs=models.IntegerField(default=0)

    def __int__(self):
        return self.auto_increment_id

class DailyAssesments1(models.Model):
    #uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    CATEGORY=(
        ('SEEKER(LEVEL 1)','SEEKER(LEVEL 1)'),
        ('PRACTITIONER(LEVEL 2)','PRACTITIONER(LEVEL 2)'),
        ('CHALLENGER(LEVEL 3)','CHALLENGER(LEVEL 3)'),
        ('PERFORMER(LEVEL 4)','PERFORMER(LEVEL 4)'),)
    auto_increment_id = models.AutoField(primary_key=True)
    heading=models.CharField(max_length=200,null=True)
    problem = models.TextField(null=True)
    des= models.TextField(null=True)
    marks=models.IntegerField(null=True,default=0)
    flag=models.CharField(max_length=1, default='D', editable=False)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
    inp1=models.TextField(null=True,blank=True)
    outp1=models.TextField(null=True,blank=True)
    inp2=models.TextField(null=True,blank=True)
    outp2=models.TextField(null=True,blank=True)
    max_marks=models.IntegerField(default=0)
    tcs=models.IntegerField(default=0)

    def __int__(self):
        return self.auto_increment_id

#class Description(model.Model)
class DiscussionForum(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment

class clinks(models.Model):
    language=(
        ('cpp','cpp'),
        ('c','c'),
        ('cs','cs'),
        ('java','java'),
        ('py','py'),
        ('rb','rb'),
        ('kt','kt'),
        ('kt','kt'),
        ('swift','swift')
        )
    sno= models.AutoField(primary_key=True)
    dpid=models.ForeignKey(DailyAssesments1,on_delete=models.CASCADE,null=True,blank=True)
    mpid=models.ForeignKey(MonthlyAssesments,on_delete=models.CASCADE,null=True,blank=True)
    wpid=models.ForeignKey(WeeklyAssesments,on_delete=models.CASCADE,null=True,blank=True)
    frmassessment=models.CharField(max_length=1,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    code=models.TextField(null=True,blank=True)
    language=models.CharField(max_length=5,null=True,blank=True,choices=language)
    marks=models.IntegerField(default=0)
    problem = models.TextField(null=True,blank=True)
    heading=models.CharField(max_length=200,null=True,blank=True)
    sub=models.IntegerField(default=0)
    subfail=models.IntegerField(default=0)
    
class Status(models.Model):
    CATEGORY=(
        ('SEEKER(LEVEL 1)','SEEKER(LEVEL 1)'),
        ('PRACTITIONER(LEVEL 2)','PRACTITIONER(LEVEL 2)'),
        ('CHALLENGER(LEVEL 3)','CHALLENGER(LEVEL 3)'),
        ('PERFORMER(LEVEL 4)','PERFORMER(LEVEL 4)'),)
    dmarks=models.IntegerField(default=0)
    mmarks=models.IntegerField(default=0)
    wmarks=models.IntegerField(default=0)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)






    







