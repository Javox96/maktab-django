from django.db import models

class Carousel(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    subtitle = models.CharField(max_length=300, null=True, blank=True, verbose_name="Kichik sarlavha")
    label = models.CharField(max_length=100, null=True, blank=True, verbose_name="Yorliq (masalan: Kelajak ta'limi)")
    image = models.ImageField(upload_to='carousel/', verbose_name="Rasm")
    button_text = models.CharField(max_length=50, null=True, blank=True, verbose_name="Tugma matni")
    button_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Tugma havolasi")
    order = models.IntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Aktivmi")

    class Meta:
        verbose_name = "Karusel"
        verbose_name_plural = "Karusellar"
        ordering = ['order']

    def __str__(self):
        return self.title
