from django.db import models


class SkillChoices(models.TextChoices):
    PYTHON = 'PYTHON', 'Python'
    DJANGO = 'DJANGO', 'Django'
    REACT = 'REACT', 'React'
    NODE = 'NODE', 'Node.js'
    SQL = 'SQL', 'SQL'
    AWS = 'AWS', 'AWS'
    DOCKER = 'DOCKER', 'Docker'


class ApplicationStatusChoices(models.TextChoices):
  HIRED = 'HIRED','Hired'
  REJECTED = 'REJECTED','Rejected'
  PENDING = 'PENDING' ,'Pending'
  NOT_SET = "NOT_SET", "Not Set"



class JobStatusChoices(models.TextChoices):
    PUBLISHED = "PUBLISHED", "Published"
    CLOSED = "CLOSED", "Closed"
