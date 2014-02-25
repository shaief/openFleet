from django.contrib import admin
from models import Car, Owner, Classification, MonthlyRecord


# class CarAdmin(admin.ModelAdmin):
#     list_display = ('license_id',
#                     'current_owner',
#                     )


# class OwnerAdmin(admin.ModelAdmin):
#     list_display = ('name',
#                     'email',
#                     )


# class ClassificationAdmin(admin.ModelAdmin):
#     list_display = ('group',
#                     )

# admin.site.register(Owner, OwnerAdmin)
# admin.site.register(Car, CarAdmin)
# admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Classification)
admin.site.register(MonthlyRecord)
