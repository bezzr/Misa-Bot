import discord
from discord.ext import commands
import random

class Misa(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        
    frases = {
        "feliz": [
        "Oiiee! A Misa chegou! O que tá rolando no servidor? 🎀",
        "Presente! E hoje eu tô cheia de energia boa! ✨",
        "Misa online! Quem precisa de ajuda ou só quer conversar? 💕",
        "Oii oii! Cheguei pra deixar o chat um pouco mais animado! 🌸",
        "Misa apareceu! Hoje tô de bom humor, aproveitem! (◕‿◕)",
    ],

    "animada": [
        "MISA ONLINE! O QUE TÁ ACONTECENDO AQUI?! 🔥",
        "Boraaa! Tô no modo energia máxima hoje! ⚡",
        "EI EI! Alguém me chamou ou eu só cheguei causando mesmo? 💪",
        "CHEGUEI! O servidor parece mais divertido agora! 🎉",
        "Modo hiper ativado! Se preparem porque hoje eu tô impossível! 🚀",
    ],

    "cansada": [
        "Oi... a Misa tá aqui... só um pouquinho cansada hoje... ☕",
        "Presente... funcionando em modo economia de energia... 💤",
        "Cheguei... mas meu travesseiro ainda tá me chamando... 😮‍💨",
        "Hoje a Misa tá operando em 50% da capacidade... 🔋",
        "Tô aqui... devagar... mas funcionando! 🐌",
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