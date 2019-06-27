from django.contrib import admin
from django.urls import path, include
from accounts.views import activate
from django.contrib.auth import views as auth_views
from curriculum.views import export_single_page, export_classic, export_class,export_classic1, addlanguage,addlanguageitem,addresume, addskill, addskillitem, addcertification, addcertificationitem, addexperience, addproject, addprojectitem, addtraining, menulist



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobsapp.urls')),
    path('', include('accounts.urls')),
    



    path('employee/', include('curriculum.urls')),





    path('activate/<uidb64>/<token>',
        activate, name='activate'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password/password_reset.html'
         ),
         name='password-reset'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password/password_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]
