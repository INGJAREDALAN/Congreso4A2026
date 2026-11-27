from django.db import models
from django.contrib.auth.models import User

from workshops.models import Workshop

class Student(User):
        enrollment = models.CharField("Matricula", max_length=11)
        folio = models.CharField(
            "Folio",
            max_length=4,
            null=True, blank=True, unique=True)
        is_valid = models.BooleanField(
            "Es valida?", default=False)
        workshops = models.ForeignKey(
            Workshop , related_name="Students",
            on_delete = models.SET_NULL, verbose_name="Taller",
            null=True, blank=True)

        def __str__(self):
            return self.enrollement + " " + self.get_full_name()


    # role = models.CharField(
    #     max_length=20,
    #     choices=Role.choices,
    #     default=Role.STUDENT)

class Tutor(User):
    pass
    


class Instructor(User):
    pass