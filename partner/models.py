from django.db import models


# Create your models here.
class Partner(models.Model):
    full_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='partner/')

    def str(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def str(self):
        return self.name


class SocialNetwork(models.Model):
    YOUTUBE = "YOUTUBE"
    TIKTOK = "TIKTOK"
    INSTAGRAM = "INSTAGRAM"
    TELEGRAM = "TELEGRAM"
    SOCIAL_NETWORK_CHOUCES = (
        (TELEGRAM, TELEGRAM),
        (TIKTOK, TIKTOK),
        (INSTAGRAM, INSTAGRAM),
        (YOUTUBE, YOUTUBE),

    )
    sub_count = models.IntegerField(default=0)
    url = models.URLField()
    name = models.CharField(choices=SOCIAL_NETWORK_CHOUCES, max_length=100)
    price = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)

    def str(self):
        return f"{self.name}|{self.partner.full_name}"