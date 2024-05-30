from django.urls import path, include


urlpatterns = [
    path('mymessages/', include('my_messages.urls')),
]
