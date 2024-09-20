from django.db import models
from ckeditor_uploader import fields


# Create your models here.
class ContentHtmlAbout(models.Model):
    content = fields.RichTextUploadingField(verbose_name='Контент')

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Контент для страницы "О нас"'
        verbose_name_plural = 'Контент для страницы "О нас"'