from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_profile.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height>300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        db_table = 'Profiles'

class Meal(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_food.jpg', upload_to='food_pics')

    def __str__(self):
        return f'{self.title}'

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height>500 or img.width > 500:
            output_size = (500,500)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        db_table = 'Meals'