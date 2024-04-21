from django.urls import path
from . import views

urlpatterns = [
    path('campaigns/', views.CreateCampaignList.as_view(), name="campaign-list"),
    path('campaigns/delete/<int:pk>/', views.CampaignDelete.as_view(), name="delete-campaign")
]