from django.contrib import admin
from .models import RequestLog
from .utils import format_as_table

class RequestLogAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('user', 'url', 'timestamp',
                'method', 'parameters_disp', 'ip_addr')
        }),
        ('Session', {
            'fields': ('session_key', 'session_data_disp'),
            'classes': ('collapse',)
        }),
        ('Cookies', {
            'fields': ('cookies_disp',),
            'classes': ('collapse',)
        }),
        ('Request META', {
            'fields': ('meta_disp',),
            'classes': ('collapse',)
        })
    )
    readonly_fields = (
        'user', 'timestamp', 'ip_addr', 'method', 'url', 'parameters_disp',
        'cookies_disp', 'meta_disp', 'session_key',
        'session_data_disp'
    )

    list_display = ('user', 'url', 'timestamp')

    def parameters_disp(self, instance):
        return format_as_table(instance.parameters)
    parameters_disp.allow_tags = True
    parameters_disp.short_description = 'Parameters'

    def cookies_disp(self, instance):
        return format_as_table(instance.cookies)
    cookies_disp.allow_tags = True
    cookies_disp.short_description = 'Cookies'

    def meta_disp(self, instance):
        return format_as_table(instance.meta)
    meta_disp.allow_tags = True
    meta_disp.short_description = 'Meta'

    def session_data_disp(self, instance):
        return format_as_table(instance.session_data)
    session_data_disp.allow_tags = True
    session_data_disp.short_description = 'Session data'

admin.site.register(RequestLog, RequestLogAdmin)
