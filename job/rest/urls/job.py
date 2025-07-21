from django.urls import path
from job.rest.views.job import (
    JobCreateView, JobListView, JobDetailView, 
)

urlpatterns = [
    path('/list', JobListView.as_view(), name='job-list'),
    path('/create', JobCreateView.as_view(), name='job-create'),
    path('/<int:pk>', JobDetailView.as_view(), name='job-detail'),
 
 
]