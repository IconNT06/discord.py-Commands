@client.command(aliases= ['Kugel'])
async def kugel(ctx, question):
    responses = ['So wie ich das sehe ja',
             'Ja',
             'Positiv',
             'Von meinem Blickpunkt aus, ja',
             'Wahrscheinlich',
             'Die Chancen stehen gut',
             'Nein',
             'Negativ',
             'Vielleicht',
             'Ich bin mir nicht sicher',
             'Vielleicht',
             'Kann ich noch nicht sagen',
             'Ich bin zu müde zum antworten',
             'Leck mich',
             '*Plopp*',
             'He he he ha',
             'Ein weiser Stein sagte einst, nein',
             'Lass mich schlafen. *schläft weiter*']
    response = random.choice(responses)
    embed=discord.Embed(title="Die magische Kugel hat gesprochen!", color=0x22a7f0)
    embed.add_field(name='`Antwort:`', value=f'{response}', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/783038584176640020/971442788195516416/kisspng-computer-icons-magic-crystal-ball-emoji-5b37fc1e0bb1b7.1756704115303956780479-removebg-preview.png')
    embed.set_footer(text='Developed by IconNT06', icon_url='https://media.discordapp.net/attachments/783038584176640020/964994528413114429/standard_8_1.png')
    await ctx.send(embed=embed)