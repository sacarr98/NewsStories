from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField


# Post Model
class News(models.Model):
    user = models.ForeignKey(
        User, related_name="news",
        on_delete=models.DO_NOTHING
    )
    title = models.CharField(max_length=100, null=True, blank=True)
    summary = models.CharField(max_length=200, null=True, blank=True)
    body = models.CharField(max_length=600, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="news_like", blank=True)

    # Count number of likes
    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return(
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.title}"
            f"{self.body}"
        )


# Comment Model
class Comment(models.Model):
    news = models.ForeignKey(News, related_name="comments", on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.comment_body} by {self.commenter}"



# Create User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",
        related_name="followed_by",
        symmetrical=False,
        blank=True)
    
    date_modified = models.DateTimeField(User, auto_now=True)
    profile_image = CloudinaryField('image', default='placeholder')

    profile_bio = models.CharField(max_length=100, null=True, blank=True)
    website_link = models.CharField(max_length=100, null=True, blank=True)
    facebook_link = models.CharField(max_length=100, null=True, blank=True)
    instagram_link = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.user.username

# Create a profile for a new user
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # User follows themselves in order to view their own posts
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

post_save.connect(create_profile, sender=User)

