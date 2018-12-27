from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from .models import Photo
from .forms import PhotoAddForm
from django.contrib import messages


class MainView(View):
    class_form = PhotoAddForm

    def get(self, request):
        photos = Photo.objects.order_by('-creation_date')
        return render(request, "photoalbum/content_page.html", {'form': self.class_form, 'photos': photos})

    def post(self, request):
        photos = Photo.objects.order_by('-creation_date')
        form = PhotoAddForm(request.POST, request.FILES)
        user = self.request.user
        if form.is_valid():
            content = form.cleaned_data.get('content')
            photo = form.cleaned_data.get('path')
            added_photo = Photo.objects.create(content=content, user=user, path=photo)
            added_photo.save()
            messages.success(request, 'Dodano wpis')
            return render(request, "photoalbum/content_page.html", {'form': self.class_form, 'photos': photos})
        return render(request, "photoalbum/content_page.html", {'form': form, 'photos': photos})


class UserInstaView(LoginRequiredMixin, View):
    class_form = PhotoAddForm

    def get(self, request):
        photos = Photo.objects.filter(user_id=self.request.user).order_by("-creation_date")
        return render(request, "photoalbum/content_page.html", {'form': self.class_form, 'photos': photos})

    def post(self, request):
        photos = Photo.objects.order_by('-creation_date')
        form = PhotoAddForm(request.POST, request.FILES)
        user = self.request.user
        if form.is_valid():
            content = form.cleaned_data.get('content')
            photo = form.cleaned_data.get('path')
            added_photo = Photo.objects.create(content=content, user=user, path=photo)
            added_photo.save()
            messages.success(request, 'Dodano wpis')
            return render(request, "photoalbum/content_page.html", {'form': self.class_form, 'photos': photos})
        return render(request, "photoalbum/content_page.html", {'form': form, 'photos': photos})