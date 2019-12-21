from django.db import models
from django.utils import timezone

from .preferences import NavigationBarSetting

class Comic(models.Model):
    today = timezone.datetime.today()

    title = models.CharField(max_length=200)
    post_date = models.DateTimeField(default=today, unique=True)
    path = models.ImageField("Image filepath", upload_to="ComicCozy/comics/")
    alt_text = models.CharField(max_length=200, blank=True)
    tags = models.CharField(max_length=200, blank=True)
    text = models.TextField("Post text", blank=True)

    def is_published(self):
        return self.post_date <= timezone.now()
    is_published.admin_order_field = 'post_date'
    is_published.boolean = True
    is_published.short_description = 'Published?'

    def __str__(self):
        return f"{self.title} {self.post_date}"

    class Meta:
        # Latest by ascending order_date.
        get_latest_by = "post_date"
