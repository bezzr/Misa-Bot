import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @commands.command()
    async def ping(self, ctx:commands.Context):
        latencia = round(self.bot.latency * 1000) # latency em segundos * 1000 = milissegundos
        await ctx.reply(f"🏓 Pong! **{latencia}ms**")
        
    @commands.command()
    async def avatar(self, ctx:commands.Context, membro:discord.Member=None):
        print(f"argumento recebido: {membro}")
        print(f"membros no cache: {len(ctx.guild.members)}")
        
        if membro is None:
            membro = ctx.author
            
        embed = discord.Embed(title=f"Avatar de {membro.display_name}")
        embed.set_image(url=membro.display_avatar.url)
        await ctx.reply(embed=embed)
            
    @commands.command()
    async def userinfo(self, ctx:commands.Context,membro:discord.Member=None):
        if membro is None:
            membro = ctx.author
        embed = discord.Embed(title=f"Informações de {membro.display_name}", color=discord.Color.blurple())
        embed.set_thumbnail(url=membro.display_avatar.url)
        embed.add_field(name="👤 Nome", value=membro.name, inline=True)
        embed.add_field(name="🪪 ID", value=membro.id, inline=True)
        embed.add_field(name="📅 Conta criada em", value=membro.created_at.strftime("%d/%m/%Y"), inline=True)
        embed.add_field(name="📥 Entrou no servidor em", value=membro.joined_at.strftime("%d/%m/%Y"), inline=True)
        embed.add_field(name="🎭 Cargo mais alto", value=membro.top_role.mention, inline=True)
        await ctx.reply(embed=embed)
    
    @commands.command()
    async def misainfo(self, ctx:commands.Context):
        embed = discord.Embed(
            title="🎀 Misa Bot",
            description= "Oiie! Eu sou a Misa, a inteligência do Misa Community!",
            color=discord.Color.blurple()
        )
        embed.add_field(name="<:okay_frieren:1479662866364760064> Desenvolvedores", value="Guuh & Clara", inline=True)
        embed.add_field(name="🏓 Latência", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        embed.add_field(name="📡 Servidores", value=len(self.bot.guilds), inline=True)
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        await ctx.reply(embed=embed)
        
        
async def setup(bot):
    await bot.add_cog(Info(bot))           