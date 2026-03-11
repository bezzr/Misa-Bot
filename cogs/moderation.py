import discord
from discord.ext import commands


class Moderacao(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        
    @commands.command()
    @commands.has_role("Misa Owner")
    async def clear(self, ctx:commands.Context, quantidade:int=10):
        await ctx.channel.purge(limit=quantidade + 1)
        await ctx.send(f"🗑️ {quantidade} mensagens apagadas!", delete_after=3)
        
    @commands.command()
    @commands.has_role("Misa Owner")
    async def slow(self, ctx:commands.Context, segundos:int=0):
        await ctx.channel.edit(slowmode_delay=segundos)
        if segundos == 0:
            await ctx.reply("Slowmode desativado!")
        else:
            await ctx.reply(f"Slowmode definido para **{segundos}**!")
            
    @commands.command()
    @commands.has_role("Misa Owner")
    async def lock(self, ctx:commands.Context):  
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.reply("Canal Travado!")
        
    @commands.command()
    @commands.has_role("Misa Owner")
    async def unlock(self, ctx:commands.Context):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.reply("Canal Destravado!")
        
async def setup(bot):
    await bot.add_cog(Moderacao(bot))  