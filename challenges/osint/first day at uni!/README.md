# First day at uni!

Category: OSINT
Difficulty: Beginner
Author: Solopie

## Challenge Description

The sunlight spills through the window as you lay in bed, scrolling through youtube recommendations on your phone. Suddenly, you get a messenger notification. An unfamiliar face pops into your screen.

"Isn't he from highschool?"

You pull down your notifications tab so that it doesn't show you've read the message.

"Yo dude! its me Mark from high school. how you been mane ive heard you been into those hacking things with all those computer nerds and stuff. anyway theres this guy that i met. im doing some uh..... special business with him and i need some info on him to check if i can trust him. Dude we only talk on instagram so that's all ive got for you. ill even you pay you bro."

Urgh. You never liked this douchebag. You've got nothing else better to do though besides your COMP.... Assignment due in 2 days..... Why not?

"Alright sure. Send me the instagram link."

Instagram Link: https://www.instagram.com/j3ff3ryth3r3f3r33/

Objective: Find what building and time Jeffery has class in

Flag format: hackmac{<building name>_<start hour><AM/PM>_<end hour><AM/PM>}
Note: Using old building name

## Writeup

Find that the university he goes to is Macquarie University with the logo in the photo
https://www.instagram.com/p/CFdg_lrlt7P-DP5XxKlobolf5PquzOWnZeYp-M0/

Going to google maps you can find the places on his way to class with streetview and find the address of the destination before he goes to class.
Post before he goes to class: https://www.instagram.com/p/CFdip6llNha_r3aSqjKmKKzn3lbhqo7ai29NzU0/

Using that post, you can find the exact time the post was made using the technique found in this post.
https://mpsocial.com/t/how-to-see-exact-time-an-instagram-post-was-made/35086

There is another post for after class which you will use to find when the class ends.
https://www.instagram.com/p/CFdpTh9log5KjoUFru3bjDG13C3YX0ZskpOZGM0/


## Flag

hackmac{E6A_12PM_1PM}


