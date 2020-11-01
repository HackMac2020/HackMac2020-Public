# Postman Pat knows everything about 13 Rotten Apples

Cateogry: OSINT
Difficulty: Hard 

## Description

Knock knock knock. It's 9PM and you hear someone quietly knocking at your door.

"What the heck who's knocking at this time?"

You minimize your dirbuster terminal and open up your camera dashboard. The light shines brightly and there you see the face of your old highschool colleague. He looked alot bigger than what you remembered and very scuffed.

"WHAT THE.... WHAT IS HE DOING HERE"

You scramble to the door and look through the peep hole.

"He's really there..."

You open one of the two security doors slowly.

"Uh hey... you're Mark right? What are you doing here?"

"YO BRO you took your time! Nah just came by to see how you doing. You've been alot of help so just thought I would thank you personally. Well, I'm gonna head off now got stuff to do, just pretend the postman came by or something."

He runs off back to a already occupied car and speeds off, music blasting down the street.

"... I don't have a good feeling about this. Something's up."


Objective: Using all the intel/resources you have currently, find a flag in the normal format.
Flag example: hackmac{this_is_a_fake_flag}

## Writeup

On Jeffery's twitter he has a follower called Aaron Boolon.

Aaron Boolon has a tweet with a website that is ROT-13 encrypted

Website leads to http://badboys.hackmac.xyz

Website has a 6 digit pin protecting the site.

Realise there are 6 numbers at the end of both Aaron's and Jeffery's emails. Using the pin grants access and there is a page with the flag.

## Flag

hackmac{hello_mr_postman}
