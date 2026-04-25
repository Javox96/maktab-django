from django.db import models
from django.contrib.auth.models import User


class Sinf(models.Model):
    """O'quv sinfi (masalan: 1-sinf, 2-sinf, ...)."""

    nom = models.CharField(max_length=100, verbose_name="Sinf nomi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqt")

    class Meta:
        verbose_name = "Sinf"
        verbose_name_plural = "Sinflar"
        ordering = ['nom']
        # Mavjud jadval nomini saqlaymiz — migratsiya kerak emas
        db_table = 'javohir_sinf'

    def __str__(self):
        return self.nom


class Savol(models.Model):
    """Test savoli — 3 ta variant va to'g'ri javob bilan."""

    class ToGriJavob(models.TextChoices):
        A = '1', 'Variant A'
        B = '2', 'Variant B'
        C = '3', 'Variant C'

    sinf = models.ForeignKey(
        Sinf,
        on_delete=models.RESTRICT,
        null=True,
        verbose_name="Sinf",
    )
    savol = models.CharField(max_length=500, verbose_name="Savol matni")
    variant1 = models.CharField(max_length=200, verbose_name="Variant A")
    variant2 = models.CharField(max_length=200, verbose_name="Variant B")
    variant3 = models.CharField(max_length=200, verbose_name="Variant C")
    tjavob = models.CharField(
        max_length=1,
        choices=ToGriJavob.choices,
        verbose_name="To'g'ri javob",
    )
    image = models.ImageField(null=True, blank=True, verbose_name="Rasm")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqt")

    class Meta:
        verbose_name = "Savol"
        verbose_name_plural = "Savollar"
        db_table = 'javohir_savol'

    def __str__(self):
        return self.savol[:60]


class Natija(models.Model):
    """Foydalanuvchining test natijasi."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    sinf = models.ForeignKey(Sinf, on_delete=models.SET_NULL, null=True, verbose_name="Sinf")
    tjavob = models.IntegerField(verbose_name="To'g'ri javoblar")
    njavob = models.IntegerField(verbose_name="Noto'g'ri javoblar")
    jamisavol = models.IntegerField(verbose_name="Jami savollar")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Sana")

    class Meta:
        verbose_name = "Natija"
        verbose_name_plural = "Natijalar"
        ordering = ['-date']
        db_table = 'javohir_natija'

    def __str__(self):
        return f"{self.user.username} - {self.sinf} - {self.tjavob}/{self.jamisavol}"

    @property
    def foiz(self):
        """To'g'ri javoblar foizi (0–100)."""
        if self.jamisavol > 0:
            return round(self.tjavob / self.jamisavol * 100)
        return 0


class Bitik(models.Model):
    """Motivatsion iqtibos (sahifa dekoratsiyasi uchun)."""

    matn = models.CharField(max_length=500, verbose_name="Iqtibos matni")
    muallif = models.CharField(max_length=200, verbose_name="Muallif")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    class Meta:
        verbose_name = "Iqtibos"
        verbose_name_plural = "Iqtiboslar"
        db_table = 'javohir_bitik'

    def __str__(self):
        return f"{self.matn[:50]} — {self.muallif}"
