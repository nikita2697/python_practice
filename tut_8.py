mystr="nikita is good girl. what about you?"
mystr1="1254"
print(mystr)
print(mystr[0])
print(mystr[0:4])#string slicing 0 include 4 exclude
print(len(mystr))
print(mystr[0:19])

print(mystr[0:19:2])#advanced slicing
print(mystr[0::2])
print(mystr[::])

#negative indices read string reverse from -1
print(mystr[-1])
print (mystr[-4:-2]) #include -4 exclude -2
print(mystr[::-1])#reverse string

#string functios
#isalpha - chcks are all alphabates
#isalnum - alphabates or numeric
#isnumeric - numeric value
#endswith
print(mystr1.isalnum())
print(mystr1.isalpha())
print(mystr1.isnumeric())
print(mystr.endswith("girl"))
print(mystr.count("g"))
print(mystr.capitalize()) # first lettr capitl
print(mystr.find("girl")) #girl strt from 15 th index