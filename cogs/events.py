import discord
from discord import app_commands
from discord.ext import commands, tasks

class eventos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        
    async def criar_embed(self, membro:discord.Member):         #cria embed do on_member_join
        minha_embed = discord.Embed(color=discord.Color.blurple())
        minha_embed.title = (f"🎀 {membro.display_name} chegou!")
        minha_embed.description = (
    f"Oiie {membro.mention} — Seja bem-vindo(a) ao **Misa Community**!\n\n"
    "Espero que esteja tudo bem por aí! Eu sou Misa, a inteligência que ajuda a cuidar deste cantinho. ݁ ≽(◉˕ ◉ ≼マ\n\n"
    "Como ainda estou sendo desenvolvida, meus moderadores estão sempre me dando upgrades.\n\n"
    "Por favor, não esqueça de ler as regras para que possamos manter uma comunidade divertida e respeitosa. Aproveite para selecionar o seu cargo e fique à vontade por aqui! ݁ ˎˊ˗\n\n"
    "Esperamos que esse cantinho seja acolhedor para você, nossos moderadores estão abertos para reportes e sugestões. ♡"
    )
    
        
        imagem = discord.File("hello.gif", "hello.gif")
        minha_embed.set_image(url="attachment://hello.gif")
        minha_embed.set_thumbnail(url=membro.display_avatar.url)
        
        return minha_embed, imagem   
        
    @commands.Cog.listener()
    async def on_member_join(self, membro:discord.Member):            
        canal = self.bot.get_channel(1473800246508126339)
        if canal is None:
            return print("Não consegui encontrar o canal :( ")
        embed, imagem = await self.criar_embed(membro)
        await canal.send(embed=embed, file=imagem) 

async def setup(bot):
    await bot.add_cog(eventos(bot))
        