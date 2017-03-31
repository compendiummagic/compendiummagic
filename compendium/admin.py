from django.contrib import admin
from .models import Book, Misc, Apparel, ApparelSize, ApparelType, MiscType
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'quantity')

class MiscAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'price', 'quantity')

class ApparelAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'price', 'quantity')

class MiscTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)

class ApparelTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)

class ApparelSizeAdmin(admin.ModelAdmin):
    list_display = ('size',)

admin.site.register(Book, BookAdmin)
admin.site.register(Misc, MiscAdmin)
admin.site.register(Apparel, ApparelAdmin)

admin.site.register(ApparelSize, ApparelSizeAdmin)
admin.site.register(ApparelType, ApparelTypeAdmin)
admin.site.register(MiscType, MiscTypeAdmin)