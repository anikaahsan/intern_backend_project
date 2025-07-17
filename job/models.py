""" Implement your job related models here. """
from django.db import models
import uuid
from multiselectfield import MultiSelectField

from core.models import User
from shared.base_model import BaseModel
from job.choices import SkillChoices,ApplicationStatusChoices

class Job(BaseModel):
  
    job_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()
    


    def __str__(self):
        return f"{self.title} ({self.status})"
    



class Application(models.Model):
    

    candidate = models.ForeignKey(User, on_delete=models.CASCADE,related_name='application')
    job = models.ForeignKey(Job, on_delete=models.CASCADE,related_name='application')

   
    skills = MultiSelectField(max_length = 100, choices = SkillChoices)
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2)
    resume = models.FileField(upload_to='resumes/')
    email = models.EmailField(null=True, blank=True)
    contact = models.CharField(max_length=20,null=True, blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=20, choices=ApplicationStatusChoices,default=ApplicationStatusChoices.NOT_SET) #hired/rejected

    class Meta:
        unique_together = ('candidate', 'job')  # Prevent duplicate applications

    def __str__(self):
        return f"{self.candidate.username} applied for {self.job.title}"    

