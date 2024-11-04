from django.urls import path, include
from. import views

urlpatterns = [
    path('', views.projecthomepage, name= 'projecthomepage'),
    path('printpagecall/',views.printpagecall, name='printpagecall'),#-- exactly match with projectnavbar.html
    path('printpagelogic/',views.printpagelogic, name='printpagelogic'),
    path('exceptionpagelogic/', views.exceptionpagelogic, name='exceptionpagelogic'),#--must with ExceptionExample.html
    path('exceptionpagecall/', views.exceptionpagecall, name='exceptionpagecall'),
    path('randompagecall/',views.randompagecall,name='randompagecall'),
    path('randomlogic/',views.randomlogic, name = 'randomlogic'),
    path('calculatorpagecall/',views.calculatorpagecall, name='calculatorpagecall'),
    path('calculatorlogic',views.calculatorlogic,name='calculatorlogic'),
    path('UserLoginPageCall',views.UserLoginPageCall,name='UserLoginPageCall'),
    path('UserLoginLogic',views.UserLoginLogic,name='UserLoginLogic'),
    path('datetimepagelogic',views.datetimepagelogic,name='datetimepagelogic'),
    path('datetimepagecall',views.datetimepagecall,name='datetimepagecall'),
    path('add_task/',views.add_task,name='add_task'),
    path('<int:pk>/delete/',views.delete_task,name='delete_task'),
    path('UserRegisterLogic/',views.UserRegisterLogic,name='UserRegisterLogic'),
    path('UserRegisterPageCall/',views.UserRegisterPageCall,name='UserRegisterPageCall'),
    path('logout/',views.logout,name='logout'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/',views.student_list,name='student_list'),
    #path('add_studentcall/', views.add_studentcall, name='add_studentcall'),
    #path('student_listcall/', views.student_listcall, name='student_listcall')
    path('upload_file/',views.upload_file,name='upload_file'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('add/', views.add_contact, name='add_contact'),
    path('contact_list', views.contact_list, name='contact_list'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),


]
