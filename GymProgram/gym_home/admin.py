from django.contrib import admin
from .models import Customer, Programs, SignedProgram

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email')
class ProgramsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'timings')
class SignedProgramAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'programName')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Programs, ProgramsAdmin)
admin.site.register(SignedProgram, SignedProgramAdmin)
