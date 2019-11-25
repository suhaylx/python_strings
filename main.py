selfish = "I am selfish "
print (selfish[7])

print('\n')
print(selfish[:5]) #it means start from begining of string and stop at 5 char

print(selfish[::2])

print(selfish[1:9:2]) # we go from " " and then skip by 2 and next is m and next is s and l
print(selfish[::-1]) # reverse 
print(selfish[-2]) # it will print h in as its reverse order


quote = 'to be or not to be '
print(quote.upper())
print(quote.capitalize())
print(quote.isprintable())
print(quote.replace("be", "me")) 
# Never for get strings are inmutable