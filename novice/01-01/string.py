#string
print ('spam egg')
print ('doesn\t')
print ("doesn't")
print ('"Yes," they said.') 
print ("\"Yes,\" they said.")
print ('"Isn\'t," they said.')
print ('_____________________')

print ('"Isn\'t," they said.')
s = 'First line.\nSecond line.'
print (s)
print ('_____________________')

#special character
print ('C:\some\name')
print (r'C:\some\name')
print ('_____________________')

#multiple line
print("""\
Usage: thingy [OPTIONS]
    -h                      DIsplay this usage message
    -H                      Hosname to connect to
""")
print ('_____________________')

#glued thogether
print ("#3 times 'un', followed by 'ium'")
print (3*'un' + 'ium')
print ('_____________________')

print ('Py' 'thon')
print ('_____________________')

#break long string
text = ('put several string within parentheses'
        'to have them joined together.')
print (text)
print ('_____________________')

prefix ='Py'
print (prefix + 'thon')
print ('_____________________')

#counting number
word ='Python'
print (word[0])
print (word[5])
print (word[-1])
print (word[-2])
print (word[-6])
print (word [0:2])
print (word[2:5])
print (word[:2] + word [2:])
print (word[:4] + word [4:])
print ('_____________________')

print (word[:2])
print (word[4:])
print (word[-2:])

print (word[4:42])

print ('J' + word[1:] )
print (word [:2] + 'py')

s = 'supercalifragilisticexpialidocious'
print (len(s))