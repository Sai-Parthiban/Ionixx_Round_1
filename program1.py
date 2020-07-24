#Function to print the repetition count of character/word in descending order
def sorted_count(frequency):
    #Dictionary variable to store the character/word and its repetition count
    d={}
    for i in set(frequency):
        d[i]=frequency.count(i)
    #To store the values in descending repetition count
    d=dict(sorted(d.items(),key=lambda x:(-x[1],x[0])))
    #DIsplaying the character/word along with its repetition count
    for i,j in d.items():
        print(i,"->",j)
#List to store the conversation
conversation=[]
#To get the chat from A
chat=input("A : ")
for i in chat.split():
    conversation.append(i)
#Variable to store the conversation count
conversation_count=0
while(1):
    #To check whether the cht terminates with quit or not
    if(chat!="quit" and chat!="QUIT" and chat!="Quit"):
        conversation_count+=1
        if(conversation_count%2!=0):
            #To get the chat from B
            chat=input("B : ")
            for i in chat.split():
                conversation.append(i)
        else:
            #To get the chat from A
            chat=input("A : ")
            for i in chat.split():
                conversation.append(i)
    #When the conversation terms up with quit, it terminates
    else:
        break
#To remove quit from the chat
conversation=conversation[:-1]
#Varaible to store the characters and their count of repetition
s=""
for i in conversation:
    s+=i
#Displaying the characters count
print("**** Character Count ****")
sorted_count(s)
#Displaying the word count
print("**** Word Count ****")
sorted_count(conversation)
#Displaying the length of the conversation
print("Length of Conversation :",conversation_count)

