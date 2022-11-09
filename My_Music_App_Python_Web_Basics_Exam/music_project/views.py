from django.shortcuts import render, redirect

from My_Music_App_Python_Web_Basics_Exam.music_project.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, \
    AlbumDeleteForm, ProfileDeleteForm
from My_Music_App_Python_Web_Basics_Exam.music_project.models import Profile, Album


def profile_add(request):
    if get_profile() is not None:
        return redirect('index') #25.30 DONCHO VIDEO

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'hide_nav': True
    }
    return render(request,'core/home-no-profile.html', context)


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return redirect('profile add')

    context = {
        'albums': Album.objects.all()
    }
    return render(request, 'core/home-with-profile.html', context)


def album_add(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'album/add-album.html', context)


def album_details(request, pk):
    album = Album.objects.filter(pk=pk).get()
    context = {
        'album': album
    }
    return render(request, 'album/album-details.html', context)


def album_edit(request, pk):
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'album' : album,
    }
    return render(request, 'album/edit-album.html', context)


def album_delete(request, pk):
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'album' : album,
    }
    return render(request, 'album/delete-album.html',context)


def profile_details(request):
    profile = get_profile()
    albums_count = Album.objects.count()
    context = {
        'profile': profile,
        'albums_count': albums_count
    }
    return render(request, 'profile/profile-details.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'profile/profile-delete.html', context)
