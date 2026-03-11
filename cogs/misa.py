import discord
from discord.ext import commands
import random

class Misa(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        
    frases = {
        "feliz": [
        "Misa online. Demorei, mas apareci. Qual a boa de hoje? ✨",
        "Heeey! A Misa deu as caras! Podem parar de sentir saudades que a alegria do servidor chegou. 🎀 Qual a fofoca de hoje?",
        "Misa online! Quem precisa de ajuda ou só quer conversar? 💕",
        "Chegueeei! Misa online e pronta para o caos (ou pra paz, vocês que mandam). ✨ O que eu perdi enquanto tava fora?",
        "Apareci! Aproveitem minha presença, que hoje eu tô inspirada! (◕‿◕)",
        "Se alguém estiver precisando de um sinal, um conselho ou só de um meme ruim, eu cheguei! 💕",
    ],

    "animada": [
        "Misa na área! Podem parar o que estão fazendo para me dar atenção agora.",
        "CHEGUEI! Pode parando tudo e me contando as novidades! 🎀",
        "Misa online! O servidor finalmente ficou completo.",
        "Misa na área! Se esse servidor não animar agora, eu vou começar a marcar o @everyone só pra ver o caos!",
        "MISA ONLINE! Tomei três cafés digitais e agora ninguém me segura! Bora agitar isso aqui antes que eu comece a mandar trava-zap de emoji!",
    ],

    "cansada": [
        "Misa na área... mas se alguém me pedir algo complexo, eu vou fingir que meu Wi-Fi caiu.",
        "Oi... Misa presente, mas operando via satélite e com sinal ruim. Se eu sumir, é porque minha bateria social (e digital) entrou em colapso.",
        "Oi... a Misa tá aqui... mas se eu fosse vocês, não esperaria muita agilidade hoje. Alguém injeta um código de cafeína em mim, por favor?",
        "Presente! Mas hoje estou funcionando na base do ódio e da economia de energia. Me chamem só se for algo muito urgente ou uma fofoca muito boa.",
        "Tô aqui... devagar... mas funcionando!",
    ],

    "estressada": [
        "Ok... Misa chegou. O que aconteceu agora? 😤",
        "Oi. Espero que não seja mais confusão no servidor... 💢",
        "Presente... tentando manter a calma hoje... 😠",
        "Misa online. Vamos resolver isso rápido, ok? 🔥",
        "Oi... respira... fala o que aconteceu. 😒",
    ],

    "curiosa": [
        "Hmm... isso parece interessante... 👀",
        "Oooh? Conta mais, fiquei curiosa agora... 🔍",
        "Misa observando tudo aqui no servidor... 💭",
        "Curioso... muito curioso mesmo... 🤔",
        "Algo me diz que essa história vai ser boa... 🐾",
        ]
    }

    humor_atual = "feliz"
    
    @commands.command()
    async def misa(self, ctx:commands.Context):
        frase = random.choice(self.frases[self.humor_atual])
        await ctx.reply(frase)
        
        
    @commands.command()
    @commands.has_role("Misa Owner")
    async def humor(self, ctx:commands.Context, estado:str):
        estados = ["feliz", "animada", "cansada", "estressada", "curiosa"]
        if estado not in estados:
            await ctx.reply(f"Estado inválido! Use: {', '.join(estados)}")
            return
        self.humor_atual = estado
        await ctx.reply(f"Humor alterado para **{estado}**!") 
        
async def setup(bot):
    await bot.add_cog(Misa(bot))