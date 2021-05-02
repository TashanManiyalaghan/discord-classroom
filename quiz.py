class Question:

    # Constructor for Question class, which will keep track of questions and answers for the question.
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    # __str__ function for the Question class which will return the question.
    def __str__(self):
        return self.question

class MultipleChoice:

    # Constructor for MultipleChoice class, which will keep track of questions, answers, and responses for the question.
    def __init__(self, question, answer, responses):
        self.question = question
        self.answer = answer
        self.responses = responses

    # __str__ function for the MultipleChoice class which will return the question and each of the choices.
    def __str__(self):
        temp = self.question
        count = 1

        for choice in self.responses:
            temp = temp + "\n\t\t\t" + str(count) + '. ' + choice
            count+=1
        
        return temp

class Latex:

    # Constructor for Latex class, which will keep track of questions and answers for the question.
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    # __str__ function for the Latex class which will return the question.
    def __str__(self):
        return self.question

class Quiz:

    # Constructor for the Quiz class which will store as an attribute a list of the questions.
    def __init__(self):
        self.questions = []

    # addQuestion function which will add a new question of the Question class to the list of questions.
    def addQuestion(self, question, answer):
        q = Question(question, answer)
        self.questions.append(q)
        return

    # addMultipleChoice function which will add a new question of the MultipleChoice class to the list of questions.
    def addMultipleChoice(self, question, answer, responses):
        mc = MultipleChoice(question, answer, responses)
        self.questions.append(mc)
        return

    # addLatex function which will add a new question of the Latex class to the list of questions.
    def addLatex(self, question, answer):
        latex = Latex(question, answer)
        self.questions.append(latex)
        return

    # revealAnswer function which will reveal the answer according to the type.
    def revealAnswer(self, number):
        if type(self.questions[number - 1]) is MultipleChoice:
            return self.questions[number - 1].responses[self.questions[number - 1].answer - 1]
        elif type(self.questions[number - 1]) is Question:
            return self.questions[number - 1].answer
        elif type(self.questions[number - 1]) is Latex:
            return self.questions[number - 1].answer

    def showQuestion(self, number):
        if type(self.questions[number - 1]) is Latex:
            return self.questions[number - 1].question
        else:
            return self.questions[number - 1].question