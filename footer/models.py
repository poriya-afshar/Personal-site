from django.db import models


class Footer(models.Model):
    address = models.TextField()
    email = models.EmailField()
    phone = models.TextField()



class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    massage = models.TextField()

    def __str__(self):
        return f'{self.name} == {self.email}'

