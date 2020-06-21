from django.contrib.auth.models import User
from django.db import models
import uuid

BLOG_STATE_CHOICES = (
    ('draft', 'DRAFT'),
    ('published', 'PUBLISHED'),
    ('archived', 'ARCHIVED'),
)


class Blog(models.Model):
    """
    Blog Model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(blank=False, null=False, max_length=300)

    slug = models.CharField(blank=False, null=False,
                            unique=True, max_length=250)

    short_description = models.TextField(
        blank=True, null=True, max_length=2000)

    content = models.TextField(blank=True, null=True)

    created_date = models.DateField(auto_now=True)

    state = models.CharField(
        max_length=20,
        choices=BLOG_STATE_CHOICES,
        default=BLOG_STATE_CHOICES[0][0])

    author = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title} - {self.author}'
