from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class Ativo(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ativos'
    )
    tipo = models.CharField(max_length=20, default='')
    codigo = models.CharField(max_length=10, null=False, blank=False)
    quant = models.FloatField(default=0)
    price = models.FloatField(default=0, validators=[MinValueValidator(0.01)])
    cotacao = models.CharField(max_length=25, default='')
    dividend_yield = models.CharField(max_length=25, default='')
    p_vp = models.CharField(max_length=25, default='')
    liquidez_diaria = models.CharField(max_length=20, default='')
    p_l = models.CharField(max_length=25, default='')
    variacao_24h = models.CharField(max_length=25, default='')
    variacao_12m = models.CharField(max_length=25, default='')
    variacao_24m = models.CharField(max_length=25, default='')
    variacao_60m = models.CharField(max_length=25, default='')

    def __str__(self):
        return f'{self.codigo}'

    def get_default_user_id():
        User = get_user_model()

        if User.objects.exists():
            return User.objects.first().id

        return None
    
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ativos',
        default=get_default_user_id
    )

    def save(self, *args, **kwargs):
        if self.quant is not None:
            self.quant = float(self.quant)

        if self.price is not None:
            self.price = float(self.price)

        super().save(*args, **kwargs)