from django.db import models
from audit_logger.decorators import audit_model

# Create your models here.
@audit_model
class About(models.Model):
    about_heading = models.CharField(max_length=25)
    about_description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_heading
    
@audit_model
class SocialLinks(models.Model):
    platform_name = models.CharField(max_length=20)
    link = models.URLField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'SocialLinks'

    def __str__(self):
        return self.platform_name