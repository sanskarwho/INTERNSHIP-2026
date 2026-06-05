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

    path(
    'non-teaching-staff/',
    views.non_teaching_staff,
    name='non_teaching_staff'),

    path('activities/',
     views.activities,
     name='activities'),

     path(
    'terms-and-conditions/',
    views.terms_conditions,
    name='terms_conditions'),

     path(
    'evaluation-participants/',
    views.evaluation_participants,
    name='evaluation_participants'),

    path(
    'resource-persons/',
    views.resource_persons,
    name='resource_persons'),

    path(
    'contact/',
    views.contact_us,
    name='contact_us'),
     path(
     'gallery/',
     views.gallery,
     name='gallery'),

     path(
    'view-messages/',
    views.view_messages,
    name='view_messages'),

     path('apply-online/',
     views.application_instructions,
     name='apply_online'),

     path('application-form/',
     views.apply_online,
     name='application_form'),

     path('reupload-form/',
     views.reupload_form,
     name='reupload_form'),

     path('application-status/', views.application_status, name='application_status'),

     path('success/', views.success_page, name='success_page'),

     path('update-course-status/<int:id>/',
     views.update_course_status,
     name='update_course_status'),

     path(
    'mark-course-full/<int:id>/',
    views.mark_course_full,
    name='mark_course_full'
     ),

     path(
     'mark-course-vacant/<int:id>/',
     views.mark_course_vacant,
     name='mark_course_vacant'
     ),

     path(
     'hide-course/<int:id>/',
     views.hide_course,
     name='hide_course'
     ),

     path(
     'show-course/<int:id>/',
     views.show_course,
     name='show_course'
     ),

     path('generate-schedule-pdf/',
     views.generate_schedule_pdf,
     name='generate_schedule_pdf'),

     path(
    'view-all-applications/',
    views.view_all_applications,
    name='view_all_applications'
     ),

     path(
     'verify-applications/',
     views.verify_applications,
     name='verify_applications'
     ),

     path(
    'application-details/<int:id>/',
    views.application_details,
    name='application_details'
     ),

     path(
    'approve-application/<int:id>/',
    views.approve_application,
    name='approve_application'
     ),

     path(
     'reject-application/<int:id>/',
     views.reject_application,
     name='reject_application'
     ),

     path(
     'generate-certificates/',
     views.generate_certificates,
     name='generate_certificates'
     ),

     path(
     'generate-certificate/<int:id>/',
     views.generate_certificate,
     name='generate_certificate'
     ),

     path(
     'certificates/',
     views.certificates,
     name='certificates'
     ),

     path(
     'verify-certificate/<str:certificate_id>/',
     views.verify_certificate,
     name='verify_certificate'
     ),


]