determine_flip = [1, 0]

@client.command()
async def coinflip(ctx):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(title="Coinflip:", color=0x22a7f0, description=f"{ctx.author.mention} hat eine Münze geworfen und bekam `Kopf`!")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Coinflip:", color=0x22a7f0, description=f"{ctx.author.mention} hat eine Münze geworfen und bekam `Zahl`!")
        await ctx.send(embed=embed)