# Uh oh

Category: OSINT
Difficulty: Hard

## Challenge Description

You scroll through the posts on the bad boys site.

"Oh my god what the heck am I getting in to..."

There you see Jeffery's name under one of the posts. You can't believe what you just found.


Objective: Find the address of the broken car Jeffery broke in to.
Flag format: hackmac{<house number>_<street>_<suburb>}
Example: hackmac{21_beast_ave_canley_vale} where 21 is the house number, beast ave is the street and canley vale is the suburb.

## Writeup

Jeffery's blog gives specific information about the location.

"Don't know why the road is called childs lol. I went to Gu Thai Cuisine with the money that I stole"

Searching up Gu Thai Cuisine you find a resteraunt in Chipping Norton. You also find Childs Rd.

Going into streetview you can find the image of the car is the same as the one as the blog post at 86 Childs Road Chipping Norton.

## Flag

hackmac{86_childs_rd_chipping_norton}
