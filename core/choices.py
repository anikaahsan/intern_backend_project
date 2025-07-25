from django.db import models


class GenderChoices(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"
    OTHER = "OTHER", "Other"
    NOT_SPECIFIED = "NOT_SPECIFIED", "Not Specified"
    NOT_SET = "NOT_SET", "Not Set"

class RoleChoices(models.TextChoices):
      RECRUITER='RECRUITER','Recruiter'
      CANDIDATE='CANDIDATE','Candidate'
      NOT_SET = "NOT_SET", "Not Set"

