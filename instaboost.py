from instagrapi import Client
import time


followlist = ["therock","instagram","cristiano","leomessi","selenagomez","kyliejenner","arianagrande","kimkardashian","beyonce","khloekardashian","nike","kendalljenner","justinbieber","natgeo","taylorswift"
,"virat.kohli","jlo","nickiminaj","kourtneykardash","neymarjr","mileycyrus","katyperry","zendaya","kevinhart4real","iamcardib","kingjames","ddlovato","badgalriri","realmadrid","chrisbrownofficial","champagnepapi",
"ellendegeneres","fcbarcelona","championsleague","k.mbappe","billieeilish","gal_gadot","vindiesel","lalalalisa_m","nasa","shakira","priyankachopra","dualipa","davidbeckham","shraddhakapoor","nba","snoopdogg"
,"jennierubyjane","narendramodi","aliaabhatt"]
cl=Client()
print("Logging in")
cl.login("accusername","accpass")
print("Logged in Successfully")

print("Starting following loop")
for user in followlist:
    cl.user_follow(cl.user_id_from_username(user))
    print("Followed @",user)
print("Success following now waiting for 10 seconds and then starting unfollowing")
time.sleep(30)



print("unfollow loop")
for user in followlist:
    cl.user_unfollow(cl.user_id_from_username(user))
    print("Unfollowed @",user)





print("Success")
exit(0)






