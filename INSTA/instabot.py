from instapy import InstaPy
session = InstaPy(username ="7702726193", password ="sameer12@")
session.login()

#You can set max and min followers here
session.set_relationship_bounds(enabled = True, max_followers = 200)

#Percentage from 0 to 100. 100 if you want to follow everyone who get your likes
session.set_do_follow(True, percentage=100)

session.like_by_tags(["mubarakpur"], amount =1)
session.set_dont_like(["insta"])
session.unfollow_users(amount=160, allFollowing=True, sleep_delay=60)
session.end()

