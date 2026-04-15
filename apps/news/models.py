from django.db import models

class News(models.Model):
    """
    This model for create news
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    created_at = models.DateField()

    class Meta:
        verbose_name = "new"
        verbose_name_plural = "news"
        ordering = ['-created_at']
        db_table = 'news'

    def __str__(self):
        return self.title