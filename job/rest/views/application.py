from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from job.rest.serializers.application import ApplicationSerializer
from job.rest.permissions import IsCandidate,IsRecruiter
from job.models import Application
 
class ApplyToJobView(CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsCandidate]
    parser_classes = [MultiPartParser, FormParser] # required for file upload
    lookup_field='job_id'

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,context={"job_id": request.query_params["job_id"]})
        serializer.is_valid(raise_exception =  True)
        serializer.save(candidate=request.user)
        return response(serializer.data,status=status.HTTP_201_CREATED)

  

class ApplicationListView(ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsCandidate,IsRecruiter]

    def get_queryset(self):
        if self.request.user.role == 'CANDIDATE' :
           return Application.objects.filter(candidate=self.request.user)
        
        if self.request.user.role == 'RECRUITER' :
            return Application.objects.all()