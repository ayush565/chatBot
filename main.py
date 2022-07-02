from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import random

bot = ChatBot("Sam")

convo = {
    'greetings': [
        'Hey', 'Hello', 'Hi', "It's great to see you", 'Nice to see you', 'Good to see you', 'hey', 'hi'
    ],
    'bye': [
        'Bye', 'Bye-Bye', 'Goodbye', 'Have a good day', 'Taking leave', 'bye', 'goodbye'
    ],
    'thank_you': [
        'thanks a bunch', 'thanks a lot.', 'thank you very much', 'thanks so much',
        'thank you so much', 'thanks', 'thank you'
    ],
    'thank_response': [
        'You\'re welcome.', 'No problem.', 'No worries.', ' My pleasure.', 'Glad to help.'
    ],
    'query': [
        'query', 'i have a query', 'i need help', 'guidance', 'assistance', 'help', 'need help', 'need assistance'
    ],
    'query_response': [
        'Yes please ask'
    ],
    'query2': [
        'taste', 'bad', 'taste is bad', 'poor', 'poor quality', 'bad quality', 'bad taste', 'quality not good',
        'taste not good', 'food not good'
    ],
    'query2_response': [
        'Sorry for your bad experience! How can I help?'
    ],
    'query3': [
        'refund my money', 'i want refund', 'refund', 'i want my money back', 'money back', 'refund money',
        'provide refund',
    ],
    'query3_response': [
        'Ok sir we will refund half amount', 'Sure sir', 'Sorry! we cannot refund you money',
        'Sure we will try our best'
    ],
    'query4': [
        'ok', 'k', 'ok!'
    ],
    'query5': [
        'package', 'package issue', 'issue', 'order issue', 'order', 'i am having package issue',
        'i am having package issues'
    ],
    'query6': [
        'till when', 'when will i get refund', 'when', 'time to refund?', 'when?', 'till when?'
    ],
    'query6_response': [
        'Within 4-5 hours', 'We will try to provide as soon as possible'
    ],
    'query7': [
        'why', 'why so', 'why?', 'why so?'
    ],
    'query7_response': [
        'service not available at the moment', 'Sorry!! cannot help'
    ],
    'fb': [
        'feedback'
    ],
    'positive': [
        'how much would ypu rate our service out of 5 (rate >2)'
    ],
    'negative': [
        'how much would ypu rate our service out of (0<=rate<3)'
    ],
    'rate': [
      '0', '1', '2', '3', '4', '5'
    ],
    '0': [
        'Sorry for your bad experience', 'That is sad that you did not like our service'
    ],
    '1': [
        'We will try to improve', 'Oops!! Sorry for bad experience', 'Sincere apologies for our bad service'
    ],
    '2': [
        'Sad to know that you are not satisfied with our service', 'We will try to improve'
    ],
    '3': [
        'We will make sure you get better service next time',
    ],
    '4': [
        'That is great that you liked our service', 'Nice! that you liked it'
    ],
    '5': [
        'We are glad that you liked our service', 'That is awesome'
    ]
}

trainer = ListTrainer(bot)
trainer.train(convo)

main = Tk()
main.geometry("500x600")
main.title("Chatbot")
img = PhotoImage(file="chatbot.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)


def ask_from_bot():
    query = textF.get()
    query = query.lower();
    msgs.insert(END, "you: " + query)
    if(query not in convo['bye']):
        if(query == 'start'):
            bot_resp = "Hi! There. I am Service bot.My name is Sam"
            msgs.insert(END, "bot: " + str(bot_resp))
            msgs.insert(END, "Type  Hi to greet" + "  ; " + "Type  Bye to Exit.")
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query in convo['thank_you']):
            bot_resp = random.choice(convo['thank_response'])
            msgs.insert(END, "bot: " + str(bot_resp))
            msgs.insert(END, "Type query for query" + " ; " + "Type bye to exit")
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query in convo['greetings']):
            bot_resp = random.choice(convo['greetings'])
            msgs.insert(END, "bot: " + str(bot_resp))
            msgs.insert(END, "Type query for query"+" ; "+"Type bye to exit")
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query in convo['query']):
            bot_resp = random.choice(convo['query_response'])
            msgs.insert(END, "bot: " + str(bot_resp))
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query in convo['query2']):
            bot_resp = random.choice(convo['query2_response'])
            msgs.insert(END, "bot: " + str(bot_resp))
            msgs.insert(END, "type refund to get refund"+" ; "+"type feedback to give feedback")
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query in convo['query3']):
            bot_resp = random.choice(convo['query3_response'])
            msgs.insert(END, "bot: " + str(bot_resp))
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query in convo['query4']):
            bot_resp = random.choice(convo['thank_response'])
            msgs.insert(END, "bot: " + str(bot_resp))
            msgs.insert(END, "type bye to exit "+" ; "+" type query for query")
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query in convo['query5']):
            bot_resp = random.choice(convo['query2_response'])
            msgs.insert(END, "bot: " + str(bot_resp))
            msgs.insert(END, "type refund to get refund" + " ; " + "type feedback to give feedback")
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query in convo['query6']):
            bot_resp = random.choice(convo['query6_response'])
            msgs.insert(END, "bot: " + str(bot_resp))
            msgs.insert(END, "type bye to exit"+" ; "+"type feedback to give feedback")
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query in convo['query7']):
            bot_resp = random.choice(convo['query7_response'])
            msgs.insert(END, "bot: " + str(bot_resp))
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query in convo['fb']):
            msgs.insert(END, "type positive" + " ; " + "or type negative")
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query == 'positive'):
            bot_resp = random.choice(convo['positive'])
            msgs.insert(END, "bot: " + str(bot_resp))
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query == 'negative'):
            bot_resp = random.choice(convo['negative'])
            msgs.insert(END, "bot: " + str(bot_resp))
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query == '0'):
            bot_resp = random.choice(convo['0'])
            msgs.insert(END, "bot: " + str(bot_resp))
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query == '1'):
            bot_resp = random.choice(convo['1'])
            msgs.insert(END, "bot: " + str(bot_resp))
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query == '2'):
            bot_resp = random.choice(convo['2'])
            msgs.insert(END, "bot: " + str(bot_resp))
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query == '3'):
            bot_resp = random.choice(convo['3'])
            msgs.insert(END, "bot: " + str(bot_resp))
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query =='4'):
            bot_resp = random.choice(convo['4'])
            msgs.insert(END, "bot: " + str(bot_resp))
            textF.delete(0, END)
            msgs.yview(END)
            return
        elif (query == '5'):
            bot_resp = random.choice(convo['5'])
            msgs.insert(END, "bot: " + str(bot_resp))
            textF.delete(0, END)
            msgs.yview(END)
            return
        else:
            msgs.insert(END, "bot:" + str("Sorry!! can't understand"))
            msgs.insert(END, "1. Please type start to know about chatbot")
            msgs.insert(END, "2. Please type hi or any other greeting to greet")
            msgs.insert(END, "3. Please type thank you or similar word to thank")
            msgs.insert(END, "4. Please type query to register query")
            msgs.insert(END, "5. Please type bye to exit")
            textF.delete(0, END)
            msgs.yview(END)
            return
    else:
        bot_resp = random.choice(convo['bye'])
        msgs.insert(END, "bot:" + str(bot_resp))
        main.after(2000, lambda: main.destroy())
        textF.delete(0, END)
        msgs.yview(END)
        return


frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)
msgs.insert(END, 'Type start to know about bot and guidance')
btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


def enter_function(event):
    btn.invoke()


main.bind('<Return>', enter_function)
main.mainloop()
