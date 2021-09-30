# K06 README
Lucas Tom-Wong, Naomi Narnajo

SoftDev

K06 -- occupation -- README

2021-09-29

# File I/O
- we used `csv.reader()` method to take input from the from the csv file
  - used commas as delimters to split the information in each row 
  - used quoatation marks as our quotechar
- the occuapation and its percentage were then stored in a list called row 
- added the two elements in the row list as a value and key pair into a dictionary


# Dictionaries
- useful when one wants to access data in pairs
  - information is stored in key and values pairs
  - the value can be accessed via the key
  - key and value pairs are maintained in the order in which they are added

# Lists 
- ordered collection of values, which can be of different data types
  - indexed starting from 0

# Weighted Random Selection
- create a random number between 0 and the probability of all possible answers
  - if the number is less than the probability of the value's probability, return true and do something
  - otherwise, remove the value from the list of possibilities as well as subtract the value's probability from the total probability 
  - repeat for all values if false.

# Github-flavoured markdown
- make text easier to read, easier than HTML
  - headings created by adding "#" before texts 
  - you can change the size of the heading based on the number of "#", with "##" being smaller then "#" and so forth 
  - bulleted lists make by “*” put before text 
  - bolded sentenced or phrases are made by adding “**” before text 
  - to add links in Markdown, put the text you want linked in brackets and the link in parenthesis after. 
