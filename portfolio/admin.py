
from django.contrib import admin
from .models import Profile, Skill, Project, Certification


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "role")
    search_fields = ("name", "role")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    search_fields = ("name", "category")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "is_featured")
    list_filter = ("is_featured",)
    search_fields = ("title", "description")


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("title", "issuer", "date", "certificate_file")
    search_fields = ("title", "issuer")
    list_filter = ("issuer",)
