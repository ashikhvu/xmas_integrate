from django.urls import path,re_path
from.import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve


urlpatterns = [

  
    path('',views.landingPage,name='landigPage'),
    path('Vacancy',views.vacancy,name='vacancy'),
    path('home',views.text_page,name='text_page'),
    # path('home',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('course',views.course,name='course'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('Service',views.service,name='service'),
    path('Core',views.core,name='core'),
    path('base',views.base,name='base'),
    path('Our-Events',views.events,name='events'),
    path('Our-Events/<int:pk>',views.event_details,name='event_details'),
    
    path('Job-apply',views.job_appy,name='job_appy'),
    path('Contact',views.vacancy_contact,name='vacancy_contact'),
    
         


    # Technologies Pages
    path('Artificial-Intelligence',views.ai,name='ai'),
    path('3Dimenzions',views.dimen,name='dimen'),
    path('Virtual-Reality',views.vr,name='vr'),
    path('Python',views.python,name='python'),
    path('React',views.react,name='react'),
    path('Angular',views.angular,name='angular'),
    path('PHP',views.php,name='php'),
    path('Android',views.android,name='android'),
    path('Game-Development',views.game,name='game'),
    path('Machine-Learning',views.ml,name='ml'),
    path('Digital-marketing',views.dm,name='dm'),
    




    path('add_user',views.add_user,name='add_user'),
    path('reg',views.reg,name='reg'),
    path('enquerys',views.enquerys,name='enquerys'),
    path('app',views.app,name='app'),

    path('ex',views.ex,name='ex'),

    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    
    path('admin_login',views.admin_login,name='admin_login'),
    path('base2',views.base2,name='base2'),

    path('Admin-DashBoard',views.dashboard,name='dashboard'),
    path('load_passwords',views.load_password,name='load_password'),
    path('add_password/<int:user_id>',views.add_password,name="add_password"),
         
    path('Course-Applications',views.course_application,name='course_application'),
    path('Job-Applications',views.job_application,name='job_application'),
    path('job_appl_approve/<int:pk>',views.job_appl_approve,name="job_appl_approve"),
    path('job_appl_reject/<int:pk>',views.job_appl_reject,name="job_appl_reject"),
    path('job_appl_delete/<int:pk>',views.job_appl_delete,name="job_appl_delete"),
         
         
    
    path('Enquery',views.ad_enquerys,name='ad_enquerys'),
    path('Course',views.ad_course,name='ad_course'),
    path('Add-Course',views.add_course,name='add_course'),
    path('Edit-Course-Save/<int:pk>',views.edit_course_save,name="edit_course_save"),
    path('Remove-Course/<int:pk>',views.remove_course,name="remove_course"),



    path('Add-Events',views.ad_events,name='ad_events'),
    path('Save-Events',views.add_event,name='add_event'),
    path('Remove-Event/<int:pk>',views.event_remove,name="event_remove"),
    path('jobs',views.jobs,name='jobs'),    
    path('add_vacancy',views.add_vacancy,name='add_vacancy'),
    path('edit_vacany/<int:pk>',views.edit_vacany,name="edit_vacany"),
    path('editsave_vacancy/<int:pk>',views.editsave_vacancy,name="editsave_vacancy"),
    path('Remove_vacany/<int:pk>',views.remove_vacany,name="remove_vacany"),
         
    path('Gallery',views.ad_gallery,name='ad_gallery'),
    path('Save-Images',views.add_images,name='add_images'),
    path('Remove-Image/<int:pk>',views.image_remove,name="image_remove"),
    path('Poster',views.ad_poster,name='ad_poster'),
    path('Poster-Save',views.add_poster,name='add_poster'),
    path('Remove-Poster/<int:pk>',views.poster_remove,name="poster_remove"),
    
    
    
    path('News',views.ad_News,name='ad_News'),
    path('Save-News',views.add_news,name='add_news'),
    path('Remove-News/<int:pk>',views.remove_news,name="remove_news"),
    path('User-Message',views.meeasges_send,name='meeasges_send'),
    path('Message',views.ad_message,name='ad_message'),
    path('Remove-Message/<int:pk>',views.remove_msg,name="remove_msg"),
    
    path('Testimonial',views.ad_testimonial,name='ad_testimonial'),
    path('Save-Testimonial',views.add_testimonial,name='add_testimonial'),
    path('Remove-Testimonial/<int:pk>',views.testi_remove,name="testi_remove"),
    

    
     
    
    path('edit_user/<int:pk>',views.edit_user,name="edit_user"),
    path('delete_user/<int:pk>',views.delete_user,name="delete_user"),
    path('msg',views.msg,name='msg'),
    path('msg_approve/<int:pk>/',views.msg_approve, name="msg_approve"),
    path('msg_reject/<int:pk>/',views.msg_reject, name="msg_reject"),
    path('regist',views.regist,name='regist'),
    path('regist_approve/<int:pk>/',views.regist_approve, name="regist_approve"),
    path('regist_reject/<int:pk>/',views.regist_reject, name="regist_reject"),
    path('delete_reg/<int:pk>',views.delete_reg,name="delete_reg"),
    path('enquir',views.enquir,name='enquir'),
    path('enquir_approve/<int:pk>/',views.enquir_approve, name="enquir_approve"),
    path('enquir_reject/<int:pk>/',views.enquir_reject, name="enquir_reject"),
    path('delete_enq/<int:pk>',views.delete_enq,name="delete_enq"),
    path('appl',views.appl,name='appl'),
    path('appl_approve/<int:pk>/',views.appl_approve, name="appl_approve"),
    path('appl_reject/<int:pk>/',views.appl_reject, name="appl_reject"),
    path('delete_apply/<int:pk>',views.delete_apply,name="delete_apply"),


    
    path('Enquery-check/<int:pk>',views.enq_check,name="enq_check"),
    path('Enquery-Reject/<int:pk>',views.enq_reject,name="enq_reject"),
    path('Enquery-Delete/<int:pk>',views.enq_delete,name="enq_delete"),
    
    path('Service/WhatsappMarketTools',views.whatsappmarkettools,name='whatsappmarkettools'),
    
    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    # -----------------------------------  ASHIKH VU (start)-----------------------------------
    path('change_theme/<str:theme>',views.change_theme,name='change_theme'),
    path('get_current_theme',views.get_current_theme,name='get_current_theme'),
    # -----------------------------------  ASHIKH VU (end)-----------------------------------

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
