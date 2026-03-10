import discord
from discord.ext import commands

CANAL_LOGS_ID = 1481056185523114246

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__
        
    @commands.Cog.listener()
    async def on_message_delete(self, mensagem:discord.Message):
        if mensagem.author.bot:
            return
        canal = self.bot.get_channel(self.CANAL_LOGS_ID)
        if canal is None:
            return
        
        embed = discord.Embed(
            title="🗑️ Mensagem deletada",
            color=discord.Color.red()
        )
        embed.add_field(name="👤 Autor", value=mensagem.author.mention, inline=True)
        embed.add_field(name="💬 Canal", value=mensagem.channel.mention, inline=True)
        embed.add_field(name="📝 Conteúdo", value=mensagem.content or "Sem conteúdo", inline=False)
        await canal.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_message_edit(self, antes:discord.Message, depois:discord.Message):
        if antes.author.bot:
            return
        if antes.content == depois.content:
            return
        canal = self.bot.get_channel(CANAL_LOGS_ID)
        if canal is None:
            return            