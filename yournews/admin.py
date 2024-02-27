from django.contrib import admin
from django.contrib.auth.models import Group, User


# unregister groups
admin.site.unregister(Group)

# extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Just display username fields on admin page
    fields = ["username"]

# unregister default user
admin.site.unregister(User)
# reregister User
admin.site.register(User, UserAdmin)