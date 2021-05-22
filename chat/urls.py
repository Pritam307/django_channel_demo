from django.contrib import admin
from django.urls import include, path

from chat.views import get_chat_view

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('start_chat/', get_chat_view,name='start_chat'),
]