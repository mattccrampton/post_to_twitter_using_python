import tweepy

# See tutorial: https://www.mattcrampton.com/blog/step_by_step_tutorial_to_post_to_twitter_using_python_part_two-posting_with_photos/

def main():
    twitter_auth_keys = {
        "consumer_key"        : "REPLACE_THIS_WITH_YOUR_CONSUMER_KEY",
        "consumer_secret"     : "REPLACE_THIS_WITH_YOUR_CONSUMER_SECRET",
        "access_token"        : "REPLACE_THIS_WITH_YOUR_ACCESS_TOKEN",
        "access_token_secret" : "REPLACE_THIS_WITH_YOUR_ACCESS_TOKEN_SECRET"
    }

    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)


    # Upload image
    media = api.media_upload("william_gibson.jpg")

    # Post tweet with image
    tweet = "Great scifi author or greatest scifi author? #williamgibson"
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])

if __name__ == "__main__":
    main()
