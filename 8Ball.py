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
    await ctx.send(embed=embed)
