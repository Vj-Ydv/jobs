from django.contrib import admin
from curriculum import models, forms
from curriculum.admin import actions


class ResumeAdmin(admin.ModelAdmin):
    actions = (actions.export_resume,)
    list_display = ('firstname', 'lastname', 'title')
    fieldsets = (
        (None, {
            'fields': (
                ('firstname', 'lastname', 'title'),
                ('user', 'image'),
                ('phone', 'email', 'website'),
                ('country', 'city'),
                
                ( 'skype', 'stackoverflow', 'github'),
                ('hobbies'),
                
            )
        }),
    )


class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'authority')
    fieldsets = (
        (None, {
            'fields': (
                ('title', 'authority', 'url'),
                
            )
        }),
    )


class CertificationItemAdmin(admin.ModelAdmin):
    list_display = ('certification', 'user')
    fieldsets = (
        (None, {
            'fields': (
                'user',
                'certification',
                ('end_year', 'end_month'),
            )
        }),
    )


class ExperienceAdmin(admin.ModelAdmin):
    form = forms.ExperienceForm
    list_display = ('title', 'entreprise', 'start_year', 'start_month',
                    'end_year', 'end_month',
                    'user')
    fieldsets = (
        (None, {
            'fields': (
                'user',
                ('title', 'entreprise', 'type'),
                'description',
                ('start_year', 'start_month', 'still'),
                ('end_year', 'end_month'),
                
            )
        }),
    )


class LanguageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name',
            )
            
        }),
    )


class LanguageItemAdmin(admin.ModelAdmin):
    list_display = ('language', 'level', 'user')
    fieldsets = (
        (None, {
            'fields': (
                'user',
                ('language', 'level'),
            )
        }),
    )


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    fieldsets = (
        (None, {
            'fields': (
                ('title', 'url'),
                'description',
            )
        }),
    )


class ProjectItemAdmin(admin.ModelAdmin):
    list_display = ('project', 'user')
    fieldsets = (
        (None, {
            'fields': (
                'user',
                'project',
                ('start_year', 'start_month', 'still'),
                ('end_year', 'end_month'),
                'weight'
            )
        }),
    )


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name','tags')
    list_per_page = 200
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'tags',
            )
        }),
    )


class SkillItemAdmin(admin.ModelAdmin):
    list_display = ('skill', 'level', 'category', 'user')
    list_per_page = 200
    fieldsets = (
        (None, {
            'fields': (
                'user',
                ('skill', 'level', 'category'),
                
            )
        }),
    )


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('degree', 'school', 'user')
    fieldsets = (
        (None, {
            'fields': (
                'user',
                ('degree', 'school'),
                'result',
                ('start_year', 'start_month'),
                ('end_year', 'end_month'),
                
            )
        }),
    )


admin.site.register(models.Resume, ResumeAdmin)
admin.site.register(models.Certification, CertificationAdmin)
admin.site.register(models.CertificationItem, CertificationItemAdmin)
admin.site.register(models.Experience, ExperienceAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.LanguageItem, LanguageItemAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.ProjectItem, ProjectItemAdmin)
admin.site.register(models.Skill, SkillAdmin)
admin.site.register(models.SkillItem, SkillItemAdmin)
admin.site.register(models.Training, TrainingAdmin)
