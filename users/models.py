from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# from datetime import date
from django.contrib.auth.models import User

# Normal default user ı (ekstra fieldlar eklemek için) kullanmayıp kendimiz bir custom user oluşturmak istiyorsak o zaman  AbstractUser dan inherit ederek oluşturabiliriz(exdending user table).Aşağıdaki gibi...ya da yeni bir tablo oluşturup bu tabloyu mevcut user tablosuna onetoone relations ile bağlarsak yeni tablomuza birçok yeni field (özellik) eklemiş oluruz...

# class MyUser(AbstractUser):
#   username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#   email = models.EmailField(('email address'), unique = True)
#   native_name = models.CharField(max_length = 5)
#   phone_no = models.CharField(max_length = 10)
#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
  
#   def __str__(self):
#       return "{}".format(self.email)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(upload_to="pictures", default="avatar.png")
    bio = models.TimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile'"
    
    
 