from askbot_log.models import UserLog
from django.contrib import admin
from django.utils.safestring import mark_safe

class UserLogAdmin(admin.ModelAdmin):
    fields = ('user', 'ip_addr', 'url', 'data')
    readonly_fields = ('user', 'ip_addr', 'url', 'data')

    def data(self, instance):
        output = ''
        for key in instance.data:
            row = '<tr><td>%s</td><td>%s</td></tr>' % (key, instance.data['key'])
            output += row
        return mark_safe('<table>'+ output + '</table>')
    data.allow_tags = True

admin.site.register(UserLog, UserLogAdmin)
