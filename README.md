# Extermely simple instagram followers booster
it uses an old strategy of following famous people then waiting 
half an hour then unfollowing (rinse and repeat)

but manually doing that is boring and not fun so instead we can use a library to access instagrams's api (Instagrapi) to follow and unfollow without human intervention


## Setup 

Setting up everything is easy all we gotta do is install instagrapi and 
export environment variables to define username and password like this.

```
pip install instagrapi
export INSTAUSERNAME="insert username here"
export INSTAPASSWORD="insert password here"
```
You can use my envsetup script or use the commands above, it should work on linux and MacOS

then you can execute ```python3 instaboost.py```

## Warning 

I haven't wrote python in a good while and i haven't implemented any kinda of exception handling or safety in any way and im not responsible if instagram bans your account so use at your own risk.
