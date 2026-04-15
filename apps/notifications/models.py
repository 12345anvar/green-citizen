from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    """
    This model for send notification to users
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    message = models.TextField()

    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "notification"
        verbose_name_plural = "notifications"
        ordering = ['-created_at']
        db_table = 'notifications'

    def __str__(self):
        return self.title