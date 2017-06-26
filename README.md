# Tweepy Trick for Better Profile Pictures

If you are using tweepy[https://github.com/tweepy/tweepy] to connect TwitterAPI probably you are not satisfy profile picture quality. Because TwitterAPI returns a unqualified photo url but you can change something on actual url to get better results.You can use following instead of original API result.

# What is the trick ?

For example you are trying to access profile picture of somebody you will get an URL something like this

```
https://pbs.twimg.com/profile_images/822547732376207360/5g0FC8XX_normal.jpg
```
when you go this address you will get 100x100px image but when you delete the "_normal" at the and of URL. You get a better photo

```
https://pbs.twimg.com/profile_images/822547732376207360/5g0FC8XX.jpg
```
Use this for better results instead of other.
