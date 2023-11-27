from django.db import models


class Task(models.Model):
    description = models.TextField(verbose_name='Описание', blank=False)
    status_choices = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
    ]
    status = models.CharField(verbose_name='Статус', max_length=20, choices=status_choices, default='new')
    due_date = models.DateField(verbose_name='Дедлайн', blank=True, null=True)