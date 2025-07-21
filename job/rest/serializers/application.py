from rest_framework import serializers
from job.models import Application,Job
from datetime import date
class ApplicationSerializer(serializers.ModelSerializer):
     class Meta:
        model=Application
        fields=['skills','expected_salary','resume','email','contact']


     def __str__(self):
        return f' { self.job.title }'
     
     def validate(self, attrs):
         print(attrs)
         job_id = self.context['job_id']
         try:
            job = Job.objects.get(pk=job_id)
         except Job.DoesNotExist:
            raise serializers.ValidationError("Job does not exist.")
         
         user = self.context['request'].user
         
         if not Application.objects.filter(candidate=user,job=job):
              raise serializers.ValidationError("You have already applied to this job.")
         if not date.today() < job.deadline :
             raise serializers.ValidationError("Deadline Exceeded")
        
         return attrs
        

        