from django.core.management.base import BaseCommand

from twitter_feed.import_tweets import ImportTweets


class Command(BaseCommand):
    help = 'Import the tweets'

    def handle(self, *args, **options):
        importer = ImportTweets()
        importer.update_tweets()