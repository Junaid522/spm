from django.db import models

# Create your models here.
from django.db.models import CASCADE


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class MarkupKey(BaseModel):
    markup_key = models.CharField(max_length=255, null=True, blank=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.markup_key)


class Container(BaseModel):
    container_number = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.container_number)


class PakistaniPayment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    container = models.ForeignKey(Container, on_delete=CASCADE)
    duty_tax = models.IntegerField(null=True, blank=True)
    other_charges = models.IntegerField(null=True, blank=True)
    total_paid = models.IntegerField(null=True, blank=True)


class ChinaPayment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    container = models.ForeignKey(Container, on_delete=CASCADE)
    tt_amount = models.FloatField(null=True, blank=True)
    tt_charges = models.FloatField(null=True, blank=True)
    rmb_comission = models.FloatField(null=True, blank=True)
    total_paid = models.FloatField(null=True, blank=True)
    file = models.FileField(upload_to='attachments/',null=True, blank=True)


class Carton(models.Model):
    container = models.ForeignKey(Container, on_delete=CASCADE)
    carton_number = models.CharField(max_length=255)
    carton_name = models.CharField(max_length=255, null=True, blank=True)


class Item(models.Model):
    carton = models.ForeignKey(Carton, on_delete=CASCADE)
    item_number = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255, null=True, blank=True)
