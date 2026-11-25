from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        INSTRUCTOR = "INSTRUCTOR", "Instructor"
        TUTOT = "TUTOR", "Tutor"
        STUDENT = "STUDENT", "Student"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT)

class StudentProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        relate_name="perfil_estudiante")
    enrollment = models.CharField("Matricula", max_length=11)

class TutorProfile(models.Model):
    user= models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="perfil_tutor")
    employee_number= models.CharField('Numero de empleado', max_length=4)

class Instructor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="perfil_instructor")
    title = models.ChardField("Titulo", max_legth=20)