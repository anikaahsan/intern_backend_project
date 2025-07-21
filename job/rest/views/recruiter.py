from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from job.models import Job,Application
from job.rest.serializers.job import JobSerializer
from job.rest.permissions import IsRecruiter



class RecruiterStatsView(APIView):
    permission_classes = [IsAuthenticated,IsRecruiter]

    def get(self, request):
        

        #Total published jobs
        total_published_jobs = Job.objects.filter(status='PUBLISHED')
        total_published_jobs_count =Job.objects.filter(status='PUBLISHED').count()

        #Total closed jobs
        total_closed_jobs_count = Job.objects.filter(status='CLOSED').count()
        total_closed_jobs = Job.objects.filter(status='CLOSED')

        #total candidate applications
        applications = Application.objects.all()
        total_applications = applications.count()

        #Total candidates hired
        total_hired=applications.filter(status='HIRED')
        total_hired_count = applications.filter(status='HIRED').count()

         #Total candidates rejected
        total_rejected=applications.filter(status='REJECTED')
        total_rejected_count = applications.filter(status='REJECTED').count()

        return Response({
            'total_published_jobs': total_published_jobs,
            'total_published_jobs_count': total_published_jobs_count,

            'total_closed_jobs': total_closed_jobs,
            'total_closed_jobs_count':total_closed_jobs_count,

            'total_candidate_applications': total_applications,
            'total_applications':total_applications,

            'total_candidates_hired': total_hired,
            'total_hired_count':total_hired_count,

            'total_candidates_rejected': total_rejected,
            'total_rejected_count':total_rejected_count
        })