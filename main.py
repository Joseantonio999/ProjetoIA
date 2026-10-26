import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    print("O bot foi inicializado com sucesso")

@bot.command()
async def somar(ctx:commands.Context, numero1:float, numero2:float):
    resultado = numero1 + numero2
    await ctx.send(f"A soma entre {numero1} e {numero2} é igula a {resultado}")
    
    

bot.run("MTU2MTgyMjA4NDYzODcwNzgwOA.GQRDVj.-iZqvYYKvmsGhQ0LfmkR32TnOogDEHE0WkkkFs")