#Title and explanation of this game
print "Observation of Italian people"
print "Welcome, here you can get to know something about Italian! I'm Japanese who worked with them, half a year for working holiday. So this is my record of life with Italian people."

#Each comments for users depending on the answer typed in
correct = "Correct! Go next blank."
incorrect = "It can be suit, but this time different answer! Try again."
finish = "Congrats you finished! Was there something you didn't know and did it interest you? If you want to play once more, choose the level you try next!"

#correct answers for easy quiz
A_e = ["ice cream","kind","smile","trial","coffee","slow"]

#correct answers for medium/ hard quiz
A = [["distance","exaggerated flapping gesture","arguing","talking","scream","natural"],["gelato","friend","optimistic","emotion","respect","voice"]]

#blank numbers of all quiz
blank = ["__1__","__2__","__3__","__4__","__5__","__6__"]

#answer options
e_op = ["jerkey / speciality kangaroo / ice cream :","scary / kind / funny :","knife / pizza / smile :","gelato / canoli / triangle / trial : ","meatball / cocaine / coke / coffee : ","slaphappy / sleasy / slow : "]
m_op = ["extreme huge voice / extra fluffy gelatoes / exaggerated flapping gesture : ","jump / sleep / scream : ","handstanding / tackling / arguing : ","wrestling / skating / talking : ","natural / nasty / nutty : "]
h_op = ["sushi / gelato / sugar free ice cream : ","freakish / friend / love : ","drunk / optimistic / negative : ","ass / emotion / muscles : ","cherish / respect / cross buttock : ","voice / merda / fart : "]

#Defining easy quiz
def easy_quiz():
    #Greeting of easy quiz, it should be executed when player try this quiz for first time.
    print "Welcome to easy quiz, here how I felt when I met one Italian family for first time in Australia!\n "
    #Easy quiz sentence
    easy_q = " First day I arrived at Fremantle, I was looking for a job. This __1__ shop was 3rd which I visited to distribute resume. They seemed really __2__, with a big __3__. Manager said to me that he's gonna give me a call next day until 12pm in order to give me __4__, but I didn't get even it was already half passed 12. So I headed to the shop, then manager said 'Oh is it already 12 ? Okay first of all, let's have a __5__. next door' 'Eh? But we have __5__ machine here''Our __5__ is not delicious' That shop everyday open at 11am by the way, according to google. Such a __6__ people. But thanks to that, I felt relaxed.\n"


#_________________________________________________________________________________________________________________________________________________________________________
#Here is the code now I'm trying to make. This for loop is supposed to work instead of looong code which I wrote below. (I gonna use this for each quiz, easy medium and hard)
    '''Let i loop through each blank(from __1__ ~ __6__),
       and ask player to answer with answer options.
       If that input answer was correct, replace the blank with correct word into quiz sentence and prompt player to answer next blank.
       If that was incorrect, one more time player has to think until getting right answer. It's repeated until blank __6__.'''

    i = 0
    for i in blank:
        blank[i] = raw_input("What word suit for "+ blank[i] + "?"+ e_op[i])
        if A_e.index(blank[i]) == blank.index(blank[i]):
            easy_q = easy_q.replace(blank[i], A_e[i])
        print correct
        i += 1
#________________________________________________________________________________________________________________________________________________________________________


    '''
    easy_2 = ''
    while easy_2 != e_answers[1]:
        easy_2 = raw_input("What word suit for __2__? HINT: scary / kind / funny :")
        easy_q = easy_q.replace("__2__",e_answers[1])
    print correct

    easy_3 = ''
    while easy_3 != e_answers[2]:
        easy_3 = raw_input("What word suit for __3__? HINT: knife / pizza / smile :")
        easy_q = easy_q.replace("__3__", e_answers[2])
    print correct

    easy_4 = ''
    while easy_4 != e_answers[3]:
        easy_4 = raw_input("What word suit for __4__? HINT: gelato / canoli / triangle / trial : ")
        easy_q = easy_q.replace("__4__", e_answers[3])
    print correct

    easy_5 = ''
    while easy_5 != e_answers[4]:
        easy_5 = raw_input("What word suit for __5__? HINT: meatball / cocaine / coke / coffee : ")
        easy_q = easy_q.replace("__5__", e_answers[4])
    print correct

    easy_6 = ''
    while easy_6 != e_answers[5]:
        easy_6 = raw_input("What word suit for __6__? HINT: slaphappy / sleasy / slow : ")
        easy_q = easy_q.replace("__6__", e_answers[5])
    print easy_q
    print finish


#Medium quiz

def medium_quiz():
    print "Welcome to medium quiz, here's lessons I got about Italian while being with them\n"
    med_q = "There's Italian family, living in Australia. They have run gelato shop and the father hired me. First I have to say, you have to keep __1__ from them, at least 1m. As you might get injured by their __2__. And don't worry, they are not __3__ but just __4__. They often __5__, not only this i __5__ family but Italians often __5__ according to my observation, and it's __6__ for them. As i expected, they love to eat. Especially the father care how the dishes made, cuz he loves cooking too. His kale chips was amazing. Oh it makes my mouth water...\n"
    m_answers = ["distance","exaggerated flapping gesture","arguing","talking","scream","natural"]
    print med_q

#<First blank> If users didn't answer correctly, let them try again
    med_1 = ''
    while med_1 != m_answers[0]:
        med_1 = raw_input("What word suit for __1__? HINT: dishes / doggie / distance : ")
        med_q = med_q.replace("__1__", m_answers[0])
    print correct

    med_2 = ''
    while med_2 != m_answers[1]:
        med_2 = raw_input("What word suit for __2__? HINT: ")
        med_q = med_q.replace("__2__", m_answers[1])
    print correct

    med_3 = ''
    while med_3 != m_answers[2]:
        med_3 = raw_input("What word suit for __3__? HINT: ")
        med_q = med_q.replace("__3__", m_answers[2])
    print correct

    med_4 =''
    while med_4 != m_answers[3]:
        med_4 = raw_input("What wprd suit for __4__? HINT: ")
        med_q = med_q.replace("__4__", m_answers[3])
    print correct

    med_5 = ''
    while med_5 != m_answers[4]:
        med_5 = raw_input("What word suit for __5__? HINT: ")
        med_q = med_q.replace("__5__", m_answers[4])
    print correct

    med_6 = ''
    while med_6 != m_answers[5]:
        med_6 = raw_input("What word suit for __6__? HINT: ")
        med_q = med_q.replace("__6__", m_answers[5])
    print med_q
    print finish

#Hard quiz

def hard_quiz():
    print "Welcome to hard quiz! Here's my experience of working with lovely Italian family.\n"
    hard_q = "There was a lot of things that I didn't know until I start to work with the Italian family. For example, customers asked me if we had __1__ but not ice cream, but boss taught me that __1__ is just Italian word of ice cream, so they are the same. What I mainly felt by being with them was Italians love to be __2__ly and __3__. Sometimes __4__al, because they're very honest, don't hide their __4__. And always beautiful, cuz Italian guy __5__ woman and woman is __5__ed. I feel their soul is full of love. All the time they are ringing their friends or family with big __6__.\n "
    h_answers = ["gelato","friend","optimistic","emotion","respect","voice"]
    print hard_q

    hard_1 = ''
    while hard_1 != h_answers[0]:
        hard_1 = raw_input("What word suit for __1__? HINT: sushi / gelato / sugar free ice cream : ")
        hard_q = hard_q.replace("__1__",h_answers[0])
    print correct

    hard_2 = ''
    while hard_2 != h_answers[1]:
        hard_2 = raw_input("What word suit for __2__? HINT: ")
        hard_q = hard_q.replace("__2__",h_answers[1])
    print correct

    hard_3 = ''
    while hard_3 != h_answers[2]:
        hard_3 = raw_input("What word suit for __3__? HINT: ")
        hard_q = hard_q.replace("__3__",h_answers[2])
    print correct

    hard_4 = ''
    while hard_4 != h_answers[3]:
        hard_4 = raw_input("What word suit for __4__? HINT: ")
        hard_q = hard_q.replace("__4__",h_answers[3])
    print correct

    hard_5 = ''
    while hard_5 != h_answers[4]:
        hard_5 = raw_input("What word suit for __5__? HINT: ")
        hard_q = hard_q.replace("__5__",h_answers[4])
    print correct

    hard_6 = ''
    while hard_6 != h_answers[5]:
        hard_6 = raw_input("What word suit for __6__? HINT: ")
        hard_q = hard_q.replace("__6__",h_answers[5])
    print hard_q
    print finish
'''
choice = ''
i = 0
while i >= 0:
    choice = raw_input("Which level you wanna try? Type easy / medium / hard ! : ")
    if choice == "easy":
        print easy_quiz()
    if choice == "medium":
        print medium_quiz()
    if choice == "hard":
        print hard_quiz()
    i += 1
