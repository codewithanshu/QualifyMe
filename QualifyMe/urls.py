"""
URL configuration for QualifyMe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


from django.urls import path, include
from user.views import UserListCreateView, UserRetrieveUpdateDeleteView
from qualifications.views import (
    QualificationListCreateView,
    QualificationRetrieveUpdateDeleteView,
    QualificationListByUserView,
)

urlpatterns = [
    path('api/users/', UserListCreateView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='user-retrieve-update-delete'),
    path('api/qualifications/', QualificationListCreateView.as_view(), name='qualification-list-create'),
    path('api/qualifications/<int:pk>/', QualificationRetrieveUpdateDeleteView.as_view(), name='qualification-retrieve-update-delete'),
    path('api/users/<int:user_id>/qualifications/', QualificationListByUserView.as_view(), name='qualification-list-by-user'),
]

