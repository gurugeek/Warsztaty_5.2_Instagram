from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import PhotoAddForm, SendMessageForm, SendMessageToUserForm, AddCommentForm
from .models import *


class MainView(View):
    class_form = PhotoAddForm

    def get(self, request):
        photos = Photo.objects.filter(blocked=False).order_by('-creation_date')
        return render(request, "photoalbum/content_page.html", {'form': self.class_form, 'photos': photos})

    def post(self, request):
        photos = Photo.objects.filter(blocked=False).order_by('-creation_date')
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
        photos = Photo.objects.filter(blocked=False, user_id=self.request.user).order_by("-creation_date")
        return render(request, "photoalbum/content_page.html", {'form': self.class_form, 'photos': photos})

    def post(self, request):
        photos = Photo.objects.filter(blocked=False).order_by('-creation_date')
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


class UserReceivedMessagesView(LoginRequiredMixin, View):
    def get(self, request):
        id_user = request.user.id
        user_messages = Message.objects.filter(sent_to_id=id_user, blocked=False).order_by("-sent_date")
        received = True
        return render(request, "photoalbum/user_messages.html",
                      {'id_user': id_user, 'user_messages': user_messages, 'received': received})


class UserSentMessagesView(LoginRequiredMixin, View):
    def get(self, request):
        id_user = request.user.id
        user_messages = Message.objects.filter(sent_from_id=id_user, blocked=False).order_by("-sent_date")
        return render(request, "photoalbum/user_messages.html", {'id_user': id_user, 'user_messages': user_messages})


class MessageDetailView(LoginRequiredMixin, View):
    def get(self, request, id_message):
        message_detail = Message.objects.get(id=id_message)
        message_detail.read = True
        message_detail.save()
        return render(request, "photoalbum/message_details.html", {'message_detail': message_detail})


class SendMessageView(LoginRequiredMixin, View):
    def get(self, request):
        form = SendMessageForm
        return render(request, "photoalbum/add.html", {'form': form})

    def post(self, request):
        sent_from = request.user
        form = SendMessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            sent_to = form.cleaned_data.get('sent_to')
            message_sent = Message(content=content, sent_from=sent_from, sent_to=sent_to, blocked=False)
            message_sent.save()
            messages.success(request, "Wiadomość wysłana")
        return redirect("messages-received")


class SendMessageToUserView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user_id = user_id
        form = SendMessageToUserForm
        return render(request, "photoalbum/add.html", {'form': form, 'user_id': user_id})

    def post(self, request, user_id):
        sent_from = request.user
        sent_to = User.objects.get(id=user_id)
        form = SendMessageToUserForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            message_sent = Message(content=content, sent_from=sent_from, sent_to=sent_to, blocked=False)
            message_sent.save()
            messages.success(request, "Wiadomość wysłana")
        return redirect("main")


class ShowPhotoView(LoginRequiredMixin, View):
    def get(self, request, id_photo):
        photo = get_object_or_404(Photo, id=id_photo, blocked=False)
        comments = Comment.objects.filter(photo_id=photo.id, blocked=False)
        form = AddCommentForm()
        return render(request, "photoalbum/photo_detail.html", {'photo':photo, 'comments':comments, 'form':form})

    def post(self, request, id_photo):
        photo = get_object_or_404(Photo, pk=id_photo)
        form = AddCommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            comment = Comment(content=content, photo=photo, user=request.user, blocked=False)
            comment.save()
            messages.success(request, "Komentarz został dodany poprawnie")
        return redirect("show-photo", id_photo=id_photo)