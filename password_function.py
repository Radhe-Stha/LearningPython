import random

def password_generator():

    symbol = '!,#,$,%,&,*'
    number = '1,2,3,4,5,6,7,8,9,0'
    letter = 'a,b,c,d,e,f,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
    letter_upper = letter.upper()
    
    combined = symbol+ ',' + number+ ',' + letter+ ',' + letter_upper
    combined_to_list = combined.split(",")
    #print(combined_to_list)
    random1 = random.choice(combined_to_list)
    random2 = random.choice(combined_to_list)
    random3 = random.choice(combined_to_list)
    random4 = random.choice(combined_to_list)
    random5 = random.choice(combined_to_list)
    random6 = random.choice(combined_to_list)
    random7 = random.choice(combined_to_list)
    random8 = random.choice(combined_to_list)

    password= random1 + random2 + random3 + random4 + random5 + random6 + random7 +random8
    print(password)
    


password_generator()
