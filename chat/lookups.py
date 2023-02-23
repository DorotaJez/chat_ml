from ajax_select import register, LookupChannel
from django.contrib.auth.models import User

@register('users')
class UserLookup(LookupChannel):

    model = User

    def check_auth(self, request):
        return True

    def get_query(self, q, request):
        return self.model.objects.filter(username__icontains=q)

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.username
    
    def format_match(self, obj):
        return self.format_item_display(obj)
    