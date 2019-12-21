from django.db import models
from preferences.models import Preferences


class NavigationBarSetting(Preferences):
    first_button_text = models.CharField(max_length=200, default="<<")
    first_button_image = models.ImageField(upload_to="ComicCozy/resources/", blank=True,
                                          help_text="Leave blank to use the text above instead")
    previous_button_text = models.CharField(max_length=200, default="<")
    previous_button_image = models.ImageField(upload_to="ComicCozy/resources/", blank=True,
                                              help_text="Leave blank to use the text above instead")
    next_button_text = models.CharField(max_length=200, default=">")
    next_button_image = models.ImageField(upload_to="ComicCozy/resources/", blank=True,
                                          help_text="Leave blank to use the text above instead")
    last_button_text = models.CharField(max_length=200, default=">>")
    last_button_image = models.ImageField(upload_to="ComicCozy/resources/", blank=True,
                                          help_text="Leave blank to use the text above instead")
