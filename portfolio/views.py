from django.shortcuts import render

from .models import Profile, Skill, Project, Certification


def home(request):
    context = {
        "profile": Profile.objects.first(),
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "certifications": Certification.objects.all(),
    }

    return render(request, "portfolio/home.html", context)