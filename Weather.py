api_key = "KEY"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

@client.command()
async def wetter(ctx, *, city: str):
  city_name = city
  complete_url = base_url + "appid=" + api_key + "&q=" + city_name
  response = requests.get(complete_url)
  x = response.json()
  channel = ctx.message.channel
  if x["cod"] != "404":
        async with channel.typing():
          y = x["main"]
          current_temperature = y["temp"]
          current_temperature_celsiuis = str(round(current_temperature - 273.15))
          current_pressure = y["pressure"]
          current_humidity = y["humidity"]
          z = x["weather"]
          weather_description = z[0]["description"]
          weather_description = z[0]["description"]
          embed = discord.Embed(title=f"Wetter in {city_name}",
                              color=0x22a7f0)
          embed.add_field(name="`Beschreibung:`", value=f"**{weather_description}**", inline=False)
          embed.add_field(name="`Temperatur:`", value=f"**{current_temperature_celsiuis}°C**", inline=False)
          embed.add_field(name="`Luftfeuchtigkeit:`", value=f"**{current_humidity}%**", inline=False)
          embed.add_field(name="`Luftdruck:`", value=f"**{current_pressure}hPa**", inline=False)
          embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
          embed.set_footer(text='Developed by IconNT06', icon_url='https://media.discordapp.net/attachments/783038584176640020/964994528413114429/standard_8_1.png')
          await channel.send(embed=embed)
  else:
    await channel.send("Stadt nicht gefunden!")