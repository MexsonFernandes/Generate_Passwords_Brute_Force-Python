import random, sys, string, argparse

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--alphabet', action='store_true', 
    help="the password contains alphabet characters")
parser.add_argument('-s', '--special', action='store_true', 
    help="the password contains special characters")
parser.add_argument('-n', '--number', action='store_true', 
    help="the password contains numbers")
parser.add_argument('-l', '--length',
    help="password length", required=True, type=int)


args = parser.parse_args()


def generate():
    N = args.length
    a= open("wordlists/wordlist"+str(N)+".txt",'w')
    b= open("logs/log"+str(N)+".txt",'w')

    list=0;
    password=''
    if args.alphabet:
        list=list+52;
        password=password+string.ascii_letters
    if args.special:
        list=list+32;
        password=password+string.punctuation
    if args.number:
        list=list+10;
        password=password+string.digits
    total=list**N#permutation for repetition N**r
    password=password*N
    print(total)
    b.write("\nGenerating password list :-"+str(total)+"\n");
    final=set([]);#to store password list
    j=0;
    print("processing...\n");
    while len(final)!=total:
    #a.write(random.sample(password,N)+"\n");
        
        final.add("".join(random.sample(password,N)))
    print(len(final))
    for i in final:
        a.write(i+"\n");	
    b.write("\n\n\nPassword generated....enjoy..Thank you for using RoboMex Service!!!");           
    a.close()
    b.close()
generate()
