django-twitter-feed
===================

Really simple app to show a Twitter feed in your Django application.

It's using a a task to update the feed regularly.


Set-up:
-------

1.Add it to your "INSTALLED_APPS" settings:

    INSTALLED_APPS = (
        ...
        'twitter_feed',
        ...
    )

2.Add your twitter account API access in the settings like this:

    TWITTER_FEED_CONSUMER_PUBLIC_KEY = '...'
    TWITTER_FEED_CONSUMER_SECRET = '...'
    TWITTER_FEED_OPEN_AUTH_TOKEN = '...'
    TWITTER_FEED_OPEN_AUTH_SECRET = '...'

3.Run `python manage.py migrate` (if you use South) or `python manage.py syncdb`

4.Run the following command lines to test your Twitter credentials and save the initial feeds:
* `python manage.py update_tweets`
* `python manage.py show_tweets`

5.In a template, show the latest 10 tweets for example:

    {% load twitter_feed_tags %}
    {% latest_tweets 10 %}

6.Customise the template - simply create a copy of `twitter_feed/latest_tweets.html` and edit it.

For example:

	{% load twitter_feed_tags %}

	<div class="tweets">
    	{% for tweet in tweets %}
	      <div class="tweet">
    	    <p>{{ tweet.content|linkify_twitter_status|urlize|url_target_blank }}</p>
        	<p class="date">{{ tweet.published_at|date:"F d, Y" }}</p>
	      </div>
    	{% endfor %}
	</div>
	
7.Make sure `python manage.py update_tweets` is regurlalry called.