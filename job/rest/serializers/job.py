from rest_framework import serializers
from job.models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields=['job_id','title','description','location','salary','deadline']


    def __str__(self):
        return f'{self.title} ({ self.deadline })'
        







