from django.db import models

class KnittingPattern(models.Model):
    """Модель для схем вязания"""
    DIFFICULTY_CHOICES = [
        ('easy', 'Легко'),
        ('medium', 'Средне'),
        ('hard', 'Сложно'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, verbose_name='Сложность')
    yarn_type = models.CharField(max_length=100, verbose_name='Тип пряжи')
    needle_size = models.CharField(max_length=50, verbose_name='Размер спиц')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    class Meta:
        verbose_name = 'Схема вязания'
        verbose_name_plural = 'Схемы вязания'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class YarnType(models.Model):
    """Модель для типов пряжи"""
    name = models.CharField(max_length=100, verbose_name='Название')
    composition = models.CharField(max_length=200, verbose_name='Состав')
    thickness = models.CharField(max_length=50, verbose_name='Толщина')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за моток')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    
    class Meta:
        verbose_name = 'Тип пряжи'
        verbose_name_plural = 'Типы пряжи'
    
    def __str__(self):
        return self.name


class Tutorial(models.Model):
    """Модель для уроков вязания"""
    title = models.CharField(max_length=200, verbose_name='Название урока')
    content = models.TextField(verbose_name='Содержание')
    video_url = models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')
    duration = models.IntegerField(help_text='Продолжительность в минутах', verbose_name='Длительность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
