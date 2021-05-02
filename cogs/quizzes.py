import discord
from discord.ext import commands, tasks
from quiz import *
from Helper import *
from latex import *

class Quizzes(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.quizzes = {}

    @commands.command()
    async def create_quiz(self, ctx, *, name):
        self.quizzes[name] = Quiz()
        await ctx.send(f'The following quiz was created: {name}')

    @commands.command()
    async def add_question(self, ctx, *, params):
        paramList = parse_inputs(params)

        quiz = paramList[0]
        qType = paramList[1]
        question = paramList[2]
        answer = paramList[3]
        
        if qType == "q":
            self.quizzes[quiz].addQuestion(question, answer)
            await ctx.send(f'Added question "{question}" to {quiz}')
        
        elif qType == "mc":
            responses = paramList[4:]
            self.quizzes[quiz].addMultipleChoice(question, int(answer), responses)
            await ctx.send(f'Added multiple choice "{question}" to {quiz}')

        elif qType == "latex":
            self.quizzes[quiz].addLatex(question, get_latex(answer))
            await ctx.send(f'Added LaTeX question {question} to {quiz}')

    @commands.command()
    async def show_response(self, ctx, *, params):
        paramsList = parse_inputs(params)
        quiz = paramsList[0]
        question = paramsList[1]
        await ctx.send(f'The answer is: {self.quizzes[quiz].revealAnswer(int(question))}')

    @commands.command()
    async def start_quiz(self, ctx, *, name):
        self.currentQuiz = self.quizzes[name]
        self.currentQuestion = -1
        self.quizChannel = await ctx.guild.create_text_channel(name, category = ctx.guild.categories[-1])

    @commands.command()
    async def next_question(self, ctx):
        if self.currentQuestion < len(self.currentQuiz.questions) - 1:
            self.answered = []
            self.currentQuestion+=1
            await self.quizChannel.send(f'Question {self.currentQuestion + 1}')
            await self.quizChannel.send(f'{self.currentQuiz.questions[self.currentQuestion]}')

        else:
            await self.quizChannel.send('End of quiz.')

    @commands.command()
    async def response_next(self, ctx):
        await self.quizChannel.send(f'The answer is: {self.currentQuiz.revealAnswer(self.currentQuestion)}')

        if self.currentQuestion < len(self.currentQuiz.questions) - 1:
            self.answered = []
            self.currentQuestion+=1
            await self.quizChannel.send(f'Question {self.currentQuestion + 1}')
            await self.quizChannel.send(f'{self.currentQuiz.questions[self.currentQuestion]}')

        else:
            await self.quizChannel.send('End of quiz.')

    @commands.command()
    async def answer(self, ctx, *, response):
        try:
            self.answered.index(ctx.author)
            await ctx.author.send('You have already answered.')

        except:
            if type(self.currentQuiz.questions[self.currentQuestion]) is MultipleChoice:
                if int(response) == self.currentQuiz.questions[self.currentQuestion].answer:
                    await ctx.author.send('Correct answer.')
        
                else:
                    await ctx.author.send('Wrong answer.')

            elif type(self.currentQuiz.questions[self.currentQuestion]) is Question:
                if response == self.currentQuiz.questions[self.currentQuestion].answer:
                    await ctx.author.send('Correct answer.')
                
                else:
                    await ctx.author.send('Wrong answer.')
                    
            elif type(self.currentQuiz.questions[self.currentQuestion]) is Latex:
                if simplify(get_latex(response) - self.currentQuiz.questions[self.currentQuestion].answer) == 0:
                    await ctx.author.send('Correct answer.')
            
                else:
                    await ctx.author.send('Wrong answer.')
            
            self.answered.append(ctx.author)

def setup(client):
    client.add_cog(Quizzes(client))