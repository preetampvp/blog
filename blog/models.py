import uuid
from django.contrib.auth.models import User
from django.db import models
from tinymce import models as tinymce_models

BLOG_STATE_CHOICES = (
    ('draft', 'DRAFT'),
    ('published', 'PUBLISHED'),
    ('archived', 'ARCHIVED'),
)


class Blog(models.Model):
    """
    Blog Model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(blank=False, null=False, max_length=300)

    slug = models.SlugField(blank=False, null=False,
                            unique=True, max_length=250)

    short_description = tinymce_models.HTMLField(
        blank=True, null=True, max_length=2000)

    content = tinymce_models.HTMLField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now=True)

    state = models.CharField(
        max_length=20,
        choices=BLOG_STATE_CHOICES,
        default=BLOG_STATE_CHOICES[0][0])

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title} - {self.author} - {self.created_date}'
