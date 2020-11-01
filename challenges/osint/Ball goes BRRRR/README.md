# Ball goes BRRRR

Category: OSINT
Difficulty: Medium
Author: Solopie

Pre-requisite challenges: "First day at uni!", "To Kill a Blue Bird"

## Challenge Description

You're finally making progress on your Java assignment when you hear a messenger notification.

"DUDE you're actually a genius! How the heck did you find his twitter account LOL. Hey I have another favour to ask you. I'll actually pay you like 5 bucks this time. could you tell me where he plays basketball? i needa get something from him and he's not replying. cheers mate"

Sigh. You stare at the message, slightly annoyed but surprisingly a bit proud.

"I think I'm actually starting to enjoy this..."

Objective: Find what suburb Jeffery plays basketball in
Flag format: hackmac{<suburb>}

## Writeup

Scroll through Jeffery's likes on twitter and you will see Ultimate Basketball posts. This is a NSW team and since you know Jeffery studys in NSW you can determine that Jeffery might have a connection to the posts.

Looking at the actual posts they're basketball game replays at a court in NSW. Going to the ultimate basketball site you can find the location of the court that they use.

https://parramattawildcats.basketball/location/



## Flag

hackmac{auburn}


