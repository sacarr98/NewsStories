from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, News, Comment


# unregister groups
admin.site.unregister(Group)

# combine profile information with user information
class ProfileInline(admin.StackedInline):
    model = Profile

# extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Just display username fields on admin page
    fields = ["username"]
    inlines = [ProfileInline]

# unregister default user
admin.site.unregister(User)

# reregister User and Profile
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)

# Register Posts
admin.site.register(News)

# Register Comments
admin.site.register(Comment)