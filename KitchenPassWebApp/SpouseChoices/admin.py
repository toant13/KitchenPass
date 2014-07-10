from django.contrib import admin
from SpouseChoices.models import SpouseRequest, SpouseResponse



class SpouseRequestAdmin(admin.ModelAdmin):
    list_display = ('question', 'votes')

class SpouseResponseAdmin(admin.ModelAdmin):
    list_display = ('answer', 'votes')

admin.site.register(SpouseRequest, SpouseRequestAdmin)
admin.site.register(SpouseResponse, SpouseResponseAdmin)

