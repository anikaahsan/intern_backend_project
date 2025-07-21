from django.urls import path, include


urlpatterns = [
    path("/job", include("job.rest.urls.job")),
    path("/application", include("job.rest.urls.application")),
     path("/recruiter", include("job.rest.urls.recruiter")),
    

]