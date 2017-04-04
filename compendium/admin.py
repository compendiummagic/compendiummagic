from django.contrib import admin
from .models import Book, Misc, Apparel, ApparelSize, ApparelType, MiscType, TrickType, Difficulty, Trick, Act, ActStyle
from .models import Item
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'quantity')

class MiscAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'price', 'quantity')

class ApparelAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'price', 'quantity')

class TrickAdmin(admin.ModelAdmin):
    list_display = ('title', 'designer', 'type', 'difficulty', 'price', 'quantity')

class ActAdmin(admin.ModelAdmin):
    list_display = ('name', 'style', 'speciality')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')

class MiscTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)

class ApparelTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)

class TrickTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)

class ActStyleAdmin(admin.ModelAdmin):
    list_display = ('style',)

class DifficutyAdmin(admin.ModelAdmin):
    list_display = ('rating',)

class ApparelSizeAdmin(admin.ModelAdmin):
    list_display = ('size',)

admin.site.register(Book, BookAdmin)
admin.site.register(Misc, MiscAdmin)
admin.site.register(Apparel, ApparelAdmin)
admin.site.register(Trick, TrickAdmin)
admin.site.register(Act, ActAdmin)
admin.site.register(Item, ItemAdmin)

admin.site.register(ApparelSize, ApparelSizeAdmin)
admin.site.register(ApparelType, ApparelTypeAdmin)
admin.site.register(MiscType, MiscTypeAdmin)
admin.site.register(TrickType, TrickTypeAdmin)
admin.site.register(ActStyle, ActStyleAdmin)
admin.site.register(Difficulty, DifficutyAdmin)