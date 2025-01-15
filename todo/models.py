from django.db import models


class todo(models.Model):
    todo_title = models.CharField(max_length=2000)
