from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
    ]
    description = models.TextField(verbose_name='Описание', blank=False)
    status = models.CharField(verbose_name='Статус', max_length=20, choices=STATUS_CHOICES, default='new')
    due_date = models.DateField(verbose_name='Дедлайн', blank=True, null=True)