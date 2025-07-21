from django.urls import path
from job.rest.views.recruiter import RecruiterStatsView

urlpatterns = [
    path('/stats', RecruiterStatsView.as_view(), name='recruiter-stats'),
]