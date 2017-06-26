import tweepy
#----------------AUTH ZONE------------------#
consumer_key = "your-consumer-keu"
consumer_secret = "your-consumer-secret"

access_token = "your-access-token"
access_token_secret = "your-access-token-secret"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#me is a User object that represents actual user connected to API
me = api.me()
#----------------AUTH ZONE------------------#

#----------------ACTUAL CODE------------------#
#profile_image_url attribute is a very low quality profile image
worse_photo_url = me.profile_image_url
#You can use following code to get high quality profile image instead of above
better_photo_url = follower.profile_image_url[:63]+follower.profile_image_url[70:]

print("Worse URL :"+worse_photo_url)
print("Better URL :"+better_photo_url)


