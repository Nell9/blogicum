from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    is_published = models.BooleanField(
        verbose_name=_('Опубликовано'),
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(_("Добавлено"), auto_now_add=True)

    class Meta:
        abstract = True


class Location(BaseModel):
    name = models.CharField(
        _("Название места"),
        max_length=256
    )

    class Meta:
        verbose_name = _("местоположение")
        verbose_name_plural = _("Местоположения")

    def __str__(self):
        return self.name


class Category(BaseModel):
    title = models.CharField(
        verbose_name=_("Заголовок"),
        max_length=256
    )
    description = models.TextField(
        verbose_name=_("Описание"),
        max_length=1024
    )
    slug = models.SlugField(
        verbose_name=_("Идентификатор"),
        unique=True,
        help_text='Идентификатор страницы для URL; '
        'разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )

    class Meta:
        verbose_name = _("категория")
        verbose_name_plural = _("Категории")

    def __str__(self):
        return self.title


class Post(BaseModel):
    title = models.CharField(
        verbose_name=_("Заголовок"),
        max_length=256
    )
    text = models.TextField(
        verbose_name=_("Текст"),
    )
    pub_date = models.DateTimeField(
        verbose_name=_("Дата и время публикации"),
        help_text='Если установить дату и время в '
        'будущем — можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Автор публикации"),
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Местоположение"),
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Категория"),
    )

    class Meta:
        verbose_name = _("публикация")
        verbose_name_plural = _("Публикации")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"post_id": self.pk})
