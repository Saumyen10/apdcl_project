from django.contrib import admin
from connections.models import connect,Contact,Zone,Division,SubDivision,Consumer

# Register your models here.
admin.site.register(Contact)

admin.site.register(connect)
#class ConnectAdmin(admin.ModelAdmin):
 #   list_display = ('name', 'pincode', 'zone', 'division', 'subdivision')
#admin.site.register(connect, ConnectAdmin)

admin.site.register(Zone)
admin.site.register(Division)
admin.site.register(SubDivision)
admin.site.register(Consumer)