from django.urls import path
from job.rest.views.application import (
    
    ApplyToJobView, ApplicationListView
)

urlpatterns = [
  

    path('/list', ApplicationListView.as_view(), name='application-list'),
    path('/apply/<int:job_id>', ApplyToJobView.as_view(), name='apply-job'),
]