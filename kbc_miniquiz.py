# CODE CAN BE DEVELOPED FURTHER...........

name = input("Please Enter your name: ")
print(f"\nWelcome to Kaun Banega Crorepati {name}! Lets start the game.\n")
print('''Question 1 -------> ₹1000
Question 2 -------> ₹2000
Question 3 -------> ₹5000
Question 4 -------> ₹10000 (safe space)
Question 5 -------> ₹20000
Question 6 -------> ₹50000
Question 7 -------> ₹75000
Question 8 -------> ₹100000 (safe space)
Question 9 -------> ₹200000
Question 10 -------> ₹500000
Question 11 -------> ₹1000000 (safe space)
Question 12 -------> ₹2000000''')
qna = [["Raulane fesival is celebrated in which state of India?","Himachal Pradesh","Uttar Pradesh","Uttarakahnd","Maharashtra","a"],
       ["Which is the highest shiva temple located in India?","Kedarnath","Rudranath","Tunganath","Kalpeshwar","c"],
       ["Which human made interstellar object has travelled 1 light day as of 2026?","Hubble", "Voyager 1","NASA","ISRO","b"],
       ["Dhari devi temple is situated in the middle of which river?","Alakananda","Ganga","Yamuna","Bhagirathi","a"],
       ["Which avatar of Lord Vishnu killed Ravana?","Krishna","Shri Ram","Narasimha","Vamana","b"],
       ["Badrinath temple is situated in which state of India?","Assam","Himachal Pradesh","Kashmir","Uttarakhand","d"],
       ["Which state is also called the Dev Bhoomi?","Uttarakhand","Odisha","Gujarat","Tripura","a"],
       ["How many brains does an octopus have?",4,5,9,12,"c"],
       ["The moons of Uranus planet are named after characters written by which poet?","Shakespeare","Wordsworth","John Milton","Alice Oswald","a"],
       ["Which galaxy is closest to The Milky Way Galaxy?","Triangulum","Whirlpool","Andromeda","Pinwheel","c"],
       ["Which city is known as the pink city of India?","Bangalore","Mumbai","Pune","Jaipur","d"],
       ["Which material is widely used in chip manufacturing?","Boron","Silicon","Aluminium","Gold","b"]]
money = [1000,2000,5000,10000,20000,50000,75000,100000,200000,500000,1000000,2000000]

money_earned=0

for i in range(0,len(qna)):
    print(f"\nQuestion for ₹{money[i]}")
    print(f"\nQuestion {i+1}: {qna[i][0]}\n")
    print(f"Option A: {qna[i][1]}                Option B: {qna[i][2]}")
    print(f"Option C: {qna[i][3]}                  Option D: {qna[i][4]}")
    print("Please choose your answer. If you want to quit, enter 'quit'")

    # if(i==3):
    #     money_earned=10000
    # elif(i==7):
    #     money_earned=100000
    # elif(i==10):
    #     money_earned=1000000
    
    ans = input().lower()
    if(ans.lower()=="quit"):
        print("You have chose to quit.")
        print(f"You have won {money_earned} rupees.")
        break
    elif(qna[i][5].lower() == ans):
        if(i == len(qna)-1):
            print("Correct answer!")
            print(f"Congratulations {name} you have won the game with {money[i]} rupees!")
            break
        print("Correct answer!")
        print("Lets move on to next question")

        # logic for actual money earned
        if(i==3):
            money_earned=10000
        elif(i==7):
            money_earned=100000
        elif(i==10):
            money_earned=1000000
        #money_earned = money[i]

    else:
        print(f"Its the wrong answer. You have won {money_earned} rupees")
        break
    

