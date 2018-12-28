from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('user_insta/', UserInstaView.as_view(), name='user-insta'),
    path('user_messages_received/', UserReceivedMessagesView.as_view(), name='messages-received'),
    path('user_messages_sent/', UserSentMessagesView.as_view(), name='messages-sent'),
    path('message_detail/<int:id_message>/', MessageDetailView.as_view(), name='message-details'),
    path('send_message/', SendMessageView.as_view(), name='send-message'),
    path('send_message/<int:user_id>', SendMessageToUserView.as_view(), name='send-message-to-user'),
    path('photo/<int:id_photo>/', ShowPhotoView.as_view(), name='show-photo'),
]
