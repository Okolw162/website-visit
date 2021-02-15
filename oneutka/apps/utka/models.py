import datetime
from django.db import models

from django.utils import timezone

class Utka(models.Model):
	utka_title = models.CharField("Название статьи", max_length=200)
	utka_text = models.TextField("Текст статьи")
	pub_date = models.DateTimeField("Дата публикации")

	def __str__(self):
		return self.utka_title

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

	class Meta:
		verbose_name = ("статью")
		verbose_name_plural = ("статьи")


class Comment(models.Model):
	utka = models.ForeignKey(Utka, on_delete=models.CASCADE)
	author_name = models.CharField("Имя автора", max_length=50)
	comment_text = models.CharField("Текст комментария", max_length=200)

	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = ("Комментарий")
		verbose_name_plural = ("Комментарии")