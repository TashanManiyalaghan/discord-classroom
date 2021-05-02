# Discord.py, Discord.ext, Quiz classes, and Helper function imports.
import discord
from discord.ext import commands
from quiz import *
from Helper import *

class Quizzes(commands.Cog):

    # Constructor for the Quizzes cog, which will store a list of quizzes as an attribute.
    def __init__(self, client):
        self.client = client
        self.quizzes = {}

    # create_quiz command which will create a quiz with a specified name.
    @commands.command()
    async def create_quiz(self, ctx, *, name):
        self.quizzes[name] = Quiz()
        await ctx.send(f'The following quiz was created: {name}')

    # add_question command which will allow the user to add different types of questions to the quiz.
    @commands.command()
    async def add_question(self, ctx, *, params):
        paramList = parse_inputs(params)
        quiz = paramList[0]
        qType = paramList[1]
        question = paramList[2]
        answer = paramList[3]
        
        # If the question type is just a standard question, create an instance of the Question class and add it to the quiz.
        if qType == "q":
            self.quizzes[quiz].addQuestion(question, answer)
            await ctx.send(f'Added question {question} to {quiz}')
        
        # If the question type is just multiple choice, create an instance of the MultipleChoice class and add it to the quiz.
        elif qType == "mc":
            responses = paramList[4:]
            self.quizzes[quiz].addMultipleChoice(question, int(answer), responses)
            await ctx.send(f'Added multiple choice {question} to {quiz}')

        # If the question type is just a LaTeX question, create an instance of the Latex class and add it to the quiz.
        elif qType == "latex":
            self.quizzes[quiz].addLatex(question, get_latex(answer))
            await ctx.send(f'Added LaTeX question {question} to {quiz}')
            preview(get_latex(answer), viewer = 'file', filename = 'image.png')

    # show_response command which will display the correct answer when called.
    @commands.command()
    async def show_response(self, ctx, *, params):
        paramsList = parse_inputs(params)
        quiz = paramsList[0]
        question = paramsList[1]

        embed = discord.Embed(
            title = quiz,
            inline = False
        )

        embed.add_field(
            name = f'Question {question}',
            value = f'{self.quizzes[quiz].showQuestion(int(question))}',
            inline = False
        )

        embed.add_field(
            name = 'Answer',
            value = f'The answer is: {self.quizzes[quiz].revealAnswer(int(question))}',
            inline = False
        )
        await ctx.send(embed = embed)

    # start_quiz command to begin execution of the quiz.
    @commands.command()
    async def start_quiz(self, ctx, *, name):
        self.currentQuiz = self.quizzes[name]
        self.currentName = name
        self.currentQuestion = -1
        self.quizChannel = await ctx.guild.create_text_channel(name, category = ctx.guild.categories[-1])

    # next_question command will call the next question and display it.
    @commands.command()
    async def next_question(self, ctx):
        if self.currentQuestion < len(self.currentQuiz.questions) - 1:
            self.answered = []
            self.currentQuestion+=1

            embed = discord.Embed(
                title = self.currentName,
                inline = False
            )

            embed.add_field(
                name = f'Question {self.currentQuestion + 1}',
                value = f'{self.currentQuiz.questions[self.currentQuestion]}',
                inline = False
            )

            await self.quizChannel.send(embed = embed)

        else:
            embed = discord.Embed(
                title = self.currentName,
                inline = False
            )

            embed.add_field(
                name = 'End of quiz.',
                value = 'Goob job!',
                inline = False
            )

            await self.quizChannel.send(embed = embed)

    # response_next command will reveal the answer for the current question and go to the next question.
    @commands.command()
    async def response_next(self, ctx):
        embed = discord.Embed(
            title = self.currentName,
            inline = False
        )

        embed.add_field(
            name = f'Question {self.currentQuestion + 1}',
            value = f'The answer is: {self.currentQuiz.revealAnswer(self.currentQuestion + 1)}',
            inline = False
        )

        await self.quizChannel.send(embed = embed)

        if self.currentQuestion < len(self.currentQuiz.questions) - 1:
            self.answered = []
            self.currentQuestion+=1

            embed = discord.Embed(
                title = self.currentName,
                inline = False
            )

            embed.add_field(
                name = f'Question {self.currentQuestion + 1}',
                value = f'{self.currentQuiz.questions[self.currentQuestion]}',
                inline = False
            )

            await self.quizChannel.send(embed = embed)

        else:
            embed = discord.Embed(
                title = self.currentName,
                inline = False
            )

            embed.add_field(
                name = 'End of quiz.',
                value = 'Goob job!',
                inline = False
            )

            await self.quizChannel.send(embed = embed)

    # answer command which allows students to answer the question, and tell them if they got their question correct or incorrect.
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