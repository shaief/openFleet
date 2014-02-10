from django.contrib import admin

# Register your models here.
from models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('license_id',
                    'current_owner',
                    )


admin.site.register(Car, CarAdmin)
