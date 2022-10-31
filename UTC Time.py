@client.command()
async def utcuhrzeit(ctx):
  timestamp = datetime.now()
  utc = pytz.timezone('UTC')
  msg = f"UTC Zeit: `{timestamp.astimezone(utc).strftime('%H:%M:%S')}` Uhr! 🕒"
  await ctx.channel.send(msg)