from django.db import models
from cidade_uf.models import CidadeUF
# para validação cpf
from cpf_field.models import CPFField
# from phone_field import PhoneField


class Person(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das opções"]
    ]

    name = models.CharField('Nome Completo', max_length=150)
    birthday = models.DateField('Aniversário')
    bio = models.TextField('Sobre', null=True, blank=True)
    photo = models.ImageField('Foto', upload_to='clients_photos', null=True, blank=True)
    cpf = CPFField('cpf', null=True, blank=True)
    rg = models.CharField('RG', max_length=14, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

   
    def __str__(self):
        return f'{self.name}'
    
    def first_name(self):
        name = self.name.strip().split()
        return name[0]


class Cliente(models.Model):
    person = models.ForeignKey(Person, on_delete= models.CASCADE, blank=True, null=True, verbose_name='Nome')
    telefone = models.CharField('Telefone',max_length=31, blank=True, null=True)
    email = models.CharField('E-mail', max_length=50)
    cidade_estado = models.ForeignKey(CidadeUF, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Cidade/UF")
    endereco = models.CharField('End', max_length=50)
    numero = models.CharField('nº', max_length=5)
    bairro = models.CharField('Bairro', max_length=20)
    cep =models.CharField('CEP', max_length=9)

    def __str__(self):
        return f'{self.person} - {self.telefone}'