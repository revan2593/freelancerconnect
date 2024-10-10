from django.urls import path
from .import views

urlpatterns = [
   path('',views.home,name='homepage'),
   path('login/',views.login ,name='loginpage' ),
   path('businesses/',views.business,name='businesses'),
   path('projects/',views.projects,name='projects')
]
