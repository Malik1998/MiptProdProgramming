"""Forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from questions.views import QuestionView, QuestionCreate, QuestionUpdate, QuestionDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('questions/', QuestionView.as_view()),
    path('question/add/', QuestionCreate.as_view(success_url="/questions/"), name='question-add'),
    path('question/update/<int:pk>/', QuestionUpdate.as_view(success_url="/questions/"), name='question-update'),
    path('question/delete/<int:pk>/', QuestionDelete.as_view(success_url="/questions/"), name='question-delete'),
    path('', QuestionView.as_view()),
]
