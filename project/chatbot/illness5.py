asking=input("Welcome Sir how can help you ?\n")
desc=input("can you describe me your illness: i have ")
z=len(desc)
a=desc.find(",")
b=desc[0:a]
o=b.find(",")
p=desc[a+1:]
y=p.find(",")
c=p[0:y]
j=p[y+1:]
#print(b)
#print(c)
#print(j)
#b==""or c=="" or j==""
#Describing 
if (b or c or j) in ["fever","headache","a dry cough"]:
    l1=input("Do you feel Intense exhaustion ?\n")
    if l1=="yes":
        l2=input("Do you have Stuffy or runny nose ?\n")
        if l2=="yes":
            l3=input("Did you lose your appetite and taste ?\n")
            if l3=="yes":
                print("unfortunately you are affected by the flu")
                #Advice 
                print("So what about drinking a cup of  herbal tea , covering yourself in bed and Inhaling eucalyptus")
                #notification
                nt=input("do you feel any better now ?\n")
                print("Take a Vitamin C tablet")
                nt1=input("Have you noticed any improvement?\n")
                print("would you like to drink cinnamon steeped in water")
                nt3=input("How do you feel now?\n")
                if nt3=="not good":
                    print("Would you like to subscribe to our Premuin version and talk directly to the doctor without waiting?")
                else:
                    print("finally are getting well")
#Describing 
if (b or c or j) in ["red and swollen tonsils","nausea","sore throat"]:
    l4=input("Do you have Fever ?\n")
    if l4=="yes":
        l5=input("Do you have Vomiting ?\n")
        if l5=="yes":
            l6=input("Do you have any Headache ?\n")
            if l6=="yes":
                print("unfortunately you are affected by the Strep throat")
                #Advice 
                print("So what about drinking a cup of honney with lime , covering yourself in bed and eating hot liquid foods")
                #notification
                nt4=input("do you feel any better now ?\n")
                print("Take thyme")
                nt5=input("Have you noticed any improvement?\n")
                print("Avoid drinking cold water")
                nt6=input("How do you feel now?\n")
                if nt6=="not good":
                    print("Would you like to subscribe to our Premuin version and talk directly to the doctor without waiting?")
                else:
                    print("finally are getting well")
#Describing 
if (b or c or j) in ["abdominal cramping","bloating","loose and watery stools"]:
    l7=input("Do you have Fever ?\n")
    if l7=="yes":
        l8=input("Do you fell Dehydration or dizziness and lightheadedness ?\n")
        if l8=="yes":
            l9=input("Do you have any Nausea ?\n")
            if l9=="yes":
                print("unfortunately you are affected by the Diarrhea")  
                #Advice 
                print("So what about drinking  a cup of sweetened tea , eating well-cooked rice and why not drinking a soda 😋")
                #notification
                nt7=input("do you feel any better now ?\n")
                print("Take a delicious broth")
                nt8=input("Have you noticed any improvement?\n")
                print("would you like to Partake of a Banana ")
                nt9=input("How do you feel now?\n")
                if nt9=="not good":
                    print("Would you like to subscribe to our Premuin version and talk directly to the doctor without waiting?")
                else:
                    print("finally are getting well")
#Describing 
if (b or c or j) in ["difficulty breathing","new loss of taste or smell","high temperature"]:
    l7=input("Do you have Fatigue ?\n")
    if l7=="yes":
        l8=input("Do you fell Dehydration or dizziness and lightheadedness ?\n")
        if l8=="yes":
            l9=input("Do you have any Headache ?\n")
            if l9=="yes":
                print("unfortunately you are affected by the covid-19")
                #Advice 
                print("So what about drinking a cup of  herbal tea , covering yourself in bed and Inhaling eucalyptus")
                #notification
                nt10=input("do you feel any better now ?\n")
                print("Take a Vitamin C tablet")
                nt11=input("Have you noticed any improvement?\n")
                print("would you like to drink cinnamon steeped in water")
                nt12=input("How do you feel now?\n")
                if nt12=="not good":
                    print("Would you like to subscribe to our Premuin version and talk directly to the doctor without waiting?")
                else:
                    print("finally are getting well")          
#





