from django.urls import path
from job.rest.views.job import (
    JobCreateView, JobListView, JobDetailView, JobDetailRecruiterView
)

urlpatterns = [
    path('/list', JobListView.as_view(), name='job-list'),
    path('/create', JobCreateView.as_view(), name='job-create'),
    path('/recruiter/<int:job_id>', JobDetailRecruiterView.as_view(), name='job-detail-recruiter'),
     path('/<int:job_id>', JobDetailView.as_view(), name='job-detail'),
 
 
]