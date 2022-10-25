@client.command()
async def nummer(ctx, *, number=0):
  number_list = [1, 2, 3, 4, 5]
  correct_number = random.choice(number_list)

  if number == correct_number:
    embed = discord.Embed(title=f'Deine Nummer: {number}', color=	0x2ecc71)
    embed.add_field(name='Dies war die richtige Nummer!', value="Danke fürs Spielen!")
    embed.set_footer(text='Developed by IconNT06', icon_url='https://media.discordapp.net/attachments/783038584176640020/964994528413114429/standard_8_1.png')
    await ctx.send(embed=embed)
  
  else:
    embed = discord.Embed(title=f'Deine Nummer: {number}', color=0xFF0000)
    embed.add_field(name="Dies war die falsche Nummer", value="Danke fürs Spielen!")
    embed.set_footer(text='Developed by IconNT06', icon_url='https://media.discordapp.net/attachments/783038584176640020/964994528413114429/standard_8_1.png')
    await ctx.send(embed=embed)