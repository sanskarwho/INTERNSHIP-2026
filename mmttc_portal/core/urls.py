from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.login_page ,name = 'login'),
    path('register/', views.register_page, name='register'),
    path('courses/', views.courses, name='courses'),

    path('dashboard/', views.applicant_dashboard,
         name='applicant_dashboard'),

    path('admin-dashboard/', views.admin_dashboard,
         name='admin_dashboard'), 

    path('create-course/',
     views.create_course,
     name='create_course'),

    path('manage-courses/',
     views.manage_courses,
     name='manage_courses'),

    path('edit-course/<int:id>/',
     views.edit_course,
     name='edit_course'),

    path('delete-course/<int:id>/',
     views.delete_course,
     name='delete_course'),

    path('apply-course/<int:id>/',
     views.apply_course,
     name='apply_course'),

    path('view-applications/',
     views.view_applications,
     name='view_applications'),

    path('my-applications/',
     views.my_applications,
     name='my_applications'),

    path('objective/',
     views.objective,
     name='objective'),

    path('philosophy/',
     views.philosophy,
     name='philosophy'),

     path('functions/',
     views.functions,
     name='functions'),

     path('responsibility/',
     views.responsibility,
     name='responsibility'),

     path('isro-edusat/',
     views.isro_edusat,
     name='isro_edusat'),

     path('facilities/',
     views.facilities,
     name='facilities'),

     path(
    'programme-courses/',
    views.programme_courses,
    name='programme_courses'),

    path('curriculum/',
     views.curriculum,
     name='curriculum'),
    path(
    'course-coordinator/',
    views.course_coordinator,
    name='course_coordinator'),

     path(
    'teaching-staff/',
    views.teaching_staff,
    name='teaching_staff'),

]