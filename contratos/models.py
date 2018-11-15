from django.db import models

class ModelBase(models.Model):
    nome = models.CharField(max_length= 100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

class Item(ModelBase):

    class Meta(ModelBase.Meta):
        db_table = 'item'

class Plano(ModelBase):
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    itens = models.ManyToManyField(Item)

    class Meta(ModelBase.Meta):
        db_table = 'plano'

class Orcamento(ModelBase):
    email = models.EmailField(max_length= 70)
    planos = models.ManyToManyField(Plano)
    data_evento = models.DateField()

    class Meta():
        db_table = 'orcamento'