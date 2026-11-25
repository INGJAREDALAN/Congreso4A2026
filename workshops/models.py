from django.db import models

# Create your models here.
# Un modelo es una representacion de una tabla
# ORM donde una tabla es una clase (Atributos , Metodos)


class Classroom (models.Model):
    name = models.CharField("nombre", max_length=100)
    description = models.TextField("Descripción", null=True, blank=True)
    building = models.CharField("Edicio", max_length=100)

    FLOORS = [("planta baja", "Planta_Baja"), ("planta_alta", "Planta_Alta")]
    floor = models.CharField("Planta", max_length=50, choices=FLOORS)

    def __str__(self):
        return self.name +" - " + self.building

    class Meta:
        verbose_name ="Salon/Laboratorio"
        verbose_name_plural = "Salones/Laboratorios"


class Workshop(models.Model):
    name = models.CharField("Nombre", max_length=100)
    description = models.TextField("Descripcion")

    # instructor = models.CharField("Instructor", max_length=100)

    capacity = models.ForeignKey(Classroom,
                                 related_name= "workshops",
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True)
    image = models.ImageField("Imagen de Taller",
                                upload_to = "images",
                                null=True, blank=True)
    date = models.DateField("Fecha")
    start_time = models.TimeField("Hora de inicio", null= True, blank=True)
    end_time = models.TimeField("Hora de termino", null= True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Taller"
        verbose_name_plural = "Talleres"