fh = open("Sample_Text.txt", "r")

#print fh.read()

text = fh.read()

#print text

print type(text)
print text.find('paploo')

if (text.find('paploo') != -1):
  print "paploo founded"
else:
  print "paploo NOT founded"


adiniz = raw_input("Adinizi Giriniz ")
print "Adiniz bu olmali", adiniz