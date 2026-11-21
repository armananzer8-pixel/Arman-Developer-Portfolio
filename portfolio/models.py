
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, default="Arman")
    role = models.CharField(max_length=150, blank=True)
    introduction = models.TextField(blank=True)
    about = models.TextField(blank=True)
    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )
    email = models.EmailField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    technologies = models.CharField(max_length=250, blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=150, blank=True)
    date = models.DateField(null=True, blank=True)

    certificate_file = models.FileField(
        upload_to="certifications/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
