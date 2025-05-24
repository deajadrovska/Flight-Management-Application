from django.contrib import admin

from application.models import Flight, Balloon, Airline, Pilot, AirlinePilot


# Register your models here.


class AirlinePilotInline(admin.TabularInline):
    model = AirlinePilot
    extra = 1


class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [AirlinePilotInline,]

class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'take_off_airport', 'landing_airport')
    exclude = ('user', )

    def save_model(self, request, obj, form, change):
        if not change: #ako ne se menuva potocno ako nov se dodava
            obj.user = request.user
        # obj.save() - vaka NE
        return super(FlightAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

class PilotAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')





admin.site.register(Flight, FlightAdmin)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Balloon)
admin.site.register(Pilot, PilotAdmin)


