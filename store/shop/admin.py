from django.forms import ModelChoiceField
from django.contrib import admin

from .models import *



class BackpackAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='backpacks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class PatchAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='patchs'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class СustomizationAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='customers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Backpack, BackpackAdmin)
admin.site.register(Patch, PatchAdmin)
admin.site.register(Customization, СustomizationAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
