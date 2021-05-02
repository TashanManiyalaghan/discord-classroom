class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return self.question

class MultipleChoice:
    def __init__(self, question, answer, responses):
        self.question = question
        self.answer = answer
        self.responses = responses

    def __str__(self):
        temp = self.question

        for choice in self.responses:
            temp = temp + "\n\t\t\t" + choice
        
        return temp

class Latex:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return self.question

class Quiz:
    def __init__(self):
        self.questions = []

    def addQuestion(self, question, answer):
        q = Question(question, answer)
        self.questions.append(q)
        return
    
    def addMultipleChoice(self, question, answer, responses):
        mc = MultipleChoice(question, answer, responses)
        self.questions.append(mc)
        return

    def addLatex(self, question, answer):
        latex = Latex(question, answer)
        self.questions.append(latex)
        return

    def revealAnswer(self, number):
        if type(self.questions[number - 1]) is MultipleChoice:
            return self.questions[number - 1].responses[self.questions[number - 1].answer - 1]

        elif type(self.questions[number - 1]) is Question:
            return self.questions[number - 1].answer

        elif type(self.questions[number - 1]) is Latex:
            return self.questions[number - 1].answer

if __name__ == '__main__':
    quiz1 = Quiz()
    quiz1.addQuestion('Some kind of question.', 'Some kind of answer.')
    quiz1.addMultipleChoice('some question 2', 2, ['kwerijurnfwiuefjn', 'jwehfnwkijfeb', 'iworkujsbnfgiwubhfger', 'wriosunfgjwiufebn', 'WIRUBFGWIUFGRBN'])

    print(quiz1.revealAnswer(2))