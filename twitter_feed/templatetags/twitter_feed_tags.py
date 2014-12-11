import re

from django import template
from django.utils.safestring import mark_safe

from twitter_feed.models import Tweet


register = template.Library()

hashtag_pattern = re.compile(r"(?P<start>.?)#(?P<hashtag>[A-Za-z0-9_]+)(?P<end>.?)")
username_pattern = re.compile(r"(?P<start>.?)@(?P<user>[A-Za-z0-9_]+)(?P<end>.?)")

@register.inclusion_tag('twitter_feed/latest_tweets.html')
def latest_tweets(limit=10):
    tweets = Tweet.objects.get_latest_tweets(offset=0, limit=limit)

    return {
        'tweets': tweets
    }


@register.filter
def linkify_twitter_status(status):
    # Find hashtags, replace with link to search
    link = r'\g<start><a href="https://twitter.com/hashtag/\g<hashtag>" title="#\g<hashtag> search Twitter">#\g<hashtag></a>\g<end>'
    text = hashtag_pattern.sub(link, status)

    # Find usernames, replace with link to profile
    link = r'\g<start><a href="http://twitter.com/\g<user>" title="#\g<user> on Twitter">@\g<user></a>\g<end>'
    text = username_pattern.sub(link, text)

    return mark_safe(text)


@register.filter
def url_target_blank(text):
    text = text.replace('<a ', '<a target="_blank" ')

    return mark_safe(text)
