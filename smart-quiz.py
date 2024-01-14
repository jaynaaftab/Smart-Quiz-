import time

def is_int(user_answer):
    try:
        int(user_answer)
        return True
    except ValueError:
        return False
   
def int_validation(user_answer):
    while is_int(user_answer) == False:
        user_answer = input("You put in the wrong data type! Reenter your value:  \n")
    return int(user_answer)


def bool_check(user_answer):
    while not user_answer in ('True', 'False'):
        user_answer = input("Your response must be either 'True' or 'False'. Type it again: \n").capitalize() 
    return user_answer
   
def multiple_choice_check(user_answer):
    while not user_answer in ("A", "B", "C", "D"):
        user_answer = input("This answer is not one of the options. Please provide a new answer: \n").upper()
    return user_answer
   
def answer_check(index, user_answer):
    answer = correct_answers[index]


    if user_answer == answer:
        print("Your answer is correct! The answer was:", answer)
        user_correct.append(1)
       


    else:
        print("Your answer is incorrect! The answer was:", answer)
   

print('Emerging Technologies Quiz') 


correct_answers = ["False", "A", "C", "D", "False", "A" "False", "False", "C", "B", "A"]
user_correct = []
questions = ["1. True or False: All IoT devices require the Internet to perform their task of communication to another source. \n",
             "2. Multiple Choice: Which of the following is NOT a characteristic of wireless IoT connectivity? \n A: Wireless connectivity is much more expensive than wired connectivity due to the modern nature of it \n B: Wireless IoT connections are, on a physical level, much easier to set up than a wired connection \n C:  Wireless connections are slower in speed of connection than wired connections \n D: The speed of wireless connections can be impacted by physical objects such as walls or floors\n",
             "",
             "3. Multiple Choice: What defines an IoT device (what makes an IoT device an IoT device in particular?) \n A: A digital device that has the general capability of connecting to the Internet \n B: Is a device that is used solely by large organizations to aid in their complex work. \n C: C: A device that contains hardware components such as processors, sensors, and communication systems that allow the device to act on the necessary information provided \n D: A measure of how well a thing (device) can connect to the internet \n",
             "",
             "4. Multiple Choice: Which of the following devices has the longest average lifespan? \n A: Smartphone \n B: B: Refurbished smartphone \n C: Router \n D: Refurbished Smart TV \n",
             "5. True or False: Most devices cannot be recycled safely due to their technical nature, so donation is the best option to be environmentally conscious \n",
             "6. Multiple Choice: Which of the following metals commonly found in devices is the safest for use in devices? \n A: Palladium \n B: Tin \n C: Lithium  \n D: Cobalt \n",
             "7. True or False: All aspects of work, including methodologies for keeping track of work and the process itself of getting a job’s work done have been entirely changed because of the advancements in technology \n",
             "",
             "8. True or False: Education requirements are much lower in comparison to in the past to get a job because technology makes jobs much easier to work through \n",
             "9. Multiple Choice: Which of the following types of AI technology refers to Artificial intelligence software that simulates human brain activity through adhering to a human’s environment, context, intent, etc.\n A: A: Deep Learning \n B: Chatbot \n C: Cognitive Computing \n Zero-shot learning \n",
             "10. Multiple Choice: Which of the following is NOT true about AI? \n A: AI can only be trained through human sources to do its needed tasks \n B:  AI can provide credible sources for all information derived from its platform \n C:  Personal data put into Artificial Intelligence is not fully secure /n D:  Data put into AI cannot be removed from its platform easily, even if it can be put in easily in the first place \n",
             "",
             "11. Multiple Choice: Which of the following situations does NOT fall under a computer ethics statement? \n A: Looking up an inappropriate topic on a search engine with a computing device \n B: Using a franchise’s company name and claiming it as your own to create a business \n C: Using information found on a blog on a published research paper created solely on one’s own",]

index = 0



for question in questions:
    if ('Multiple Choice') in question:
        time.sleep(1)
        question = input(question).upper()
        question = multiple_choice_check(question)
        answer_check(index, question)
        index += 1
   
    elif ('True or False') in question:
        time.sleep(1)
        question = input(question).capitalize()
        question = bool_check(question)
        answer_check(index, question)
        index += 1
   
    elif ('number') in question:
        time.sleep(1)
        question = input(question)
        question = int_validation(question)
        answer_check(index, question)
        
    print("") 



score = sum(user_correct)
print("Your final score is:", score, "/ 11")
