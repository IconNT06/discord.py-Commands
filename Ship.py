@client.command()
async def ship(ctx, user_1 : discord.Member, user_2 : discord.Member):
    responses = [' passen zu 1% zusammen!',
             ' passen zu 5% zusammen!',
             ' passen zu 10% zusammen!',
             ' passen zu 15% zusammen!',
             ' passen zu 20% zusammen!',
             ' passen zu 25% zusammen!',
             ' passen zu 30% zusammen!',
             ' passen zu 35% zusammen!',
             ' passen zu 40% zusammen!',
             ' passen zu 45% zusammen!',
             ' passen zu 50% zusammen!',
             ' passen zu 55% zusammen!',
             ' passen zu 60% zusammen!',
             ' passen zu 65% zusammen!',
             ' passen zu 70% zusammen!',
             ' passen zu 75% zusammen!',
             ' passen zu 80% zusammen!',
             ' passen zu 85% zusammen!',
             ' passen zu 90% zusammen!',
             ' passen zu 95% zusammen!',
             ' passen zu 100% zusammen!']
    response = random.choice(responses)
    embed=discord.Embed(title="Hier ist euer Ergebnis!", color=0x22a7f0)
    embed.add_field(name='`Antwort:`', value=f"{user_1.mention} und {user_2.mention}{response}", inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/783038584176640020/1001564396121767966/hand-drawn-heart-11549459255jz1gvm6cwh-removebg-preview.png')
    await ctx.send(embed=embed)