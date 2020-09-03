from django.db import models


class Colaborador(models.Model):
    colab_name = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    celular = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.colab_name

    pass


class Ativo(models.Model):
    mac = models.CharField(max_length=12)
    dev_name = models.CharField(max_length=50)
    ports = models.IntegerField()
    poe = models.BooleanField()
    ipv4 = models.GenericIPAddressField(protocol='IPv4', null=True, blank=True)
    ipv6 = models.GenericIPAddressField(protocol='IPv6', null=True, blank=True)
    serial = models.CharField(max_length=50, null=True, blank=True)
    patrimonio = models.CharField(max_length=10)
    instalado = models.BooleanField()
    local = models.CharField(max_length=200)
    rack_pos = models.IntegerField(null=True, blank=True)
    instaladores = models.ManyToManyField(Colaborador)

    def __str__(self):
        return self.dev_name
