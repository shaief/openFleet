from django.contrib import admin
from models import (Classification, Car, CarStatus, CarOwnership,
                    Department, Manager, Owner,
                    MonthlyRecord, KMRead, Accident,
                    TreatmentType, Treatment,
                    City, Parking, Road6)


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
admin.site.register(Department)
admin.site.register(Manager)
admin.site.register(Owner)

admin.site.register(Classification)
admin.site.register(Car)
admin.site.register(CarStatus)
admin.site.register(CarOwnership)

admin.site.register(MonthlyRecord)
admin.site.register(KMRead)
admin.site.register(Accident)

admin.site.register(TreatmentType)
admin.site.register(Treatment)

admin.site.register(City)
admin.site.register(Parking)

admin.site.register(Road6)
