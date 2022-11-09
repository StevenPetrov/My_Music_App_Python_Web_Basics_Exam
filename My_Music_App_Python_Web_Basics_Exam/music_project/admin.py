from django.contrib import admin

# Register your models here.
from My_Music_App_Python_Web_Basics_Exam.music_project.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass
