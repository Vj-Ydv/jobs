"""
Views that can used by developer for easily export resume as PDF.
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from curriculum import export
from curriculum import models
from curriculum.models import Resume,ProjectItem,SkillItem,CertificationItem,Training,Experience
from accounts.models import User
from django.template.loader import get_template
from curriculum.forms import LanguageForm, LanguageItemForm, ResumeForm, SkillForm, SkillItemForm, CertificationForm, CertificationItemForm, ExperienceForm, ProjectForm, ProjectItemForm, TrainingForm, UpdateResumeForm, UpdateTrainingForm, UpdateSkillitemForm, UpdateSkillForm, UpdateProjectitemForm, UpdateProjectForm, UpdateLanguageitemForm, UpdateLanguageForm, UpdateExperienceForm, UpdateCertificationitemForm, UpdateCertificationForm

from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

def export_single_page(request):
    """Get a resume in a single page PDF."""
    #resume = get_object_or_404(Resume.objects.filter(firstname='Vijay'))
    current_user=request.user
    pdf, result = export.export_pdf(current_user, export.single_page)
    raw_pdf = result.getvalue()
    if not pdf.err:
        return HttpResponse(raw_pdf, content_type='application/pdf')
    return HttpResponse('We had some errors.')

def export_classic(request):
    """Get a resume in a PDF with classic format."""
    #resume = get_object_or_404(Resume.objects.filter(id=resume_id))
    #resume = get_object_or_404(Resume.objects.filter(user=request.user))
    current_user=request.user
    pdf, result = export.export_pdf(current_user, export.classic)
    raw_pdf = result.getvalue()
    if not pdf.err:
        return HttpResponse(raw_pdf, content_type='application/pdf')
    return HttpResponse('We had some errors.')


def export_classic2(request):
    """Get a resume in a PDF with classic format."""
    #resume = get_object_or_404(Resume.objects.filter(id=resume_id))
    #resume = get_object_or_404(Resume.objects.filter(user=request.user))
    current_user=request.user
    pdf, result = export.export_pdf(current_user, export.classic2)
    raw_pdf = result.getvalue()
    if not pdf.err:
        return HttpResponse(raw_pdf, content_type='application/pdf')
    return HttpResponse('We had some errors.')

def export_classic1(request):
    """Get a resume in a PDF with classic format."""
    #resume = get_object_or_404(Resume.objects.filter(id=resume_id))
    #resume = get_object_or_404(Resume.objects.filter(firstname='Vijay'))
    current_user=request.user
    pdf, result = export.export_pdf(current_user, export.classic1)
    raw_pdf = result.getvalue()
    if not pdf.err:
        return HttpResponse(raw_pdf, content_type='application/pdf')
    return HttpResponse('We had some errors.')


def export_class(request):
    """
    Create a classic resume in :mod:`xhtml2pdf` format.
    """
    resume = get_object_or_404(Resume.objects.filter(user=request.user))
    #resume=Resume.objects.get(firstname=first_name)
    current_user = request.user
    context = {
        'pagesize': 'a4',
        'resume': resume,
        'skills': current_user.skills.order_by('category'),
        'projects': current_user.projects.order_by('-weight'),
        'experiences': current_user.experiences.order_by('-start_year'),
        'trainings': current_user.trainings.order_by('-start_year', '-start_month'),
        'certifications': current_user.certifications.order_by('-end_year', '-end_month'),
    }
   # return get_template('curriculum/test1.html').render(context)
    return render(request,'curriculum/cvpreview.html',context)

"""
def skillitem(request):
    if request.method=="POST":
        form=ExperienceForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect()
            except:
                pass
    else:
        form=ExperienceForm()
    return render(request,"producttemp.html",{'form':form})
"""

def addlanguage(request):
    form=LanguageForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, f'Your account has been updated!')
        return redirect('curriculum:languageitem')

    context={
        'form':form,
        'language_active':"active"
    }
    return render(request,"curriculum/language.html",context)

def addlanguageitem(request):
    form=LanguageItemForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.resume= Resume.objects.get(user=request.user)
        instance.save()
        messages.success(request, f'Your account has been updated!')
        return redirect('curriculum:languageitem')

    context={
        'form':form,
        'languageitem_active':"active"
    }
    return render(request,"curriculum/languageitem.html",context)

#@login_required(login_url="")
def addresume(request):
    form=ResumeForm(request.POST or None, request.FILES)
    obj=User.objects.filter(email=request.user)
    # instance.user=request.user
    try:
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            # print(instance.user)
            instance.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('curriculum:training')

        context={
            'form':form,
            'obj':obj,
            'resume_active':"active"
        }
        return render(request,"curriculum/resume.html",context)
    except IntegrityError:
        return HttpResponse("ERROR!!! Go to update resume to change information")







def addskill(request):
    form=SkillForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, f'Your account has been updated!')
        return redirect('curriculum:skillitem')

    context={
        'form':form,
        'skill_active':"active"
    }
    return render(request,"curriculum/skill.html",context)

def addskillitem(request):
    form=SkillItemForm(request.POST or None, request.FILES)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.resume= Resume.objects.get(user=request.user)
        instance.save()
        messages.success(request, f'Your account has been updated!')
        return redirect('curriculum:experience')

    context={
        'form':form,
        'skillitem_active':"active"
    }
    return render(request,"curriculum/skillitem.html",context)

def addcertification(request):
    form=CertificationForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, f'Your account has been updated!')
        return redirect('curriculum:certificationitem')

    context={
        'form':form,
        'certification_active':"active"
    }
    return render(request,"curriculum/certification.html",context)

def addcertificationitem(request):
    form=CertificationItemForm(request.POST or None, request.FILES)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.resume= Resume.objects.get(user=request.user)
        instance.save()
        messages.success(request, f'Your account has been updated!')
        return redirect('curriculum:language')

    context={
        'form':form,
        'certificationitem_active':"active"
    }
    return render(request,"curriculum/certificationitem.html",context)

def addexperience(request):
    form=ExperienceForm(request.POST or None, request.FILES)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.resume= Resume.objects.get(user=request.user)
        instance.save()
        messages.success(request, f'Your account has been updated!')
        return redirect('curriculum:certification')

    context={
        'form':form,
        'experience_active':"active"
    }
    return render(request,"curriculum/experience.html",context)

def addproject(request):
    form=ProjectForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, f'Your account has been updated!')
        return redirect('curriculum:projectitem')

    context={
        'form':form,
        'project_active':"active"
    }
    return render(request,"curriculum/project.html",context)

def addprojectitem(request):
    form=ProjectItemForm(request.POST or None, request.FILES)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.resume= Resume.objects.get(user=request.user)
        instance.save()
        messages.success(request, f'Your account has been updated!')
        return redirect('curriculum:skill')

    context={
        'form':form,
        'projectitem_active':"active"
    }
    return render(request,"curriculum/projectitem.html",context)

def addtraining(request):
    form=TrainingForm(request.POST or None, request.FILES)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.resume= Resume.objects.get(user=request.user)
        instance.save()
        messages.success(request, f'Your account has been updated!')
        return redirect('curriculum:project')

    context={
        'form':form,
        'training_active':"active"
    }
    return render(request,"curriculum/training.html",context)

def menulist(request,*args,**kwargs):
    return render(request,"resume_base.html",{})


def resume_generate(request,*args,**kwargs):
    return render(request,"curriculum/resume_generate.html",{})


# def fullResume(request,*args,**kwargs):
#     resume_form=ResumeForm(request.POST or None, request.FILES)
#     skill_form=SkillForm(request.POST or None, request.FILES)
#     project_form=ProjectForm(request.POST or None, request.FILES)
#     # resume_form.fields["firstname"].queryset = User.objects.filter(id=1)
#     obj=User.objects.filter(email=request.user)
#     print(request.user)
#     print(obj)
    
#     context = {
#         'r_form':resume_form,
#         's_form':skill_form,
#         'p_form':project_form,
#         'obj':obj
#     }

#     return render(request, 'curriculum/profile.html', context)



def fullResume(request,*args,**kwargs):
    resume_form=UpdateResumeForm(request.POST or None, request.FILES,instance=request.user)
    # skill_form=SkillForm(request.POST or None, request.FILES)
    # project_form=ProjectForm(request.POST or None, request.FILES)
    # # resume_form.fields["firstname"].queryset = User.objects.filter(id=1)
    # obj=User.objects.filter(email=request.user)
    # print('sss')
    # print(obj.id)
    # print(obj)
    
    context = {
        'r_form':resume_form,
        's_form':skill_form,
        'p_form':project_form,
        # 'obj':obj
    }

    return render(request, 'curriculum/profile.html', context)




class EditProfileView(UpdateView):
    model = models.Resume
    form_class = UpdateResumeForm
    context_object_name = 'resume'
    template_name = 'curriculum/update/profile.html'
    success_url = reverse_lazy('curriculum:updateResume')

    # @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        # obj = self.request.user
        # obj = models.Resume.objects.filter(pk=self.kwargs['user_id'])
        obj = models.Resume.objects.filter(user=self.request.user)



        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj.first()





class EditTrainingView(UpdateView):
    model = models.Training
    form_class = UpdateTrainingForm
    # context_object_name = 'resume'
    template_name = 'curriculum/update/training.html'
    success_url = reverse_lazy('curriculum:updateResume')

    # @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        # obj = self.request.user
        # obj = models.Resume.objects.filter(pk=self.kwargs['user_id'])
        obj = models.Training.objects.filter(user=self.request.user)
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj.first()



class EditSkillView(UpdateView):
    model = models.Skill
    form_class = UpdateSkillForm
    # context_object_name = 'resume'
    template_name = 'curriculum/update/skill.html'
    success_url = reverse_lazy('curriculum:updateResume')

    # @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        # obj = self.request.user
        # obj = models.Resume.objects.filter(pk=self.kwargs['user_id'])
        obj = models.Skill.objects.filter(user=self.request.user)
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj.first()


class EditSkillitemView(UpdateView):
    model = models.Skill
    form_class = UpdateSkillitemForm
    # context_object_name = 'resume'
    template_name = 'curriculum/update/skillitem.html'
    success_url = reverse_lazy('curriculum:updateResume')

    # @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        # obj = self.request.user
        # obj = models.Resume.objects.filter(pk=self.kwargs['user_id'])
        obj = models.Skill.objects.filter(user=self.request.user)
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj.first()




class EditProjectView(UpdateView):
    model = models.Project
    form_class = UpdateProjectForm
    # context_object_name = 'resume'
    template_name = 'curriculum/update/project.html'
    success_url = reverse_lazy('curriculum:updateResume')

    # @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        # obj = self.request.user
        # obj = models.Resume.objects.filter(pk=self.kwargs['user_id'])
        obj = models.Project.objects.filter(user=self.request.user)
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj.first()




class EditProjectitemView(UpdateView):
    model = models.ProjectItem
    form_class = UpdateProjectitemForm
    # context_object_name = 'resume'
    template_name = 'curriculum/update/projectitem.html'
    success_url = reverse_lazy('curriculum:updateResume')

    # @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        # obj = self.request.user
        # obj = models.Resume.objects.filter(pk=self.kwargs['user_id'])
        obj = models.ProjectItem.objects.filter(user=self.request.user)
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj.first()



class EditLanguageView(UpdateView):
    model = models.Language
    form_class = UpdateLanguageForm
    # context_object_name = 'resume'
    template_name = 'curriculum/update/language.html'
    success_url = reverse_lazy('curriculum:updateResume')

    # @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        # obj = self.request.user
        # obj = models.Resume.objects.filter(pk=self.kwargs['user_id'])
        obj = models.Language.objects.filter(user=self.request.user)
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj.first()



class EditLanguageitemView(UpdateView):
    model = models.LanguageItem
    form_class = UpdateLanguageitemForm
    # context_object_name = 'resume'
    template_name = 'curriculum/update/languageitem.html'
    success_url = reverse_lazy('curriculum:updateResume')

    # @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        # obj = self.request.user
        # obj = models.Resume.objects.filter(pk=self.kwargs['user_id'])
        obj = models.LanguageItem.objects.filter(user=self.request.user)
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj.first()



class EditExperienceView(UpdateView):
    model = models.Experience
    form_class = UpdateExperienceForm
    # context_object_name = 'resume'
    template_name = 'curriculum/update/experience.html'
    success_url = reverse_lazy('curriculum:updateResume')

    # @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        # obj = self.request.user
        # obj = models.Resume.objects.filter(pk=self.kwargs['user_id'])
        obj = models.Experience.objects.filter(user=self.request.user)
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj.first()



class EditCertificationView(UpdateView):
    model = models.Certification
    form_class = UpdateCertificationForm
    # context_object_name = 'resume'
    template_name = 'curriculum/update/certification.html'
    success_url = reverse_lazy('curriculum:updateResume')

    # @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        # obj = self.request.user
        # obj = models.Resume.objects.filter(pk=self.kwargs['user_id'])
        obj = models.Certification.objects.filter(user=self.request.user)
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj.first()



class EditCertificationitemView(UpdateView):
    model = models.Certification
    form_class = UpdateCertificationitemForm
    # context_object_name = 'resume'
    template_name = 'curriculum/update/certificationitem.html'
    success_url = reverse_lazy('curriculum:updateResume')

    # @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        # obj = self.request.user
        # obj = models.Resume.objects.filter(pk=self.kwargs['user_id'])
        obj = models.CertificationItem.objects.filter(user=self.request.user)
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj.first()

