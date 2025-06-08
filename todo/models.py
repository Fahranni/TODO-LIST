from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)  

    def __str__(self):
        return self.name

PRIORITY_CHOICES = [
    ('low', 'low'),
    ('medium', 'medium'),
    ('high', 'high'),
]

STATUS_CHOICES = [
    ('pending', 'pending'),
    ('completed', 'completed'),
]

CATEGORY_CHOICES = [
    ('work', 'Work'),
    ('personal', 'Personal'),
    ('study', 'Study'),
    ('shopping', 'Shopping'),
    ('health', 'Health'),
   
]

category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='personal')


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='pending')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='medium')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='personal')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
