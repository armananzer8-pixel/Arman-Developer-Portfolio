
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile, Skill, Project, Certification


def home(request):
    context = {
        "profile": Profile.objects.first(),
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "certifications": Certification.objects.all(),
    }

    return render(request, "portfolio/home.html", context)


@login_required
def dashboard(request):
    context = {
        "profile": Profile.objects.first(),
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "certifications": Certification.objects.all(),
    }

    return render(request, "portfolio/dashboard.html", context)
