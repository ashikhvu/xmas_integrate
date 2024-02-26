from datetime import date
from django.db import models

# Create your models here.

class userdata(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    Phone = models.CharField(max_length=12)
    massage =  models.CharField(max_length=255)
    status = models.IntegerField(default=0)

class register(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    Phone = models.CharField(max_length=12)
    date   = models.CharField(max_length=20)
    message =  models.CharField(max_length=255)
    status = models.IntegerField(default=0)

class enquery(models.Model):
    Name = models.CharField(max_length=255)
    enq_date=models.DateField(auto_now_add=True,null=True)
    Email = models.EmailField()
    Phone = models.CharField(max_length=12)
    project = models.CharField(max_length=255)
    message =  models.CharField(max_length=255)
    status = models.IntegerField(default=0)

class apply(models.Model):
    course = models.CharField(max_length=255)
    apply_date=models.DateField(auto_now_add=True,null=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    Phone = models.CharField(max_length=12)
    place =  models.CharField(max_length=255)
    status = models.IntegerField(default=0)

#courses

class courses(models.Model):
    course_name=models.CharField(max_length=255)
    course_des=models.TextField()
    course_img=models.FileField(upload_to='course')
    course_cre_date=models.DateField(auto_now_add=True,null=True)
    course_vacancy=models.IntegerField(default=0)
    rating=models.IntegerField(default=0)

class Event(models.Model):
    ev_head=models.CharField(max_length=255)
    ev_des=models.TextField(default='')
    ev_des1=models.TextField(default='')
    ev_des2=models.TextField(default='')
    ev_des3=models.TextField(default='')
    ev_img=models.FileField(upload_to='events')
    event_cre_date=models.DateField(auto_now_add=True,null=True)

class Poster(models.Model):
    ps_head=models.CharField(max_length=255)
    ps_des=models.TextField(default='')
    ps_des2=models.TextField(default='')
    ps_des3=models.TextField(default='')
    ps_img=models.FileField(upload_to='events')
    ps_cre_date=models.DateField(auto_now_add=True,null=True)



class Gallery(models.Model):
    gallery_img=models.FileField(upload_to='events')
    img_cre_date=models.DateField(auto_now_add=True,null=True)

class Newsupdate(models.Model):
    news_text=models.TextField()
    news_cre_date=models.DateField(auto_now_add=True,null=True)


class UserMessages(models.Model):
   
    send_date=models.DateField(auto_now_add=True,null=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    subj = models.CharField(max_length=150)
    message =  models.CharField(max_length=255)
    send_status = models.IntegerField(default=0)

class Testimonial(models.Model):
    testi_name=models.CharField(max_length=255)
    testi_des=models.CharField(max_length=255)
    testi_img=models.FileField(upload_to='testimonial')
    testi_cre_date=models.DateField(auto_now_add=True,null=True)
    testi_desecri=models.TextField()

class Vacancys(models.Model):
    loc=models.CharField(max_length=255,default='')
    post_name=models.CharField(max_length=255,default='')
    post_disc=models.TextField(default='')
    qualific=models.CharField(max_length=255,default='')
    type_job=models.CharField(max_length=150,default='')
    last_date=models.DateField(auto_now_add=False,null=True)
    created_date=models.DateField(auto_now_add=True,null=True)
    job_status=models.CharField(max_length=150,default=0)

class Vacancy_Application(models.Model):
    appli_loc=models.CharField(max_length=255,default='')
    appli_name=models.CharField(max_length=255,default='')
    appli_email=models.TextField(default='')
    appli_phone=models.CharField(max_length=255,default='')
    appli_job=models.ForeignKey(Vacancys, on_delete=models.CASCADE, null=True,default='')
    appli_date=models.DateField(auto_now_add=True,null=True)
    appli_resume=models.FileField(upload_to='resume', default='')
    appli_status=models.CharField(max_length=150,default=0)

class ThemeModel(models.Model):
    theme_name = models.CharField(max_length=255,default="default")
