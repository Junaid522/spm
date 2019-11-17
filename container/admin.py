from django.contrib import admin

# Register your models here.
from container.models import MarkupKey, Container, PakistaniPayment, ChinaPayment, Carton, Item


class MarkupKeyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'created_at', 'updated_at', 'is_active', 'is_used', 'markup_key',)
    list_display_links = ('id', 'markup_key',)
    list_filter = ['is_active', 'is_used', ]
    search_fields = ('id', 'markup_key',)
    ordering = ['-id', ]


class ContainerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'created_at', 'updated_at', 'container_number',)
    list_display_links = ('id', 'container_number',)
    list_filter = ['container_number', ]
    search_fields = ('id', 'container_number',)
    ordering = ['-id', ]


class PakistaniPaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'container', 'duty_tax', 'other_charges', 'total_paid',)
    list_display_links = ('id', 'container',)
    list_filter = ['container', ]
    search_fields = ('id', 'container',)
    ordering = ['-id', ]


class ChinaPaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'container', 'tt_amount', 'tt_charges', 'rmb_comission', 'total_paid', 'file',)
    list_display_links = ('id', 'container',)
    list_filter = ['container', ]
    search_fields = ('id', 'container',)
    ordering = ['-id', ]


class CartonAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'container', 'carton_number', 'carton_name',)
    list_display_links = ('id', 'container',)
    list_filter = ['container', 'carton_number',]
    search_fields = ('id', 'container',)
    ordering = ['-id', ]


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'carton', 'item_number', 'item_name',)
    list_display_links = ('id', 'carton',)
    list_filter = ['carton', 'item_number',]
    search_fields = ('id', 'carton',)
    ordering = ['-id', ]


admin.site.register(MarkupKey, MarkupKeyAdmin)
admin.site.register(Container, ContainerAdmin)
admin.site.register(PakistaniPayment, PakistaniPaymentAdmin)
admin.site.register(ChinaPayment, ChinaPaymentAdmin)
admin.site.register(Carton, CartonAdmin)
admin.site.register(Item, ItemAdmin)
