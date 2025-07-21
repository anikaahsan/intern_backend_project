from rest_framework import serializers
from job.models import Application,Job
from datetime import date
class ApplicationSerializer(serializers.ModelSerializer):
     class Meta:
        model=Application
        fields=['job','skills','expected_salary','resume','email','contact']


     def __str__(self):
        return f' { self.job.title }'
     
     def validate(self, attrs):
         print(attrs)
         job=attrs['job']
         user = self.context['request'].user
         job=Job.objects.get(pk=attrs['job'])
         if not Application.objects.filter(candidate=user,job=job):
              raise serializers.ValidationError("You have already applied to this job.")
         if not date.today() < job.deadline :
             raise serializers.ValidationError("Deadline Exceeded")
        
         return attrs
        

        