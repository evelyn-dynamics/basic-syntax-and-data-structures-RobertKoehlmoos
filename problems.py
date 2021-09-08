""""
We need your help to write our software that processes new users into our system
Write a program that prompts a user five times for the following information in order:
1. First Name
2. Last Name
3. Year Born
4. Month Born
5. Day Born

And print that information out in the following format:
<First Name> <Last Name> was born on <Month> <Day> in <Year>

Then print out their user id, consisting of the first four letters of their last name,
the first letter of their first name, and the day of the month they were born:
<first four of last name><first letter of first name><Day Born>
(Corporate believes there are no possible issues with this system)

Finally, print out their temporary password, consisting of the last letter of their first name,
their last name backwards, the last digit of the year they were born spelled out lowercase:
<last letter of first name><last name backwards><last digit of year born spelled out>
(Corporate insisted on user friendly passwords)

Finally, print 'Unlucky' if the user was born on the 13th, otherwise print 'Lucky'
(Don't even ask)

But, the user will provide month as a number from 1 to 12 (inclusive), you need to convert it
into the word representing the month.
For example, the below input
Scooby
Doo
1969
9
13

Would print

Scooby Doo was born on September 13 in 1969
ScooD13
yooDnine
Lucky

Don't worry, the users will only give months consisting of integers that correspond to months that actually exist.
"""
