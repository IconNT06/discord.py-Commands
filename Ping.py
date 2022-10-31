@client.command()
async def ping(ctx):
    await ctx.send(f'Mein Ping liegt bei: `{round(client.latency * 1000)}`ms! :globe_with_meridians:')