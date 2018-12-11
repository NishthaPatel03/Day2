import re

sentence='Dogs and Cats are Domestic animals,I love dogs.'

#match()

matched=re.match(r'Cats',sentence)
#print(matched.group()) #error,match only matches at beginning of sentence.


#findall()

print(re.findall(r'dog',sentence)) #casesensitive.


#search
sentence1='Dogs and Cats are Domestic animals,I love Dogs.'
print(re.search(r'Dog',sentence)) #restrict search to only first occurence

