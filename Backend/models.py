from django.db import models


class Pic(models.Model):
    pic = models.ImageField(upload_to='pics', blank=True, null=True)

    def get_absolute_url(self):
        return f"/pic/{self.id}"