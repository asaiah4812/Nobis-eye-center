from django.contrib import admin
from . models import Service, Day, Doctor, Book, Message

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'created')
    prepopulated_fields = {'slug': ('title',)}
    
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('slug', 'position', 'slug', 'create_at')
    prepopulated_fields = {'slug': ('position',)}


admin.site.register(Service, ServiceAdmin)

admin.site.register(Day)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Book)
admin.site.register(Message)

