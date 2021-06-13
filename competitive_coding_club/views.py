from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from .models import Student,DailyAssesments1,MonthlyAssesments,WeeklyAssesments,DiscussionForum,clinks,Status
from .forms import CreateUserForm
from competitive_coding_club.templatetags import extras
import datetime
import requests
import json

# Create your views here.
a={}
def url(a):
    url = "https://codexweb.netlify.app/.netlify/functions/enforceCode"
    payload = json.dumps(a)
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    #Codex.objects.codex{
        #code = a["code"],
        #language = a["language"],
        #input = a["input"]
    #}
    dict = response.json()
    return dict

def studrank(username,obj):
	r=1
	for i in obj:
		if i.username!=username:
			r+=1
		else:
			break
	return r
def clusterrank(username,obj):
	dr=1
	for i in obj:
		if i.user!=username:
			dr+=1
		else:
			break
	return dr
def ret(user):
	v=[]
	hm2=Status.objects.all()
	hm1=Student.objects.get(username=user)
	t=0
	for i in hm2:
		if i.user==user:
			t+=1
			break
	if(t==0):
		hm=Status(user=user,category=hm1.category)
		hm.save()
		hmpage=Status.objects.get(user=user)
	else:
		hmpage=Status.objects.get(user=user)
	if(hmpage.dmarks>10000 and hmpage.mmarks>1000 and hmpage.wmarks>1000):
		if(hm1.category=='SEEKER(LEVEL 1)'):
			hm1.category='PRACTITIONER(LEVEL 2)'
			hm1.save()
		elif(hm1.category=='PRACTITIONER(LEVEL 2)'):
			hm1.category='CHALLENGER(LEVEL 3)'
			hm1.save()
		elif(hm1.category=='CHALLENGER(LEVEL 3)'):
			hm1.category='PERFORMER(LEVEL 4)'
			hm1.save()
	hm1.total_marks=hmpage.dmarks+hmpage.mmarks+hmpage.wmarks
	hm1.save()
	hm2=Student.objects.all()
	leaderboardtot=Student.objects.order_by('total_marks').reverse()
	tots=Student.objects.filter(category='SEEKER(LEVEL 1)').order_by('total_marks').reverse()
	totpr=Student.objects.filter(category='PRACTITIONER(LEVEL 2)').order_by('total_marks').reverse()
	totc=Student.objects.filter(category='CHALLENGER(LEVEL 3)').order_by('total_marks').reverse()
	totpe=Student.objects.filter(category='PERFORMER(LEVEL 4)').order_by('total_marks').reverse()
	das=Status.objects.filter(category='SEEKER(LEVEL 1)').order_by('dmarks').reverse()
	dapr=Status.objects.filter(category='PRACTITIONER(LEVEL 2)').order_by('dmarks').reverse()
	dac=Status.objects.filter(category='CHALLENGER(LEVEL 3)').order_by('dmarks').reverse()
	dape=Status.objects.filter(category='PERFORMER(LEVEL 4)').order_by('dmarks').reverse()
	mas=Status.objects.filter(category='SEEKER(LEVEL 1)').order_by('mmarks').reverse()
	mapr=Status.objects.filter(category='PRACTITIONER(LEVEL 2)').order_by('mmarks').reverse()
	mac=Status.objects.filter(category='CHALLENGER(LEVEL 3)').order_by('mmarks').reverse()
	mape=Status.objects.filter(category='PERFORMER(LEVEL 4)').order_by('mmarks').reverse()
	was=Status.objects.filter(category='SEEKER(LEVEL 1)').order_by('wmarks').reverse()
	wapr=Status.objects.filter(category='PRACTITIONER(LEVEL 2)').order_by('wmarks').reverse()
	wac=Status.objects.filter(category='CHALLENGER(LEVEL 3)').order_by('wmarks').reverse()
	wape=Status.objects.filter(category='PERFORMER(LEVEL 4)').order_by('wmarks').reverse()
	leaderboarddam=Status.objects.order_by('dmarks').reverse()
	leaderboardmam=Status.objects.order_by('mmarks').reverse()
	leaderboardwam=Status.objects.order_by('wmarks').reverse()
	ranks=studrank(user.username,tots)
	rankpr=studrank(user.username,totpr)
	rankc=studrank(user.username,totc)
	rankpe=studrank(user.username,totpe)
	dasr=clusterrank(user,das)
	dappr=clusterrank(user,dapr)
	dacr=clusterrank(user,dac)
	daper=clusterrank(user,dape)
	masr=clusterrank(user,mas)
	mappr=clusterrank(user,mapr)
	macr=clusterrank(user,mac)
	maper=clusterrank(user,mape)
	wasr=clusterrank(user,was)
	wappr=clusterrank(user,wapr)
	wacr=clusterrank(user,wac)
	waper=clusterrank(user,wape)
	leaderboardtotrank=studrank(user.username,leaderboardtot)
	lbdrank=clusterrank(user,leaderboarddam)
	lbmrank=clusterrank(user,leaderboardmam)
	lbwrank=clusterrank(user,leaderboardwam)
	v.append(hmpage.dmarks)
	v.append(hmpage.mmarks)
	v.append(hmpage.wmarks)
	v.append(hmpage.category)
	v.append(hm1.total_marks)
	v.append(ranks)
	v.append(rankpr)
	v.append(rankc)
	v.append(rankpe)
	v.append(dasr)
	v.append(dappr)
	v.append(dacr)
	v.append(daper)
	v.append(masr)
	v.append(mappr)
	v.append(macr)
	v.append(maper)
	v.append(wasr)
	v.append(wappr)
	v.append(wacr)
	v.append(waper)
	v.append(leaderboardtotrank)
	v.append(leaderboardtot)
	return v

def index(request):
	user = request.user
	t=0
	x1=clinks.objects.all()
	but=request.POST['but']
	if(but=="1"):
		if request.method=='POST':
			wa=request.POST['wa']
			if wa=='D':
				x=DailyAssesments1.objects.all()
				d=request.POST['dpid']
				dpid=x[int(d)-1]
				for i in x1:
					if(i.user==user and dpid==i.dpid):
						t+=1
						break
				if(t==0):
					ins1=clinks(dpid=dpid,frmassessment=wa,user=user,marks=0)
					ins1.save()
				else:
					ins1=clinks.objects.all()
				all_pro=DailyAssesments1.objects.filter(auto_increment_id=d)
				context={'stat':ins1,'desc':all_pro}	
			elif wa=='M':
				x=MonthlyAssesments.objects.all()
				m=request.POST['mpid']
				mpid=x[int(m)-1]
				for i in x1:
					if(i.user==user and mpid==i.mpid):
						t+=1
						break
				if(t==0):
					ins1=clinks(mpid=mpid,frmassessment=wa,user=user,marks=0)
					ins1.save()	
				else:
					ins1=clinks.objects.all()
				all_pro=MonthlyAssesments.objects.filter(auto_increment_id=m)
				context={'stat':ins1,'desc':all_pro}
			else:
				x=WeeklyAssesments.objects.all()
				w=request.POST['wpid']
				wpid=x[int(w)-1]
				for i in x1:
					if(i.user==user and wpid==i.wpid):
						t+=1
						break
				if(t==0):
					ins1=clinks(wpid=wpid,frmassessment=wa,user=user,marks=0)
					ins1.save()	
				else:
					ins1=clinks.objects.all()
				all_pro=WeeklyAssesments.objects.filter(auto_increment_id=w)
				context={'stat':ins1,'desc':all_pro}
		return render(request,'index.html',context)
	else:
		a={"code":request.POST["code"],"language":request.POST["language"],"input":request.POST["input"]}
		dict=url(a)
		wa=request.POST['wa']
		if wa=='D':
			d=request.POST['pid']
			all_pro=DailyAssesments1.objects.filter(auto_increment_id=d)
		elif wa=='M':
			d=request.POST['pid']
			all_pro=MonthlyAssesments.objects.filter(auto_increment_id=d)
		else:
			d=request.POST['pid']
			all_pro=WeeklyAssesments.objects.filter(auto_increment_id=d)
		return render(request,'index.html',{'output':dict['output'],'code':dict['sourceCode'],'language':dict['language'],'desc':all_pro})
		
def compare(a,b):
	a=a.rstrip("\n")
	if(a == b):
		return "done"
	else:
		return "not done"		


def done(request):
	if request.method=='POST':
		a={"code":request.POST["code"],"language":request.POST["language"],"input":request.POST["input"]}
		dict=url(a)
		count=0
		t=0
		p=0
		user=request.user
		wa=request.POST['wa']
		x1=clinks.objects.all()
		if wa=='D':
			d=request.POST['pid']
			x=DailyAssesments1.objects.all()
			all_pro=DailyAssesments1.objects.get(auto_increment_id=d)
			dpid=x[int(d)-1]
			for i in x1:
				if(i.user==user and dpid==i.dpid):
					p=i.marks
					t+=1
					break
			upd=clinks.objects.get(dpid=dpid,user=user)
			upd.code=dict['sourceCode']
			upd.language=dict['language']
			upd.save()
		elif wa=='M':
			d=request.POST['pid']
			x=MonthlyAssesments.objects.all()
			all_pro=MonthlyAssesments.objects.get(auto_increment_id=d)
			dpid=x[int(d)-1]
			for i in x1:
				if(i.user==user and dpid==i.mpid):
					p=i.marks
					t+=1
					break
			print(p)
			upd=clinks.objects.get(mpid=dpid,user=user)
			upd.code=dict['sourceCode']
			upd.language=dict['language']
			upd.save()
		else:
			d=request.POST['pid']
			x=WeeklyAssesments.objects.all()
			all_pro=WeeklyAssesments.objects.get(auto_increment_id=d)
			dpid=x[int(d)-1]
			for i in x1:
				if(i.user==user and dpid==i.wpid):
					p=i.marks
					t+=1
					break
			upd=clinks.objects.get(wpid=dpid,user=user)
			upd.code=dict['sourceCode']
			upd.language=dict['language']
			upd.save()
		a={"code":upd.code,"language":upd.language,"input":all_pro.inp1}
		dict=url(a)
		out=dict['output']
		xz=compare(str(out),str(all_pro.outp1))
		if(xz=="done"):
			count+=1
		a={"code":upd.code,"language":upd.language,"input":all_pro.inp2}
		dict=url(a)
		out=dict['output']
		xz=compare(str(out),str(all_pro.outp2))
		if(xz=="done"):
			count+=1
		all_pro.tcs=count
		gm=all_pro.max_marks/2
		gm=gm*count
		upd.marks=gm
		if(gm==all_pro.max_marks):
			upd.sub=1
			upd.subfail=0
		else:
			upd.sub=0
			upd.subfail=1
		all_pro.marks=gm
		all_pro.save()
		upd.save()
		hm1=Student.objects.get(username=user)
		hmp=Status.objects.get(user=user)
		if(t==0):
			if(wa=='D'):
				hmp.dmarks=hmp.dmarks+gm
				hmp.save()
			elif(wa=='M'):
				print(hmp.mmarks)
				hmp.mmarks=hmp.mmarks+gm
				hmp.save()
			else:
				hmp.wmarks=hmp.wmarks+gm
				hmp.save()
		else:
			if(wa=='D'):
				hmp.dmarks-=p
				hmp.dmarks=hmp.dmarks+gm
				hmp.save()
			elif(wa=='M'):
				print(hmp.mmarks)
				hmp.mmarks-=p
				print(hmp.mmarks)
				hmp.mmarks=hmp.mmarks+gm
				print(hmp.mmarks)
				hmp.save()
			else:
				hmp.wmarks-=p
				hmp.wmarks=hmp.wmarks+gm
				hmp.save()
		return render(request,'testcases.html',{'tcs':count,'marks':gm})
	else:
		index()


l1=[] 
l1.append('')	
        
# Create your views here.
def registerPage(request):
	'''if request.user.is_authenticated:
		return redirect('home')
	else:'''
	form=CreateUserForm()
	if request.method=='POST':
		form=CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user=form.cleaned_data.get('username')
			messages.success(request,'Account was created for '+user)
			l1[0]=user
			return redirect('student')
	context={'form':form}
	return render(request,'accounts/register.html',context)

def loginPage(request):
	'''if request.user.is_authenticated:
		return redirect('home')
	else:'''
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect('dashboard')
		else:
			messages.info(request,'Username or password is incorrect')
		
	context={}
	return render(request,'accounts/login.html',context)

    

def logout(request):
	auth.logout(request)
	return redirect('home')

def home(request):
	return render(request,'accounts/home.html')

def dashboard(request):
	user=request.user
	if user.id == None:
		return render(request,'accounts/dashboard.html')
	else:
		val=ret(user)
		sta=clinks.objects.filter(user=user)
		sp=0
		sf=0
		st=0
		for i in sta:
			if(i.sub==1):
				sp+=1
			else:
				sf+=1
		st=sp+sf
		print(sp,sf,st)
		context={'sp':sp,'sf':sf,'st':st,'category':val[3]}
		return render(request,'accounts/dashboard.html',context)


def profile(request):
	user=request.user
	if user.id == None:
		return render(request,'accounts/profile.html')
	else:
		val=ret(user)
		context={'dmarks':val[0],'mmarks':val[1],'wmarks':val[2],'category':val[3],'total_marks':val[4],
		'ranks':val[5],'rankpr':val[6],'rankc':val[7],'rankpe':val[8],
		'dasr':val[9],'dappr':val[10],'dacr':val[11],'daper':val[12],
		'masr':val[13],'mappr':val[14],'macr':val[15],'maper':val[16],
		'wasr':val[17],'wappr':val[18],'wacr':val[19],'waper':val[20]}
		return render(request,'accounts/profile.html',context)

def leaderboard(request):
	user=request.user
	if user.id == None:
		leaderboardtot=Student.objects.all().order_by('total_marks').reverse()
		return render(request,'accounts/leaderboard.html',{'leader':leaderboardtot})
	else:
		val=ret(user)
		leaderboardtot=Student.objects.all().order_by('total_marks').reverse()
		context={'dmarks':val[0],'mmarks':val[1],'wmarks':val[2],'category':val[3],'total_marks':val[4],
		'leadertotra':val[21],'leader':leaderboardtot}
		return render(request,'accounts/leaderboard.html',context)


def submissions(request):
	user=request.user
	if user.id == None:
		return render(request,'accounts/submissions.html')
	else:
		ts=clinks.objects.all()
		ts1=clinks.objects.filter(user=user)
		da=DailyAssesments1.objects.all()
		ma=MonthlyAssesments.objects.all()
		wa=WeeklyAssesments.objects.all()
		for i in ts1:
			if(i.dpid):
				for j in da:
					if(i.dpid==da[j.auto_increment_id-1]):
						p=clinks.objects.get(dpid=i.dpid,user=user)
						p.problem=j.problem
						p.heading=j.heading
						p.save()
			elif(i.mpid):
				for j in ma:
					if(i.mpid==ma[j.auto_increment_id-1]):
						p=clinks.objects.get(mpid=i.mpid,user=user)
						p.problem=j.problem
						p.heading=j.heading
						p.save()
			else:
				for j in wa:
					if(i.wpid==wa[j.auto_increment_id-1]):
						p=clinks.objects.get(wpid=i.wpid,user=user)
						p.problem=j.problem
						p.heading=j.heading
						p.save()
		context={'ts1':ts1}
		return render(request,'accounts/submissions.html',context)
	


def about(request):
	return render(request,'accounts/about.html')
def weekly(request):
	user = request.user.username
	sta=Student.objects.filter(username=user)
	all_pro2=WeeklyAssesments.objects.all()
	context={'stat':sta,'Weekly':all_pro2}
	return render(request,'accounts/challenges/weekly.html',context)

def daily(request):
	user = request.user.username
	sta=Student.objects.filter(username=user)
	all_pro=DailyAssesments1.objects.all()
	context={'stat':sta,'Daily':all_pro}
	return render(request,'accounts/challenges/daily.html',context)

def monthly(request):
	user = request.user.username
	sta=Student.objects.filter(username=user)
	all_pro1=MonthlyAssesments.objects.all()
	context={'stat':sta,'Monthly':all_pro1}
	return render(request,'accounts/challenges/monthly.html',context)


def student(request):
    if request.method=='POST':
        username=l1[0]
        phone=request.POST['phone']
        yearOfStudy=request.POST['yearOfStudy']
        category=request.POST['category']
        ins=Student(username=username,phone=phone,yearOfStudy=yearOfStudy,category=category)
        ins.save()
        return redirect('login')
    return render(request,'accounts/student.html',{'username':l1[0]})

def discussionForum(request):
	user = request.user
	timestamp=datetime.datetime.now()
	if request.method=='POST':
		comment=request.POST['comment']
		parentsno=request.POST['parentsno']
		if parentsno=="":
			res=DiscussionForum(comment=comment,user=user,timestamp=timestamp)
		else:
			parent=DiscussionForum.objects.get(sno=parentsno)
			res=DiscussionForum(comment=comment,user=user,timestamp=timestamp,parent=parent)
		res.save()
	comments=DiscussionForum.objects.filter(parent=None)
	replies=DiscussionForum.objects.exclude(parent=None)
	repDict={}
	for reply in replies:
		if reply.parent.sno not in repDict.keys():
			repDict[reply.parent.sno]=[reply]
		else:
			repDict[reply.parent.sno].append(reply)
	context={'cs':comments,'repDict':repDict}
	return render(request,'accounts/discussionForum.html',context)

def contact(request):
    return render(request,'accounts/contact.html')
def events(request):
    return render(request,'accounts/events.html')