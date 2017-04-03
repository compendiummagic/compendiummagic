from django.contrib import admin
from .models import Book, Misc, Apparel, ApparelSize, ApparelType, MiscType, TrickType, Difficulty, Trick
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'quantity')

class MiscAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'price', 'quantity')

class ApparelAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'price', 'quantity')

class TrickAdmin(admin.ModelAdmin):
    list_display = ('title', 'designer', 'type', 'difficulty', 'price', 'quantity')

class MiscTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)

class ApparelTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)

class TrickTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)

class DifficutyAdmin(admin.ModelAdmin):
    list_display = ('rating',)

class ApparelSizeAdmin(admin.ModelAdmin):
    list_display = ('size',)

admin.site.register(Book, BookAdmin)
admin.site.register(Misc, MiscAdmin)
admin.site.register(Apparel, ApparelAdmin)
admin.site.register(Trick, TrickAdmin)

admin.site.register(ApparelSize, ApparelSizeAdmin)
admin.site.register(ApparelType, ApparelTypeAdmin)
admin.site.register(MiscType, MiscTypeAdmin)
admin.site.register(TrickType, TrickTypeAdmin)
admin.site.register(Difficulty, DifficutyAdmin)