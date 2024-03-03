from django.contrib import admin
from tweetapp.models import Tweet
# Admin sayfasının görünümünü burdan değiştirebiliriz.


class TweetAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Message group',{"fields":["message"]}),
        ('field group',{"fields":["nickname"]}),


    ]

    # fields=['message','nickname']

admin.site.register(Tweet,TweetAdmin)
