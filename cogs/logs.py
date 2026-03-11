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
        canal = self.bot.get_channel(CANAL_LOGS_ID)
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
        
        embed = discord.Embed(
            title="✏️ Mensagem editada",
            color=discord.Color.yellow()
        )
        embed.add_field(name="👤 Autor", value=antes.author.mention, inline=True)
        embed.add_field(name="💬 Canal", value=antes.channel.mention, inline=True)
        embed.add_field(name="📝 Antes", value=antes.content or "Sem conteúdo", inline=False)
        embed.add_field(name="✅ Depois", value=depois.content or "Sem conteúdo", inline=False)
        await canal.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_member_remove(self, membro:discord.Member):
        canal = self.bot.get_channel(CANAL_LOGS_ID)
        if canal is None:
            return
        embed = discord.Embed(
             title="👋 Membro saiu",
            color=discord.Color.red()
        )
        embed.add_field(name="👤 Membro", value=membro.mention, inline=True)
        embed.add_field(name="🪪 ID", value=membro.id, inline=True)
        embed.set_thumbnail(url=membro.display_avatar.url)
        await canal.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_member_update(self, antes:discord.Member, depois:discord.Member):
        if antes.roles == depois.roles:
            return
        canal = self.bot.get_channel(CANAL_LOGS_ID)
        if canal is None:
            return
        cargos_adicionados = [r for r in depois.roles if r not in antes.roles]  
        cargos_removidos = [r for r in antes.roles if r not in depois.roles]
        
        if cargos_adicionados:
            embed = discord.Embed(title="📥 Cargo adicionado", color=discord.Color.green())
            embed.add_field(name="👤 Membro", value=depois.mention, inline=True)
            embed.add_field(name="🎭 Cargo", value=cargos_adicionados[0].mention, inline=True)
            await canal.send(embed=embed)
        if cargos_removidos:
            embed = discord.Embed(title="📤 Cargo removido", color=discord.Color.red())
            embed.add_field(name="👤 Membro", value=depois.mention, inline=True)
            embed.add_field(name="🎭 Cargo", value=cargos_removidos[0].mention, inline=True)
            await canal.send(embed=embed)
     
async def setup(bot):
    await bot.add_cog(Logs(bot))            
            
                