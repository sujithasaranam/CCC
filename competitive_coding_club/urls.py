from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logout,name="logout"),
    path('', views.home,name="home"),
path('dashboard/', views.dashboard,name="dashboard"),
   path('about/', views.about,name="about"),
    path('student/', views.student,name="student"),
    path('challenges/weekly/',views.weekly,name="weekly"),
    path('challenges/daily/',views.daily,name="daily"),
    path('challenges/monthly/',views.monthly,name="monthly"),
    path('discussionForum/',views.discussionForum,name="discussionForum"),
    path('index',views.index,name='index'),
    path('done',views.done,name='done'),
    path('submissions/',views.submissions,name="submissions"),
    path('profile/',views.profile,name="profile"),
     path('leaderboard/',views.leaderboard,name="leaderboard"),
     path('contact/',views.contact,name='contact'),
     path('events/',views.events,name='events'),
]