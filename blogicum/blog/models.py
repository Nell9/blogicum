from django.db import models
from django.utils.translation import gettext_lazy as _

class Post(models.Model):

    title = models.CharField('Название', max_length=256)
    text = models.TextField('Описание')
    pub_date = models.DateTimeField("Дата публикации")
    author = models.ForeignKey()
    
    class Meta:
        verbose_name = _("Пост")
        verbose_name_plural = _("Посты")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
