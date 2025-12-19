from django.contrib import admin
from .models import KnittingPattern, YarnType, Tutorial


@admin.register(KnittingPattern)
class KnittingPatternAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'yarn_type', 'needle_size', 'created_at')
    list_filter = ('difficulty', 'created_at')
    search_fields = ('title', 'description')


@admin.register(YarnType)
class YarnTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'composition', 'thickness', 'price', 'in_stock')
    list_filter = ('in_stock', 'thickness')
    search_fields = ('name', 'composition')


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
