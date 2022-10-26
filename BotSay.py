@client.command()
@commands.is_owner()
async def say(ctx, *, message):
  await asyncio.sleep(1)
  await ctx.message.delete()
  await asyncio.sleep(1)
  await ctx.send(message)