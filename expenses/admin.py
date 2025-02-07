from django.contrib import admin
from django.utils.html import format_html
from .models import DiaryEntry, PasswordStorage, Grade, TierList, TierItem, UserActivity

@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_preview', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username', 'content')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)

    def content_preview(self, obj):
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content
    content_preview.short_description = 'Conteúdo'

@admin.register(PasswordStorage)
class PasswordStorageAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_name', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username', 'service_name')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'value', 'date', 'created_at')
    list_filter = ('user', 'subject', 'date')
    search_fields = ('user__username', 'subject', 'notes')
    date_hierarchy = 'date'
    readonly_fields = ('created_at', 'updated_at')

class TierItemInline(admin.TabularInline):
    model = TierItem
    extra = 1
    readonly_fields = ('created_at', 'updated_at')

@admin.register(TierList)
class TierListAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'items_count', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username', 'name', 'description')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    inlines = [TierItemInline]

    def items_count(self, obj):
        return obj.items.count()
    items_count.short_description = 'Número de Itens'

@admin.register(TierItem)
class TierItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'tierlist', 'tier_colored', 'created_at')
    list_filter = ('tier', 'created_at', 'tierlist')
    search_fields = ('name', 'description', 'tierlist__name')
    readonly_fields = ('created_at', 'updated_at')

    def tier_colored(self, obj):
        colors = {
            'S': '#FF7F7F',  # Vermelho claro
            'A': '#FFB27F',  # Laranja
            'B': '#FFFF7F',  # Amarelo
            'C': '#7FFF7F',  # Verde claro
            'D': '#7F7FFF',  # Azul claro
            'F': '#FF7FFF',  # Rosa
        }
        return format_html(
            '<span style="background-color: {}; padding: 2px 6px; border-radius: 3px;">{}</span>',
            colors.get(obj.tier, '#FFFFFF'),
            obj.get_tier_display()
        )
    tier_colored.short_description = 'Tier'

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'path', 'last_activity')
    list_filter = ('user', 'last_activity', 'ip_address')
    search_fields = ('user__username', 'ip_address', 'path')
    date_hierarchy = 'last_activity'
    readonly_fields = ('user', 'ip_address', 'last_activity', 'user_agent', 'path')
