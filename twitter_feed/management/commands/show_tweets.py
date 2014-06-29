from django.core.management.base import BaseCommand

from twitter_feed.models import Tweet


class Command(BaseCommand):
    help = 'Show the current tweets saved in db - for debugging purpose'

    def handle(self, *args, **options):
        for tweet in Tweet.objects.all():
            print "*************************"
            print tweet.published_at
            print tweet.content