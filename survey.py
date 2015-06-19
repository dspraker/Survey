__author__ = 'David'

#create dictionary of questions to be filled in based on user input
names = {
    'myname': 'David'
}

user_questions = {
    'samplequestion': 'What is a sample question?'
}

# Create dictionary of answers
answers = {
    'testquestion': 'Test answer'
}


#Create a class to collect the user attributes
class User():
    def __init__(self, sillygirl):
        self.sillygirl = sillygirl

    def personalinfo(self):

        print "What is your name?"
        username = raw_input('> ')
        names['user'] = username

        print "Hello, ", names['user']

        print " To find out how much your friends " \
              "know about you, we first need to find out a little" \
              "more information."

        print "/n" \
              "ok - let's start with what you like. What is your" \
              "favorite TV show?"
        tv = raw_input('> ')
        user_questions['tv'] = tv


        print "Wow! That is a great show. You have excellent " \
              "taste. Now, what is your favorite ice cream flavor?"
        icecream = raw_input('> ')
        user_questions['icecream'] = icecream

        print "That is so cool! That is my favorite flavor, too. " \
              "Let's keep going. What is your address?"
        address = raw_input('. ')
        user_questions['address'] = address

        print "Hmmmmm....I don't know where that is, but I bet" \
              "your friends do. Just a couple of more questions and we'll" \
              "have the friend test ready for them to take it." \
              "What kind of animal do you wish you had for a pet?"
        pet = raw_input('> ')
        user_questions['pet'] =  pet




#Create class that lists the questions for Personality
class Personality():
    def __init__(self, question):
        self.question = question

    def tvshow(self):
        print "What is %s's favorite TV show?" % username
        action = raw_input("> ")
        if action == "yes!":
            print "It worked!!!!"
        else:
            print "try again"
            answers['tv'] = action


# call methods owned by virtual objects to ask questions
Start = User("sillygirl")
Start.personalinfo()

Q1 = Personality("question")
Q1.tvshow()

#confirm contents of dictionary
print "The answer dictionary contents are ", answers
print "The user dictionary contents are ", user_questions

print "Finished"