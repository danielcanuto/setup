from django.db import models

class Regiao(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "REGIÕES"


class Cidades(models.Model):
    cidade = models.CharField(max_length= 80)
    
    def __str__(self):
        return self.cidade
    
    class Meta:
        verbose_name_plural = "CIDADES"
        ordering = ['cidade']



class UnidadeFederativa(models.Model):
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Região")
    estado = models.CharField(max_length=40, verbose_name="Unidade Federativa")
    sigla = models.CharField(max_length=2, verbose_name="Sigla Estado")
    
    def __str__(self):
        return self.sigla

    class Meta:
        verbose_name_plural = "TABELA ESTADOS"   
        ordering = ['sigla']

class CidadeUF(models.Model):
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE, blank=True, null=True)
    estado = models.ForeignKey(UnidadeFederativa, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.cidade}/{self.estado}'

    class Meta:
        verbose_name_plural = "CIDADES/ESTADO"
        ordering = ['estado']        

class Capitais(models.Model):
    cidade = models.ForeignKey(CidadeUF, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.cidade}'

    class Meta:
        verbose_name_plural = "CAPITAIS"
        ordering = ['cidade']