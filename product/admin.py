from django.contrib import admin
from .models import LanguageTagMaster, Product, LevelTagMaster, ContentTagMaster, Review

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'producer', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    search_fields = ('title', 'user_id')

class LevelTagMasterAdmin(admin.ModelAdmin):
    list_display = ('level_tag_name','pk')

class LanguageTagMasterAdmin(admin.ModelAdmin):
    list_display = ('language_tag_name','pk')

class ContentTagMasterAdmin(admin.ModelAdmin):
    list_display = ('content_tag_name','pk')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user_id', 'created_at', 'score')
    ordering = ('-created_at',)
    
admin.site.register(Product,ProductAdmin)
admin.site.register(LevelTagMaster,LevelTagMasterAdmin)
admin.site.register(LanguageTagMaster,LanguageTagMasterAdmin)
admin.site.register(ContentTagMaster,ContentTagMasterAdmin)
admin.site.register(Review,ReviewAdmin)