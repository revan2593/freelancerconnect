from django.urls import path,include
from .import views

urlpatterns = [
   path('',views.home,name='homepage'),
   path('login/',views.logininto ,name='loginpage' ),
   path('businesses/',views.business,name='businesses'),
   path('projects/',views.project,name='projects'),
   path('register/', views.register, name='register'),
   path('setup_freelancer/',views.setup_freelancer, name="setup_freelancer" ),
   path('logout/', views.logout_view, name='logoutpage' ),
   path('setup_corporate/',views.setup_corporate,name='setup_corporate' ),
   # path('profile/',views.profile,name='profile'),
   path('addproject/',views.create_project,name='create_project'),
   path('projects/apply/', views.apply_to_project, name='apply_to_project'),
   path('profile/<int:project_id>/',views.myprojectsinfo,name='myproject'),
   path('profile/<str:user_name>/',views.profile ,name='profile'),
   path('profile/<int:project_id>/<int:freelancer_id>',views.offer ,name='offer'),
   path('accept/<int:project_id>/',views.accept,name='accept'),
   path('review/<int:project_id>',views.give_review,name='review'),
   path('reject/<int:project_id>/',views.reject,name='reject'),
   path('edit-profile/', views.edit_profile, name='edit_profile'),
   path('freelancers/',views.freelancer, name='freelancers'),

]

