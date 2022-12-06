my_file= open('moinul.txt','a')

# print(my_file.readlines())
 
my_file.write('im writing noice \n')

my_file.close()

my_file=open("moinul.txt")

for line in (my_file.readlines()):
    print(line,end="")


