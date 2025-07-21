from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from job.models import Job
from job.rest.serializers.job import JobSerializer
from job.rest.permissions import IsRecruiter



class JobListView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [AllowAny]

    

class JobCreateView(CreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated,IsRecruiter ]


    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(recruiter=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class JobDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsRecruiter] 
    lookup_field = "job_id"   





