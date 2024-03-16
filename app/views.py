
from django.shortcuts import redirect, render
from django.contrib import messages
from app.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from datetime import datetime

def handler404(request, exception):
    return render(request, '404.html', status=404)

# Create your views here.

def landingPage(request):
    if ThemeModel.objects.filter().exists():
        current_theme = ThemeModel.objects.last().theme_name
    else:
        current_theme = ''
    return render(request, 'landingpage.html',{'current_theme':current_theme})

def ex(request):
    return render(request, 'ex.html')

def base(request):
    return render(request, 'base.html')

def base2(request):
    return render(request, 'base2.html')
    
def home(request):
    testimo=Testimonial.objects.all()
    return render(request, 'index.html',{'testimo':testimo})


def text_page(request):
    testimo=Testimonial.objects.all()
    if ThemeModel.objects.filter().exists():
        current_theme = ThemeModel.objects.last().theme_name
    else:
        current_theme = ''
    return render(request,'Textpage.html',{'testimo':testimo,
                                           'current_theme':current_theme})

def vacancy(request):
    today = datetime.today()
    cour=courses.objects.all()
    vacan=Vacancys.objects.filter(last_date__gt=today).order_by('-id') 
    if ThemeModel.objects.filter().exists():
        current_theme = ThemeModel.objects.last().theme_name
    else:
        current_theme = ''
    return render(request, 'vacancy.html',{'vacan':vacan,'cour':cour,"current_theme":current_theme})

def contact(request):
    if ThemeModel.objects.filter().exists():
        current_theme = ThemeModel.objects.last().theme_name
    else:
        current_theme = ''
    return render(request, 'contact.html',{'current_theme':current_theme})
    
def course(request):
    return render(request, 'course.html')

def signin(request):
    return render(request, 'signin.html')

def aboutus(request):
    if ThemeModel.objects.filter().exists():
        current_theme = ThemeModel.objects.last().theme_name
    else:
        current_theme = ''
    return render(request, 'aboutus.html',{"current_theme":current_theme})

def service(request):
    if ThemeModel.objects.filter().exists():
        current_theme = ThemeModel.objects.last().theme_name
    else:
        current_theme = ''
    return render(request, 'service.html',{"current_theme":current_theme})

def core(request):
    if ThemeModel.objects.filter().exists():
        current_theme = ThemeModel.objects.last().theme_name
    else:
        current_theme = ''
    return render(request, 'core.html',{"current_theme":current_theme})

def events(request):
    allnews=Newsupdate.objects.all()
    allevents=Event.objects.all().order_by('-id')
    allimage=Gallery.objects.all()
    allimages=Gallery.objects.all()[4:]
    pos=Poster.objects.all().order_by('-id')
    if ThemeModel.objects.filter().exists():
        current_theme = ThemeModel.objects.last().theme_name
    else:
        current_theme = ''
    return render(request, 'events.html',{'allevents':allevents,'allnews':allnews,'allimage':allimage,'allimages':allimages,'pos':pos,"current_theme":current_theme})

def event_details(request,pk):
    allevents=Event.objects.get(id=pk)
    if ThemeModel.objects.filter().exists():
        current_theme = ThemeModel.objects.last().theme_name
    else:
        current_theme = ''
    return render(request, 'events_details.html',{'allevents':allevents,"current_theme":current_theme})
    

def meeasges_send(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        sub=request.POST['subject']
        mess=request.POST['message']
        sd=UserMessages(Name=name,Email=email,subj=sub,message=mess)
        sd.save()
        msg="We Will Contact You As Soon As Possible"
        return render(request,'contact.html',{'msg':msg})
    
def vacancy_contact(request):
    if request.method=='POST':
        name=request.POST['Name']
        email=request.POST['Email']
        sub=request.POST['Phone']
        mess=request.POST['place']
        sd=UserMessages(Name=name,Email=email,subj=sub,message=mess)
        sd.save()
        msg="We Will Contact You As Soon As Possible"
        return redirect('vacancy')

def job_appy(request):
    if request.method=='POST':
        job=Vacancy_Application()
        job.appli_name=request.POST['Name']
        job.appli_email=request.POST['Email']
        job.appli_phone=request.POST['Phone']
        vacn=Vacancys.objects.get(id=request.POST['jobname'])
        job.appli_job=vacn
        job.appli_loc=request.POST['plac']
        job.appli_resume=request.FILES.get('resume_file')
        job.appli_status=1
        job.save()
        today = datetime.today()
        vancy_success='Thank You For Apply. Our Team Will Contact You Soon.'
        vacan=Vacancys.objects.filter(last_date__gte=today).order_by('-id') 
        return render(request, 'vacancy.html',{'vacan':vacan,'vancy_success':vancy_success})



 # Technologies Pages

def ai(request):
    return render(request, 'tech/ai.html')
def dimen(request):
    return render(request, 'tech/3d.html')
def vr(request):
    return render(request, 'tech/vr.html')
def python(request):
    return render(request, 'tech/python.html')
def react(request):
    return render(request, 'tech/react.html')
def php(request):
    return render(request, 'tech/php.html')
def game(request):
    return render(request, 'tech/game.html')
def android(request):
    return render(request, 'tech/android.html')
def angular(request):
    return render(request, 'tech/angular.html')
def ml(request):
    return render(request, 'tech/ml.html')
def dm(request):
    return render(request, 'tech/dm.html')





def admin_login (request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
    
        
        if user is not None:
            request.session["uid"]=user.id
    
            auth.login(request,user)    
            application=apply.objects.all().count() 
            course=courses.objects.all().count()
            enq=enquery.objects.filter(status=0).count()
            jobapp=Vacancy_Application.objects.filter(appli_status=1).count()
            return render(request,'Admin/admin.html',{'application':application,'course':course,'enq':enq,'jobapp':jobapp})

        else:
            messages.info(request, 'Invalid Username or Password. Try Again.')
            return redirect('signin')
    else:
        return redirect('signin')



def dashboard(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        application=apply.objects.all().count()
        course=courses.objects.all().count()
        enq=enquery.objects.filter(status=0).count()
        jobapp=Vacancy_Application.objects.filter(appli_status=1).count()
        return render(request,'Admin/admin.html',{'application':application,'course':course,'enq':enq,'jobapp':jobapp})
    
    else:
        return redirect('signin')
    
def load_password(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        admin_data=User.objects.get(id=uid)
        return render(request,'Admin/adminpassword.html',{'admin_data':admin_data})

    else:
        return redirect('signin')
    
def add_password(request, user_id):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        user = User.objects.get(pk=user_id)
        user.username= request.POST.get('uname')
        password = request.POST.get('password')
        user.set_password(password)
        user.save()
        admin_data=User.objects.get(id=uid)
        msg='Password Changed'
        return render(request,'Admin/adminpassword.html',{'admin_data':admin_data,'msg':msg})

    else:
        return redirect('signin')



def course_application(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        course=apply.objects.all()
        return render(request,'Admin/admin_course_application.html',{'course':course})
    else:
        return redirect('signin')
    

def job_application(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        vacan=Vacancy_Application.objects.all()
        return render(request,'Admin/admin_job_application.html',{'vacan':vacan})
    else:
        return redirect('signin')

def ad_enquerys(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        enq=enquery.objects.all().order_by('-id')
        return render(request,'Admin/admin_enquery.html',{'enq':enq})
    else:
        return redirect('signin')

def enq_check(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        enq=enquery.objects.get(id=pk)
        enq.status=1
        enq.save()
        return redirect('ad_enquerys')
    else:
        return redirect('signin')

def enq_reject(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        enq=enquery.objects.get(id=pk)
        enq.status=2
        enq.save()
        return redirect('ad_enquerys')
    else:
        return redirect('signin')


def enq_delete(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        enq=enquery.objects.get(id=pk)
        enq.delete()
        return redirect('ad_enquerys')
    else:
        return redirect('signin')


def ad_course(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        cour=courses.objects.all()
        return render(request,'Admin/admin_course.html',{'cour':cour})
    else:
        return redirect('signin')

def add_course(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        if request.method =='POST':
            cour=courses(course_name=request.POST['course_name'],
                course_des=request.POST['course_dese'],
                course_vacancy=request.POST['course_vacancy'],
                rating=request.POST['course_rating'],
                course_img=request.FILES.get('course_img')
                )
            cour.save()
            messages.info(request, 'Succesfully Added !')
            cour=courses.objects.all()
            return render(request,'Admin/admin_course.html',{'cour':cour})
    else:
        return redirect('signin') 


def edit_course_save(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        if request.method =='POST':
            img=request.FILES.get('edit_course_img')
            cour=courses.objects.get(id=pk)
            cour.course_name=request.POST['edit_course_name']
            cour.course_des=request.POST['edit_course_dese']
            cour.course_vacancy=request.POST['edit_course_vacancy']
            cour.rating=request.POST['edit_course_rating']
            if img:
                cour.course_img=img
            else:
                cour.course_img=cour.course_img
            messages.info(request, 'Succesfully Edited !')
            cour.save()

            return redirect('ad_course')
    else:
        return redirect('signin')

def remove_course(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        cour=courses.objects.get(id=pk)
        cour.delete()
        cour=courses.objects.all()
        messages.info(request, 'Succesfully Remove !')
        return redirect('ad_course')
    else:
        return redirect('signin')

def ad_events(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        allevents=Event.objects.all().order_by('-id')
        return render(request,'Admin/admin_events.html',{'allevents':allevents})
    else:
        return redirect('signin')

def add_event(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        if request.method =='POST':
            evnt=Event(ev_head=request.POST['ev_head'],
                ev_des=request.POST['ev_dese'],
                ev_des1=request.POST['ev_dese1'],
                ev_des2=request.POST['ev_dese2'],
                ev_des3=request.POST['ev_dese3'],
                ev_img=request.FILES.get('ev_img'))
            evnt.save()
            allevents=Event.objects.all().order_by('-id')
            messages.info(request, 'Succesfully Added !')
            return render(request,'Admin/admin_events.html',{'allevents':allevents})
    else:
        return redirect('signin')
  
def event_remove(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        event=Event.objects.get(id=pk)
        event.delete()
        messages.info(request, 'Succesfully Deleted !')
        return redirect('ad_events')
    else:
        return redirect('signin')
    

def jobs(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        
        today = datetime.today()
        vacan=Vacancys.objects.filter(last_date__lt=today).order_by('-id') 
        for i in vacan:
            i.job_status=2
            i.save()
        vacan=Vacancys.objects.all().order_by('-id') 
        return render(request,'Admin/admin_jobs.html',{'vacan':vacan})   


def ad_gallery(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        imags=Gallery.objects.all().order_by('-id') 
        return render(request,'Admin/admin_gallery.html',{'imags':imags})
    else:
        return redirect('signin')
    


def ad_poster(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        pos=Poster.objects.all().order_by('-id') 
        return render(request,'Admin/admin_poster.html',{'pos':pos})
    else:
        return redirect('signin')
    

def add_poster(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        if request.method =='POST':
            evnt=Poster(ps_head=request.POST['pos_head'],
                ps_des=request.POST['pos_dese'],
                ps_des2=request.POST['pos_dese2'],
                ps_des3=request.POST['pos_dese3'],
                ps_img=request.FILES.get('pos_img'))
            evnt.save()
            pos=Poster.objects.all().order_by('-id')
            messages.info(request, 'Succesfully Added !')
            return render(request,'Admin/admin_poster.html',{'pos':pos})
    else:
        return redirect('signin')
    

        
def poster_remove(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        pos=Poster.objects.get(id=pk)
        pos.delete()
        messages.info(request, 'Succesfully Deleted !')
        return redirect('ad_poster')
    else:
        return redirect('signin')


def add_images(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        if request.method =='POST':
            gla_img=request.FILES.getlist('gal_img')
            for img in gla_img:
                img_save=Gallery(gallery_img=img)
                img_save.save()
        
            imags=Gallery.objects.all().order_by('-id')
            messages.info(request, 'Successfully Added !')      
            return render(request,'Admin/admin_gallery.html',{'imags':imags})
    else:
        return redirect('signin')


def add_vacancy(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        if request.method =='POST':
            vac=Vacancys()
            vac.loc=request.POST['jloc']
            vac.post_name=request.POST['jname']
            vac.post_disc=request.POST['jdisc']
            vac.qualific=request.POST['jquali']
            vac.type_job=request.POST['jtype']
            vac.last_date=request.POST['jldate']
            vac.job_status=1
            vac.save()

            messages.info(request, 'Successfully Added !')      
            vacan=Vacancys.objects.all().order_by('-id') 
            return render(request,'Admin/admin_jobs.html',{'vacan':vacan})   
    else:
        return redirect('signin')
    

def edit_vacany(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        vanc=Vacancys.objects.get(id=pk)
        return render(request,'Admin/admin_jobs_edit.html',{'vanc':vanc})   
    else:
        return redirect('signin')
    

def editsave_vacancy(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        if request.method =='POST':
            vac=Vacancys.objects.get(id=pk)
            vac.loc=request.POST['jloc']
            vac.post_name=request.POST['jname']
            vac.post_disc=request.POST['jdisc']
            vac.qualific=request.POST['jquali']
            vac.type_job=request.POST['jtype']
            vac.last_date=request.POST['jldate']
            vac.job_status=1
            vac.save()

            messages.info(request, 'Successfully Edited !')      
            vacan=Vacancys.objects.all().order_by('-id') 
            return render(request,'Admin/admin_jobs.html',{'vacan':vacan})   
    else:
        return redirect('signin')
    
    
    
def remove_vacany(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        vanc=Vacancys.objects.get(id=pk)
        vanc.delete()
        messages.info(request, 'Succesfully Deleted !')
        return redirect('jobs')
    else:
        return redirect('signin')


def image_remove(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        img=Gallery.objects.get(id=pk)
        img.delete()
        messages.info(request, 'Succesfully Deleted !')
        return redirect('ad_gallery')
    else:
        return redirect('signin')


def ad_News(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        allnews=Newsupdate.objects.all().order_by('-id') 
        return render(request,'Admin/admin_news.html',{'allnews':allnews})
    else:
        return redirect('signin')

def add_news(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        if request.method =='POST':
            a=Newsupdate(news_text=request.POST['news_txt'])
            a.save()
            messages.info(request, 'Succesfully Added !')
            allnews=Newsupdate.objects.all().order_by('-id') 
            return render(request,'Admin/admin_news.html',{'allnews':allnews})
    else:
        return redirect('signin')


def remove_news(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        a=Newsupdate.objects.get(id=pk)
        a.delete()
        messages.info(request, 'Succesfully Deleted !')
        return redirect('ad_News')
    else:
        return redirect('signin')

def ad_message(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        msges=UserMessages.objects.all().order_by('-id')
        return render(request,'Admin/admin_message.html',{'msges':msges})
    else:
        return redirect('signin')
    
def remove_msg(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        msg_dele=UserMessages.objects.get(id=pk)
        msg_dele.delete()

        msges=UserMessages.objects.all().order_by('-id')
        return render(request,'Admin/admin_message.html',{'msges':msges})
    else:
        return redirect('signin')


def ad_testimonial(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        testimo=Testimonial.objects.all().order_by('-id')
        return render(request,'Admin/admin_testimonial.html',{'testimo':testimo})
    else:
        return redirect('signin')

def add_testimonial(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        if request.method =='POST':
            a=Testimonial(testi_name=request.POST['tsti_name'],
                testi_des=request.POST['tsti_desig'],
                testi_desecri=request.POST['tsti_dese'],
                testi_img=request.FILES.get('testi_img'))
            a.save()
            testimo=Testimonial.objects.all().order_by('-id')
            messages.info(request, 'Succesfully Added !')
            return render(request,'Admin/admin_testimonial.html',{'testimo':testimo})
    else:
        return redirect('signin')

def testi_remove(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        a=Testimonial.objects.get(id=pk)
        a.delete()
        messages.info(request, 'Succesfully Deleted !')
        testimo=Testimonial.objects.all().order_by('-id')
        return redirect('ad_testimonial')
    else:
        return redirect('signin')

def job_appl_approve(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        vacan=Vacancy_Application.objects.get(id=pk)
        vacan.appli_status=2
        vacan.save()
        return redirect('job_application')
    else:
        return redirect('signin')
    
def job_appl_reject(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        vacan=Vacancy_Application.objects.get(id=pk)
        vacan.appli_status=0
        vacan.save()
        return redirect('job_application')
    else:
        return redirect('signin')

def job_appl_delete(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        vacan=Vacancy_Application.objects.get(id=pk)
        vacan.delete()
        return redirect('job_application')
    else:
        return redirect('signin')


def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('text_page')

def add_user(request):
    if request.method=='POST':
        uname=request.POST['Name']
        
        uemail=request.POST['Email']
        uphone=request.POST['Phone']
        umsg=request.POST['massage']

        u=userdata(Name=uname,massage=umsg,Email=uemail,Phone=uphone)
       
    if userdata.objects.filter(Email=uemail).exists():
                messages.error(request, 'Email already exists!!!!!!')
                return redirect('contact') 
    else:
        messages.success(request,'Thank you for contacting us.We will try to reach you as soona as possible... ')

    

    u.save()
        
       
    return redirect('contact')

@login_required(login_url='user_login')
def msg(request):
    msg=userdata.objects.all()
    
    return render(request,'msg.html',{'u':msg})

def msg_approve(request,pk):
    leave = userdata.objects.get(id=pk)
    leave.status = 1
    leave.save()
    return redirect('msg')

def msg_reject(request, pk):
    leave =  userdata.objects.get(id=pk)
    leave.status = 2
    leave.save()
    return redirect('msg')

    

@login_required(login_url='user_login')
def edit_user(request,pk):
    if request.method=="POST":
        msg=userdata.objects.get(id=pk)
        msg.Name=request.POST['Name']
        msg.Email=request.POST['Email']
        msg.Phone=request.POST['Phone']
        msg.massage=request.POST['massage']
        msg.save()
        return redirect('msg')
 
#@login_required(login_url='user_login')
#def delete_user(request,pk):
 #   msg=userdata.objects.get(id=pk)
 #   msg.delete()
 #   return redirect('msg')
@login_required(login_url='signin')
def delete_user(request,pk):
    u=userdata.objects.get(id=pk)
    u.delete()
    return redirect('msg')  


    
def reg(request):
    if request.method=='POST':
        uname=request.POST['Name']
        udate=request.POST['date']
        uemail=request.POST['Email']
        uphone=request.POST['Phone']
        umsg=request.POST['message']


        
        user=register(Name=uname,message=umsg,Email=uemail,Phone=uphone,date=udate)
       
    if register.objects.filter(Email=uemail).exists():
                messages.error(request, 'Email already exists!!!!!!')
                return redirect('course') 
    else:
         messages.success(request,'You have registered successfully ')
    

    user.save()
        
       
    return redirect('course') 

@login_required(login_url='signin')
def regist(request):
    msg=register.objects.all()
    return render(request,'regist.html',{'user':msg})

@login_required(login_url='signin')
def regist_approve(request,pk):
    leave = register.objects.get(id=pk)
    leave.status = 1
    leave.save()
    return redirect('regist')

@login_required(login_url='signin')
def regist_reject(request, pk):
    leave =  register.objects.get(id=pk)
    leave.status = 2
    leave.save()
    return redirect('regist')


@login_required(login_url='signin')
def delete_reg(request,pk):
    user=register.objects.get(id=pk)
    user.delete()
    return redirect('regist')  


def enquerys(request):
    if request.method=='POST':
        uname=request.POST['Name']
        uemail=request.POST['Email']
        uphone=request.POST['Phone']
        uproject=request.POST['project']
        umsg=request.POST['message']

        enq=enquery(Name=uname,Email=uemail,Phone=uphone,message=umsg,project=uproject)
        enq.save()
        messages.success(request,'Thank you for your enquiry....')
        return redirect('text_page') 
    else:
        return render(request,'Textpage.html') 

@login_required(login_url='signin')
def enquir(request):
    msg=enquery.objects.all()
    return render(request,'enquir.html',{'user':msg})

def enquir_approve(request,pk):
    leave = enquery.objects.get(id=pk)
    leave.status = 1
    leave.save()
    return redirect('enquir')

def enquir_reject(request, pk):
    leave =  enquery.objects.get(id=pk)
    leave.status = 2
    leave.save()
    return redirect('enquir')


@login_required(login_url='user_login')
def delete_enq(request,pk):
    user=enquery.objects.get(id=pk)
    user.delete()
    return redirect('enquir')  


def app(request):
    if request.method=='POST':
        ucourse=request.POST['course']
        uname=request.POST['Name']
        uemail=request.POST['Email']
        uphone=request.POST['Phone']
        uplace=request.POST['place']


        
        user=apply(Name=uname,place=uplace,Email=uemail,Phone=uphone,course=ucourse)
       
    if apply.objects.filter(Email=uemail).exists():
                messages.error(request, 'Email already exists!!!!!!')
                return redirect('vacancy') 
    else:
         messages.success(request,'APPLICATION RECIEVED....')
    

    user.save()
        
       
    return redirect('vacancy') 

@login_required(login_url='user_login')
def appl(request):
    msg=apply.objects.all()
    return render(request,'appl.html',{'user':msg})

@login_required(login_url='signin')
def appl_approve(request,pk):
    leave = apply.objects.get(id=pk)
    leave.status = 1
    leave.save()
    return redirect('course_application')

@login_required(login_url='signin')
def appl_reject(request, pk):
    leave =  apply.objects.get(id=pk)
    leave.status = 2
    leave.save()
    return redirect('course_application')

@login_required(login_url='signin')
def delete_apply(request,pk):
    user=apply.objects.get(id=pk)
    user.delete()
    return redirect('course_application')  


def whatsappmarkettools(request):
    if ThemeModel.objects.filter().exists():
        current_theme = ThemeModel.objects.last().theme_name
    else:
        current_theme = ''
    return render(request, 'whatsappmarkettools.html',{"current_theme":current_theme})

# ----------------------------------------- ASHIKH VU (start) -----------------------------------

def change_theme(request,theme):
    if not ThemeModel.objects.all().exists():
        new_theme = ThemeModel(theme_name='default')
        new_theme.save()
    if(theme == 'default'):
        new_theme = ThemeModel.objects.first()
        new_theme.theme_name = 'default'
        new_theme.save()
    elif(theme == 'xmas'):
        new_theme = ThemeModel.objects.first()
        new_theme.theme_name = 'xmas'
        new_theme.save()
    elif(theme == 'onam'):
        new_theme = ThemeModel.objects.first()
        new_theme.theme_name = 'onam'
        new_theme.save()
    elif(theme == 'diwali'):
        new_theme = ThemeModel.objects.first()
        new_theme.theme_name = 'diwali'
        new_theme.save()
    elif(theme == 'pongal'):
        new_theme = ThemeModel.objects.first()
        new_theme.theme_name = 'pongal'
        new_theme.save()
    elif(theme == 'vishu'):
        new_theme = ThemeModel.objects.first()
        new_theme.theme_name = 'vishu'
        new_theme.save()
    elif(theme == 'easter'):
        new_theme = ThemeModel.objects.first()
        new_theme.theme_name = 'easter'
        new_theme.save()
    elif(theme == 'republic'):
        new_theme = ThemeModel.objects.first()
        new_theme.theme_name = 'republic'
        new_theme.save()
    elif(theme == 'ramadan'):
        new_theme = ThemeModel.objects.first()
        new_theme.theme_name = 'ramadan'
        new_theme.save()
    return redirect('dashboard')

from django.http import JsonResponse

def get_current_theme(request):
    get_theme = ThemeModel.objects.last()
    data = {'current_theme':f'{get_theme.theme_name}'}
    return JsonResponse(data)
# ----------------------------------------- ASHIKH VU (end) -------------------------------------