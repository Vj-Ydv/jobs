from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from .views import *


app_name = "curriculum"

urlpatterns = [
    
    path('classic/',export_classic,name='classic'),
    path('classic1/',export_classic1,name='classic1'),
    path('modern/',export_single_page,name='modern'),
    #path('htmltest/<str:first_name>/',export_class,name='test'),
    path('viewCV/',export_class,name='viewCV'),
    path('htmltest/',export_classic2,name='test'),

    path('language/',addlanguage,name='language'),
    path('languageitem/',addlanguageitem,name='languageitem'),
    path('resume/',addresume,name='resume'),
    path('skill/',addskill,name='skill'),
    path('skillitem/',addskillitem,name='skillitem'),
    path('certification/',addcertification,name='certification'),
    path('certificationitem/',addcertificationitem,name='certificationitem'),
    path('experience/',addexperience,name='experience'),
    path('project/',addproject,name='project'),
    path('projectitem/',addprojectitem,name='projectitem'),
    path('training/',addtraining,name='training'),
    path('cv/',resume_generate,name='resume_generate'),
    path('edit_profile/',menulist,name='showmenu'),
    path('updateresume/',EditProfileView.as_view(),name='updateResume'),
    path('updatetraining/',EditTrainingView.as_view(),name='updatetraining'),
    path('updateskill',EditSkillView.as_view(),name='updateskill'),
    path('updateskillitem',EditSkillitemView.as_view(),name='updateskillitem'),
    path('updateproject',EditProjectView.as_view(),name='updateproject'),
    path('updateprojectitem',EditProjectitemView.as_view(),name='updateprojectitem'),
    path('updatecertification',EditCertificationView.as_view(),name='updatecertification'),
    path('updatelanguage',EditLanguageView.as_view(),name='updatelanguage'),
    path('updatelanguageitem',EditLanguageitemView.as_view(),name='updatelanguageitem'),
    path('updateexperience',EditExperienceView.as_view(),name='updateexperience'),
    path('updatecertificationitem',EditCertificationitemView.as_view(),name='updatecertificationitem'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)