
file_text=open("bankaccount.txt").read()


sum=0
for n in file_text:
    if n=='C' or n=='G':
       sum=sum+1 
print "There are", sum, "C or G characters in a string of", len(file_text)-1
print "The percentage of C and G characters in the file is", 100.00*sum/(len(file_text)-1),"%"
