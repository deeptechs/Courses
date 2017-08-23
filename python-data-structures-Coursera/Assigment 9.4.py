# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

my_dict = dict()
for line in handle:
    word = line.split()
    if len(word) > 0:
        for i in range(len(word)):
            if word[i] == 'From' and len(word) > i:
                my_dict[word[i + 1]] = my_dict.get(word[i + 1], 0) + 1

max_sent_val = 0
for key, value in my_dict.items():
    if my_dict[key] >= max_sent_val:
        max_sent_val = my_dict[key]
        max_sent_key = key

print(max_sent_key, my_dict[max_sent_key])
