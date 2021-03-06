from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from group.models import MeetAppGroup

class Interest(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    GENDER_CHOICES = (
        ("Male","Male"),
        ("Female","Female"),
        ("Not Interested","Not Interested")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='profile')
    email = models.EmailField(null=True,help_text="A valid email address")
    location = models.CharField(max_length=255)
    hometown = models.CharField(max_length=255)
    bio = models.TextField(max_length=500, blank=True)
    interests = models.ManyToManyField(Interest, related_name="interests")
    avatar = models.ImageField(upload_to="users/media/images")
    birthdate = models.DateField(null=True, blank=True)
    datejoined = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=14,choices=GENDER_CHOICES)
    group_organizing = models.ManyToManyField(MeetAppGroup,related_name="profile_groups")
    is_organizer = models.BooleanField(default=False)
    
    def __str__(self):
      return f"{self.user.username} Profile" 
    


# Signals to create/update User once Instance is created/updated.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
