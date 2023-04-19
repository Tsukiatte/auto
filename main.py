import datetime
import disnake
from disnake.ext import commands, tasks

import time
import json
import random
import asyncio

from pycoingecko import CoinGeckoAPI

client = commands.Bot(command_prefix='!', intents=disnake.Intents.all())

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	#scanner.start()

@client.slash_command(description="cryptoticket msg")
async def cryptoticketmsg(inter):
	await inter.response.defer()

	channel = inter.channel
	embed = disnake.Embed(
		title="**Auto - Cryptocurrency Services**",
		description="""
The following rules must be followed - failure to abide may result in an instant ban. Staff will have independant thresholds to what is deemed completely innapropriate.
**Supported Currencies** 💱
Bitcoin, Ethereum & Litecoin

**Service Fees** 💳
**$4.00 USD** or **0.5%** of deal

**How does it work?** ❔
Simply press the **'Crypto Middleman'** button below to create a ticket. We will ask you a series of questions in order for us to understand the deal.

> - What Cryptocurrency? (BTC/ETH/LTC)
> - Who are you dealing with? (tag/dev id)
> - What is the type of deal? (Limiteds/Exchange etc)
> - How much USD should the bot receive?

Once we understand what the deal is regarding, we will create a payment invoice for the sender, once the payment has securely been received we will tell both users to exchange assets, or whatever the deal is regarding. Once the product has been delivered the funds can be released for the other dealer to claim.

**Is this system safe?** 🛡️
This system is **100% secure**, we ensure every ticket has its own unique wallet to avoid any confliction. All wallet private keys are encrypted and securely stored, they are backed up and can be accessed if needed.
  	""",
		color=0xe4741f
	)
	embed.set_image(url="https://images-ext-2.discordapp.net/external/1PoFcspw4sdIcRIfFlQ9_Kr7Y1MpPjt3HGB5h3B1sn4/https/s4.gifyu.com/images/standard28b6475d089fd2934.gif")

	embedtwo = disnake.Embed(
		description="""
Status: **ONLINE**
Events: [**Under $300 deals free!**](https://discord.com/channels/1082259227575320606/1082259258650931271)
  """,
		color=0x26c350
	)

	await channel.send(embed=embed)
	await channel.send(embed=embedtwo)
	msg = await inter.edit_original_response("Done!")

	await asyncio.sleep(2)

	await msg.delete()

@client.slash_command(description="cryptoticket msg")
async def limitedsmsg(inter):
	await inter.response.defer()

	channel = inter.channel
	embed = disnake.Embed(
		title="**Auto - Limiteds Middleman Service**",
		description="""
**Fees** 💳
$4 - Buy MM Passes for discounted rates in <#1082259298224197665>

**Fee Payment ** 💱
Bitcoin / Ethereum / Litecoin / Cash App

**How does it work?** ❔
Simply press the 'Limiteds Middleman' button below to create a ticket. The points below explain the simple process we've designed.

> - Tell the bot who you're dealing with
> - Specify whether you are buying or selling the item
> - Cover the service fee
> - Seller sends the trade to our ROBLOX Middleman account
> - Both dealers confirm items involved in trade
> - Buyer pays for item
> - Seller releases item
> - Buyer gives username
> - Buyer claims item

**Is this system safe?** 🛡️
This system has been designed and extensively tested over months of development. We have processed over 15,000 individual deals using this system.""",
		color=0xe4741f
	)
	embed.set_image(url="https://images-ext-2.discordapp.net/external/CIbptxRuHxJHFvk4gFI7DFAE8N-PwzJlWl1j_7FC8oo/https/s1.gifyu.com/images/standard3.gif")

	embedtwo = disnake.Embed(
		description="""
Status: **ONLINE**
Events: [**Under 150k Deals FREE!**](https://discord.com/channels/1082259227575320606/1082259258650931271)
  """,
		color=0x26c350
	)

	await channel.send(embed=embed)
	await channel.send(embed=embedtwo)
	msg = await inter.edit_original_response("Done!")

	await asyncio.sleep(2)

	await msg.delete()

@client.event
async def on_guild_channel_create(channel):
	await asyncio.sleep(1)

	class ChooseType(disnake.ui.View):
		def __init__(self):
			super().__init__(timeout=None)

		@disnake.ui.string_select(
			placeholder="Make a selection",
			options=[
				disnake.SelectOption(label="Bitcoin",description="BTC",value="Bitcoin",emoji="<:btc:1082259937511616623>"),
				disnake.SelectOption(label="Litecoin",description="LTC",value="Litecoin",emoji="<:ltc:1082259913033662514>"),
				disnake.SelectOption(label="Ethereum",description="ETH",value="Ethereum",emoji="<:eth:1082259949192753193>"),
				disnake.SelectOption(label="USDT",description="ERC-20",value="USDT",emoji="<:usdt:1082259961138122782>")
			],
			max_values=1
		)
		async def button1(self, interaction: disnake.Interaction, selected: disnake.ui.Select):
			product = interaction.values[0]

			if True:
				if True:
					if True:

						embed = disnake.Embed(
							title="**Bitcoin Middleman System 1.0.0**",
							description="Welcome to our Bitcoin Escrow System - here we will process any deal involving Bitcoin",
							color=0xf7931a
						)
						embed.add_field(
							name="**How does it work?**",
							value="""
					Whoever is sending the Bitcoin will send it to one of our secure wallets. Once the required amount of confirmations have been reached, we will ask the other user to provide the
					item/asset/service to the user who sent the Cryptocurrency to us.""",
							inline=False
						)
						embed.add_field(
							name="**How many confirmations are required?**",
							value="""
					For Bitcoin transactions we require 1 Network Confirmations, this is to ensure that nothing can go wrong with the payment.""",
							inline=False
						)
						embed.add_field(
							name="**What do I do if something goes wrong?**",
							value="""
					If you are ever confused or unsure, you may ping a member of <@&1082259646473048124> for assistance - we are always happy to assist!""",
							inline=False
						)
						embed.set_thumbnail("https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/640px-Bitcoin.svg.png")

						embedtwo = disnake.Embed(
							title="Who are you dealing with?",
							description="""
					eg. username#1234
					eg. 123456789012345678
					  """,
							color=0xf7931a
						)

						await channel.send(embed=embed)
						await channel.send(embed=embedtwo)

						userone = ""
						usertwo = ""

						def check(m):
							return m.channel == channel and m.author.id != 1095145973090635876

						async def erroronemsg(cnl):
							await cnl.send("**Invalid username**. *Please try again*.")

						await asyncio.sleep(0.5)

						with open(f"roles/{channel.name}.json", "r") as file:
							data = json.load(file)
							data['crypto'] = product

							message = await channel.fetch_message(data['msg'])
							await message.delete()

							with open(f"roles/{channel.name}.json", "w") as update:
								json.dump(data, update, indent=4)

						while usertwo == "":
							msg = await client.wait_for("message", check=check)

							if "#" in msg.content:
								if msg.content.count("#") != 1:
									await erroronemsg(channel)
									await asyncio.sleep(1)
								else:
									username = msg.content.split("#")[0]
									discrim = msg.content.split("#")[1]
									memberslist = client.get_guild(1082259227575320606).members
									for member in memberslist:
										if usertwo != "":
											break
										else:
											memberdiscrim = member.discriminator
											if memberdiscrim == discrim:
												membername = member.name
												if membername == username:
													if member.id != msg.author.id:
														userone = msg.author
														usertwo = member

									if usertwo == "":
										await erroronemsg(channel)
										await asyncio.sleep(1)

							else:
								try:
									member = client.get_guild(1082259227575320606).get_member(int(msg.content))

									if member.id != msg.author.id:
										userone = msg.author
										usertwo = member
								except:
									await erroronemsg(channel)
									await asyncio.sleep(0.5)

						class Roles(disnake.ui.View):
							def __init__(self):
								super().__init__(timeout=None)

							sender = ""
							receiver = ""

							@disnake.ui.button(style=disnake.ButtonStyle.gray, label="I am Sender")
							async def button1(self, button, interaction):
								await interaction.response.defer()

								with open(f"roles/{channel.name}.json", "r") as file:
									data = json.load(file)
									sender = data['sender']
									receiver = data['receiver']

									if receiver == interaction.author.id:
										data['receiver'] = ""
										receiver = ""

									if sender == interaction.author.id:
										data['sender'] = ""
										with open(f"roles/{channel.name}.json", "w") as update:
											json.dump(data, update, indent=4)

										messageid = data['msg']

										if type(receiver) == str:
											receiver = "`None`"

										else:
											receiver = "<@" + str(receiver) + ">"

										embed = disnake.Embed(
											title="User Identification",
											description="**Sender** - Providing bitcoin to bot\n**Receiver** - Recieving bitcoin after deal is completed",
											color=0xf7931a
										)
										embed.add_field(
											name="**Sender**",
											value="`None`",
											inline=True
										)
										embed.add_field(
											name="**Receiver**",
											value=f"{receiver}",
											inline=True
										)

										message = await channel.fetch_message(messageid)
										await message.edit(embed=embed)

									else:
										data['sender'] = interaction.author.id
										sender = interaction.author.id
										with open(f"roles/{channel.name}.json", "w") as update:
											json.dump(data, update, indent=4)

										messageid = data['msg']

										if type(receiver) == str:
											receiver = "`None`"

										else:
											receiver = "<@" + str(receiver) + ">"

										embed = disnake.Embed(
											title="User Identification",
											description="**Sender** - Providing bitcoin to bot\n**Receiver** - Recieving bitcoin after deal is completed",
											color=0xf7931a
										)
										embed.add_field(
											name="**Sender**",
											value=f"<@{data['sender']}>",
											inline=True
										)
										embed.add_field(
											name="**Receiver**",
											value=f"{receiver}",
											inline=True
										)

										message = await channel.fetch_message(messageid)
										await message.edit(embed=embed)

										if sender != "" and receiver != "`None`":
											await message.delete()

											class Confirm(disnake.ui.View):
												def __init__(self):
													super().__init__(timeout=None)

												sender = ""
												receiver = ""

												@disnake.ui.button(style=disnake.ButtonStyle.green, label="Correct")
												async def button1(self, button, interaction):
													with open(f"roles/{channel.name}.json", "r") as file:
														data = json.load(file)

														if data['confs'] == 0:
															data['confs'] += 1
															data['confirmed'] = interaction.author.id

															with open(f"roles/{channel.name}.json", "w") as update:

																embed = disnake.Embed(
																	description=f"{interaction.author.mention} has responded to 'Correct'",
																	color=0x2bb530
																)
																message = await interaction.send(embed=embed)
																yayeffy = await interaction.original_response()
																data['msgone'] = yayeffy.id

																json.dump(data, update, indent=4)

														else:
															if True:
																if interaction.author.id != data['confirmed']:
																	data['confs'] += 1
																	data['confirmed'] = interaction.author.id

																	message = await channel.fetch_message(data['msg'])

																	await asyncio.sleep(0.5)

																	await message.delete()

																	class ChooseType(disnake.ui.View):
																		def __init__(self):
																			super().__init__(timeout=None)
																		@disnake.ui.string_select(
																			placeholder="Make a selection",
																			options=[
																				disnake.SelectOption(label="ROBLOX Limiteds",value="ROBLOX Limiteds"),
																				disnake.SelectOption(label="ROBLOX Ingame Items",value="ROBLOX Ingame Items"),
																				disnake.SelectOption(label="CSGO Knives",value="CSGO Knives"),
																				disnake.SelectOption(label="Currency Exchange",value="Currency Exchange"),
																				disnake.SelectOption(label="Other",description="Ensure product delivery is 'provable'",value="Other")
																			],
																			max_values=1
																		)
																		async def button1(self, interaction: disnake.Interaction, selected: disnake.ui.Select):
																			product = interaction.values[0]

																			with open(f"roles/{channel.name}.json", "r") as file:
																				data = json.load(file)
																				data['type'] = product
																				data['confs'] = 0
																				data['confirmed'] = ""
																				with open(f"roles/{channel.name}.json", "w") as update:
																					json.dump(data, update, indent=4)

																			class ConfirmTwo(disnake.ui.View):
																				def __init__(self):
																					super().__init__(timeout=None)

																				@disnake.ui.button(style=disnake.ButtonStyle.green, label="Correct")
																				async def button1(self, button, interaction):
																					with open(f"roles/{channel.name}.json", "r") as file:
																						data = json.load(file)

																						if data['confs'] == 0:
																							data['confs'] += 1
																							data['confirmed'] = interaction.author.id

																							with open(f"roles/{channel.name}.json", "w") as update:

																								embed = disnake.Embed(
																									description=f"{interaction.author.mention} has responded to 'Correct'",
																									color=0x2bb530
																								)
																								message = await interaction.send(embed=embed)
																								yayeffy = await interaction.original_response()
																								data['msgtwo'] = yayeffy.id

																								json.dump(data, update, indent=4)
																						else:
																							if True:
																								if interaction.author.id != data['confirmed']:
																									data['confs'] = 0
																									data['confirmed'] = ""

																									with open(f"roles/{channel.name}.json", "w") as update:
																										json.dump(data, update, indent=4)

																									message = await channel.fetch_message(data['msg'])
																									messageone = await channel.fetch_message(data['msgone'])
																									messagetwo = await channel.fetch_message(data['msgtwo'])

																									await asyncio.sleep(0.5)

																									await message.delete()
																									await messageone.delete()
																									await messagetwo.delete()

																									embed = disnake.Embed(
																										description=f"This deal has been categorized as a **{product}**",
																										color=0x2bb530
																									)

																									await channel.send(embed=embed)

																									recievemoney = 0

																									embed = disnake.Embed(
																										title="**How much should we expect to receive in USD?**",
																										description="eg. $100",
																										color=0xf7931a
																									)

																									msg = await channel.send(embed=embed)

																									data['msg'] = msg.id
																									with open(f"roles/{channel.name}.json", "w") as update:
																										json.dump(data, update, indent=4)

																									while recievemoney == 0:
																										data = ''
																										with open(f"roles/{channel.name}.json", "r") as file:
																											data = json.load(file)

																										try:
																											if data['done'] != "t":
																												pass
																										except:
																											if True:
																												msg = await client.wait_for("message", check=check)

																												try:
																													data['value'] = int(msg.content)
																													with open(f"roles/{channel.name}.json", "w") as update:
																														json.dump(data, update, indent=4)
																												except:
																													await channel.send(f"`{msg.content}` is *not* a **valid integer**!")
																												else:
																													try:
																														message = await channel.fetch_message(data['msg'])

																														await asyncio.sleep(0.2)
																														await message.delete()
																													except:
																														pass

																													embed = disnake.Embed(
																														description=f"Should we expect to recieve **${int(msg.content)}.00** worth of {data['crypto']}?",
																														color=0xf7931a
																													)

																													class ConfirmThree(disnake.ui.View):
																														def __init__(self):
																															super().__init__(timeout=None)

																														@disnake.ui.button(style=disnake.ButtonStyle.green, label="Yes")
																														async def button1(self, button, interaction):
																															with open(f"roles/{channel.name}.json", "r") as file:
																																data = json.load(file)

																																if data['confs'] == 0:
																																	data['confs'] += 1
																																	data['confirmed'] = interaction.author.id

																																	with open(f"roles/{channel.name}.json", "w") as update:
																																		json.dump(data, update, indent=4)

																																		embed = disnake.Embed(
																																			description=f"{interaction.author.mention} has responded to 'Yes'",
																																			color=0x2bb530
																																		)

																																		message = await interaction.send(embed=embed)
																																		yayeffy = await interaction.original_response()
																																		data['msgtwo'] = yayeffy.id
																																else:
																																	if True:
																																		if interaction.author.id != data['confirmed']:
																																			data['confs'] += 1
																																			data['confirmed'] = interaction.author.id
																																			data['done'] = "t"

																																			try:
																																				message = await channel.fetch_message(data['msg'])
																																				await asyncio.sleep(0.5)
																																				await message.delete()
																																			except:
																																				pass
																																			try:
																																				messagetwo = await channel.fetch_message(data['msgtwo'])
																																				await messagetwo.delete()
																																			except:
																																				pass

																																			crypto_currency = data['crypto'].lower().replace("usdt", "usd")
																																			destination_currency = 'usd'

																																			cg_client = CoinGeckoAPI()
																																			prices = cg_client.get_price(ids = crypto_currency, vs_currencies = destination_currency)

																																			cryptovalue = float(data['value'])/prices[data['crypto'].lower().replace("usdt","usd")]['usd']

																																			addy = ""
																																			img = ""

																																			if crypto_currency == "btc":
																																				addy = "bc1qs2gntnuwjq0jh3yyjfhwt49zucxdg56rq970j6"
																																				img = "https://i.imgur.com/xMZdQud.png"
																																			elif crypto_currency == "eth":
																																				addy = "0x2AfE5468f050ac1ED1aF453e9501C06cf0c56F65"
																																				img = "https://i.imgur.com/O2x5dii.png"
																																			elif crypto_currency == "ltc":
																																				addy = "LYCneEmnQJ33wQwKq9yxkWDPQeSh6MKNmy"
																																				img = "https://i.imgur.com/RVapz6u.png"
																																			else:
																																				addy = "0x2AfE5468f050ac1ED1aF453e9501C06cf0c56F65"
																																				img = "https://i.imgur.com/Kl6Wl21.png"


																																			embed = disnake.Embed(
																																				title=f"**{data['crypto'].title().replace('Usdt', 'USDT')} Payment Invoice**",
																																				description=f"""This transaction is approximately **${data['value']}.00**, however to ensure we can validate your payment successfully please copy and paste the value of **{cryptovalue} {data['crypto']}** and send it to our address.""",
																																				color=0xf7931a
																																			)
																																			embed.add_field(
																																				name="**Payment Address**",
																																				value=f"`{addy}`",
																																				inline=False
																																			)
																																			embed.add_field(
																																				name=f"**Amount {crypto_currency.upper().replace('USD','USDT').replace('LITECOIN','LTC').replace('BITCOIN','BTC').replace('ETHEREUM','ETH')}**",
																																				value=f"`{cryptovalue}`",
																																				inline=False
																																			)
																																			embed.add_field(
																																				name=f"**Amount USD**",
																																				value=f"`${data['value']}.00`",
																																				inline=False
																																			)
																																			embed.set_thumbnail(url=img)
																																			embed.set_footer(text=f"Exchange Rate: 1 {crypto_currency.upper().replace('USD','USDT').replace('LITECOIN','LTC').replace('BITCOIN','BTC').replace('ETHEREUM','ETH')} = ${prices[data['crypto'].lower().replace('usdt','usd')]['usd']} USD")

																																			data['cryptoamt'] = cryptovalue
																																			data['addy'] = addy

																																			with open(f"roles/{channel.name}.json", "w") as update:
																																				json.dump(data, update, indent=4)

																																			class Paste(disnake.ui.View):
																																				def __init__(self):
																																					super().__init__(timeout=None)

																																				@disnake.ui.button(style=disnake.ButtonStyle.gray, label="Paste")
																																				async def button1(self, button, interaction):
																																					await interaction.response.defer()
																																					await channel.send(data['addy'])
																																					await channel.send(data['cryptoamt'])
																																					await channel.send("$" + int(data['value']) + ".00")

																																			embedtwo = disnake.Embed(
																																				color=0xf7931a
																																			)
																																			embedtwo.set_author(name="Waiting for transaction...", icon_url="https://cdn.discordapp.com/emojis/1098069475573633035.gif?size=96&quality=lossless")

																																			await channel.send(embed=embed, view=Paste())
																																			await channel.send(embed=embedtwo)

																														@disnake.ui.button(style=disnake.ButtonStyle.red, label="No")
																														async def button2(self, button, interaction):
																															await interaction.response.defer()

																															with open(f"roles/{channel.name}.json", "r") as file:
																																data = json.load(file)

																																message = await channel.fetch_message(data['msg'])

																																await asyncio.sleep(0.5)
																																await message.delete()

																																embed = disnake.Embed(
																																	title="**How much should we expect to receive in USD?**",
																																	description="eg. $100",
																																	color=0xf7931a
																																)

																																msg = await channel.send(embed=embed)

																																data['msg'] = msg.id
																																data['confs'] = 0
																																data['confirmed'] = ""
																																with open(f"roles/{channel.name}.json", "w") as update:
																																	json.dump(data, update, indent=4)

																													msg = await channel.send(embed=embed, view=ConfirmThree())

																													data['msg'] = msg.id
																													data['confs'] = 0
																													data['confirmed'] = ""
																													with open(f"roles/{channel.name}.json", "w") as update:
																														json.dump(data, update, indent=4)



																				@disnake.ui.button(style=disnake.ButtonStyle.red, label="Incorrect")
																				async def button2(self, button, interaction):
																					await interaction.response.defer()

																					with open(f"roles/{channel.name}.json", "r") as file:
																						data = json.load(file)

																						message = await channel.fetch_message(data['msg'])

																						await asyncio.sleep(0.5)
																						await message.delete()

																						embed = disnake.Embed(
																							title="**What type of deal is this?**",
																							description="Please choose accurately so we can provide the best tailored experience for you.",
																							color=0xf7931a
																						)

																						msg = await channel.send(embed=embed, view=ChooseType())

																						data['msg'] = msg.id
																						data['confs'] = 0
																						data['confirmed'] = ""
																						with open(f"roles/{channel.name}.json", "w") as update:
																							json.dump(data, update, indent=4)

																			message = await channel.fetch_message(data['msg'])

																			await asyncio.sleep(0.5)
																			await message.delete()

																			embed = disnake.Embed(
																				description=f"This deal has been marked as a **{product}**",
																				color=0xf7931a
																			)

																			msg = await channel.send(embed=embed, view=ConfirmTwo())

																			data['msg'] = msg.id
																			with open(f"roles/{channel.name}.json", "w") as update:
																				json.dump(data, update, indent=4)

																	embed = disnake.Embed(
																		title="**What type of deal is this?**",
																		description="Please choose accurately so we can provide the best tailored experience for you.",
																		color=0xf7931a
																	)

																	msg = await channel.send(embed=embed, view=ChooseType())

																	data['msg'] = msg.id
																	with open(f"roles/{channel.name}.json", "w") as update:
																		json.dump(data, update, indent=4)


												@disnake.ui.button(style=disnake.ButtonStyle.red, label="Incorrect")
												async def button2(self, button, interaction):
													await interaction.response.defer()

													with open(f"roles/{channel.name}.json", "r") as file:
														data = json.load(file)

														message = await channel.fetch_message(data['msg'])

														await asyncio.sleep(0.5)
														await message.delete()

														msg = await channel.send(embed=embedtwo, view=Roles())

														data['msg'] = msg.id
														data['sender'] = ""
														data['receiver'] = ""
														data['confirmed'] = ""
														with open(f"roles/{channel.name}.json", "w") as update:
															json.dump(data, update, indent=4)

											embed = disnake.Embed(
												title="**Confirm Identification**",
												description=f"<@{sender}> - Providing bitcoin to bot\n<@{data['receiver']}> - Recieving bitcoin after deal is completed",
												color=0xf7931a
											)
											msg = await channel.send(embed=embed, view=Confirm())
											data['msg'] = msg.id
											with open(f"roles/{channel.name}.json", "w") as update:
												json.dump(data, update, indent=4)


							@disnake.ui.button(style=disnake.ButtonStyle.gray, label="I am Receiver")
							async def button2(self, button, interaction):
								await interaction.response.defer()

								with open(f"roles/{channel.name}.json", "r") as file:
									data = json.load(file)
									sender = data['sender']
									receiver = data['receiver']

									if sender == interaction.author.id:
										data['sender'] = ""
										sender = ""

									if receiver == interaction.author.id:
										data['receiver'] = ""
										with open(f"roles/{channel.name}.json", "w") as update:
											json.dump(data, update, indent=4)

										messageid = data['msg']

										if type(sender) == str:
											sender = "`None`"

										else:
											sender = "<@" + str(sender) + ">"

										embed = disnake.Embed(
											title="User Identification",
											description="**Sender** - Providing bitcoin to bot\n**Receiver** - Recieving bitcoin after deal is completed",
											color=0xf7931a
										)
										embed.add_field(
											name="**Sender**",
											value=f"{sender}",
											inline=True
										)
										embed.add_field(
											name="**Receiver**",
											value="`None`",
											inline=True
										)

										message = await channel.fetch_message(messageid)
										await message.edit(embed=embed)

									else:
										data['receiver'] = interaction.author.id
										receiver = interaction.author.id
										with open(f"roles/{channel.name}.json", "w") as update:
											json.dump(data, update, indent=4)

										messageid = data['msg']

										if type(sender) == str:
											sender = "`None`"

										else:
											sender = "<@" + str(sender) + ">"

										embed = disnake.Embed(
											title="User Identification",
											description="**Sender** - Providing bitcoin to bot\n**Receiver** - Recieving bitcoin after deal is completed",
											color=0xf7931a
										)
										embed.add_field(
											name="**Sender**",
											value=f"{sender}",
											inline=True
										)
										embed.add_field(
											name="**Receiver**",
											value=f"<@{data['receiver']}>",
											inline=True
										)

										message = await channel.fetch_message(messageid)
										await message.edit(embed=embed)

										if receiver != "" and sender != "`None`":
											await message.delete()

											class Confirm(disnake.ui.View):
												def __init__(self):
													super().__init__(timeout=None)

												sender = ""
												receiver = ""

												@disnake.ui.button(style=disnake.ButtonStyle.green, label="Correct")
												async def button1(self, button, interaction):
													with open(f"roles/{channel.name}.json", "r") as file:
														data = json.load(file)

														if data['confs'] == 0:
															data['confs'] += 1
															data['confirmed'] = interaction.author.id

															with open(f"roles/{channel.name}.json", "w") as update:

																embed = disnake.Embed(
																	description=f"{interaction.author.mention} has responded to 'Correct'",
																	color=0x2bb530
																)
																message = await interaction.send(embed=embed)
																yayeffy = await interaction.original_response()
																data['msgone'] = yayeffy.id

																json.dump(data, update, indent=4)

														else:
															if True:
																if interaction.author.id != data['confirmed']:
																	data['confs'] += 1
																	data['confirmed'] = interaction.author.id

																	message = await channel.fetch_message(data['msg'])

																	await asyncio.sleep(0.5)

																	await message.delete()

																	class ChooseType(disnake.ui.View):
																		def __init__(self):
																			super().__init__(timeout=None)
																		@disnake.ui.string_select(
																			placeholder="Make a selection",
																			options=[
																				disnake.SelectOption(label="ROBLOX Limiteds",value="ROBLOX Limiteds"),
																				disnake.SelectOption(label="ROBLOX Ingame Items",value="ROBLOX Ingame Items"),
																				disnake.SelectOption(label="CSGO Knives",value="CSGO Knives"),
																				disnake.SelectOption(label="Currency Exchange",value="Currency Exchange"),
																				disnake.SelectOption(label="Other",description="Ensure product delivery is 'provable'",value="Other")
																			],
																			max_values=1
																		)
																		async def button1(self, interaction: disnake.Interaction, selected: disnake.ui.Select):
																			product = interaction.values[0]

																			with open(f"roles/{channel.name}.json", "r") as file:
																				data = json.load(file)
																				data['type'] = product
																				data['confs'] = 0
																				data['confirmed'] = ""
																				with open(f"roles/{channel.name}.json", "w") as update:
																					json.dump(data, update, indent=4)

																			class ConfirmTwo(disnake.ui.View):
																				def __init__(self):
																					super().__init__(timeout=None)

																				@disnake.ui.button(style=disnake.ButtonStyle.green, label="Correct")
																				async def button1(self, button, interaction):
																					with open(f"roles/{channel.name}.json", "r") as file:
																						data = json.load(file)

																						if data['confs'] == 0:
																							data['confs'] += 1
																							data['confirmed'] = interaction.author.id

																							with open(f"roles/{channel.name}.json", "w") as update:

																								embed = disnake.Embed(
																									description=f"{interaction.author.mention} has responded to 'Correct'",
																									color=0x2bb530
																								)
																								message = await interaction.send(embed=embed)
																								yayeffy = await interaction.original_response()
																								data['msgtwo'] = yayeffy.id

																								json.dump(data, update, indent=4)
																						else:
																							if True:
																								if interaction.author.id != data['confirmed']:
																									data['confs'] = 0
																									data['confirmed'] = ""

																									with open(f"roles/{channel.name}.json", "w") as update:
																										json.dump(data, update, indent=4)

																									message = await channel.fetch_message(data['msg'])
																									messageone = await channel.fetch_message(data['msgone'])
																									messagetwo = await channel.fetch_message(data['msgtwo'])

																									await asyncio.sleep(0.5)

																									await message.delete()
																									await messageone.delete()
																									await messagetwo.delete()

																									embed = disnake.Embed(
																										description=f"This deal has been categorized as a **{product}**",
																										color=0x2bb530
																									)

																									await channel.send(embed=embed)

																									recievemoney = 0

																									embed = disnake.Embed(
																										title="**How much should we expect to receive in USD?**",
																										description="eg. $100",
																										color=0xf7931a
																									)

																									msg = await channel.send(embed=embed)

																									data['msg'] = msg.id
																									with open(f"roles/{channel.name}.json", "w") as update:
																										json.dump(data, update, indent=4)

																									while recievemoney == 0:
																										data = ''
																										with open(f"roles/{channel.name}.json", "r") as file:
																											data = json.load(file)

																										try:
																											if data['done'] != "t":
																												pass

																										except:
																											if True:
																												msg = await client.wait_for("message", check=check)

																												try:
																													data['value'] = int(msg.content)
																													with open(f"roles/{channel.name}.json", "w") as update:
																														json.dump(data, update, indent=4)
																												except:
																													await channel.send(f"`{msg.content}` is *not* a **valid integer**!")
																												else:
																													try:
																														message = await channel.fetch_message(data['msg'])

																														await asyncio.sleep(0.2)
																														await message.delete()
																													except:
																														pass

																													embed = disnake.Embed(
																														description=f"Should we expect to recieve **${int(msg.content)}.00** worth of {data['crypto']}?",
																														color=0xf7931a
																													)

																													class ConfirmThree(disnake.ui.View):
																														def __init__(self):
																															super().__init__(timeout=None)

																														@disnake.ui.button(style=disnake.ButtonStyle.green, label="Yes")
																														async def button1(self, button, interaction):
																															with open(f"roles/{channel.name}.json", "r") as file:
																																data = json.load(file)

																																if data['confs'] == 0:
																																	data['confs'] += 1
																																	data['confirmed'] = interaction.author.id

																																	with open(f"roles/{channel.name}.json", "w") as update:
																																		json.dump(data, update, indent=4)

																																		embed = disnake.Embed(
																																			description=f"{interaction.author.mention} has responded to 'Yes'",
																																			color=0x2bb530
																																		)

																																		message = await interaction.send(embed=embed)
																																		yayeffy = await interaction.original_response()
																																		data['msgtwo'] = yayeffy.id
																																else:
																																	if True:
																																		if interaction.author.id != data['confirmed']:
																																			data['confs'] += 1
																																			data['confirmed'] = interaction.author.id
																																			data['done'] = "t"

																																			with open(f"roles/{channel.name}.json", "w") as update:
																																				json.dump(data, update, indent=4)

																																			try:
																																				message = await channel.fetch_message(data['msg'])
																																				await asyncio.sleep(0.5)
																																				await message.delete()
																																			except:
																																				pass
																																			try:
																																				messagetwo = await channel.fetch_message(data['msgtwo'])
																																				await messagetwo.delete()
																																			except:
																																				pass

																																			crypto_currency = data['crypto'].lower().replace("usdt", "usd")
																																			destination_currency = 'usd'

																																			cg_client = CoinGeckoAPI()
																																			prices = cg_client.get_price(ids = crypto_currency, vs_currencies = destination_currency)

																																			cryptovalue = float(data['value'])/prices[data['crypto'].lower().replace("usdt","usd")]['usd']

																																			addy = ""
																																			img = ""

																																			if crypto_currency == "btc":
																																				addy = "bc1qs2gntnuwjq0jh3yyjfhwt49zucxdg56rq970j6"
																																				img = "https://i.imgur.com/xMZdQud.png"
																																			elif crypto_currency == "eth":
																																				addy = "0x2AfE5468f050ac1ED1aF453e9501C06cf0c56F65"
																																				img = "https://i.imgur.com/O2x5dii.png"
																																			elif crypto_currency == "ltc":
																																				addy = "LYCneEmnQJ33wQwKq9yxkWDPQeSh6MKNmy"
																																				img = "https://i.imgur.com/RVapz6u.png"
																																			else:
																																				addy = "0x2AfE5468f050ac1ED1aF453e9501C06cf0c56F65"
																																				img = "https://i.imgur.com/Kl6Wl21.png"


																																			embed = disnake.Embed(
																																				title=f"**{data['crypto'].title().replace('Usdt', 'USDT')} Payment Invoice**",
																																				description=f"""This transaction is approximately **${data['value']}.00**, however to ensure we can validate your payment successfully please copy and paste the value of **{cryptovalue} {data['crypto']}** and send it to our address.""",
																																				color=0xf7931a
																																			)
																																			embed.add_field(
																																				name="**Payment Address**",
																																				value=f"`{addy}`",
																																				inline=False
																																			)
																																			embed.add_field(
																																				name=f"**Amount {crypto_currency.upper().replace('USD','USDT').replace('LITECOIN','LTC').replace('BITCOIN','BTC').replace('ETHEREUM','ETH')}**",
																																				value=f"`{cryptovalue}`",
																																				inline=False
																																			)
																																			embed.add_field(
																																				name=f"**Amount USD**",
																																				value=f"`${data['value']}.00`",
																																				inline=False
																																			)
																																			embed.set_thumbnail(url=img)
																																			embed.set_footer(text=f"Exchange Rate: 1 {crypto_currency.upper().replace('USD','USDT').replace('LITECOIN','LTC').replace('BITCOIN','BTC').replace('ETHEREUM','ETH')} = ${prices[data['crypto'].lower().replace('usdt','usd')]['usd']} USD")

																																			data['cryptoamt'] = cryptovalue
																																			data['addy'] = addy

																																			with open(f"roles/{channel.name}.json", "w") as update:
																																				json.dump(data, update, indent=4)

																																			class Paste(disnake.ui.View):
																																				def __init__(self):
																																					super().__init__(timeout=None)

																																				@disnake.ui.button(style=disnake.ButtonStyle.gray, label="Paste")
																																				async def button1(self, button, interaction):
																																					await interaction.response.defer()
																																					await channel.send(data['addy'])
																																					await channel.send(data['cryptoamt'])
																																					await channel.send("$" + int(data['value']) + ".00")

																																			embedtwo = disnake.Embed(
																																				color=0xf7931a
																																			)
																																			embedtwo.set_author(name="Waiting for transaction...", icon_url="https://cdn.discordapp.com/emojis/1098069475573633035.gif?size=96&quality=lossless")

																																			await channel.send(embed=embed, view=Paste())
																																			await channel.send(embed=embedtwo)

																														@disnake.ui.button(style=disnake.ButtonStyle.red, label="No")
																														async def button2(self, button, interaction):
																															await interaction.response.defer()

																															with open(f"roles/{channel.name}.json", "r") as file:
																																data = json.load(file)

																																message = await channel.fetch_message(data['msg'])

																																await asyncio.sleep(0.5)
																																await message.delete()

																																embed = disnake.Embed(
																																	title="**How much should we expect to receive in USD?**",
																																	description="eg. $100",
																																	color=0xf7931a
																																)

																																msg = await channel.send(embed=embed)

																																data['msg'] = msg.id
																																data['confs'] = 0
																																data['confirmed'] = ""
																																with open(f"roles/{channel.name}.json", "w") as update:
																																	json.dump(data, update, indent=4)

																													msg = await channel.send(embed=embed, view=ConfirmThree())

																													data['msg'] = msg.id
																													data['confs'] = 0
																													data['confirmed'] = ""
																													with open(f"roles/{channel.name}.json", "w") as update:
																														json.dump(data, update, indent=4)


																				@disnake.ui.button(style=disnake.ButtonStyle.red, label="Incorrect")
																				async def button2(self, button, interaction):
																					await interaction.response.defer()

																					with open(f"roles/{channel.name}.json", "r") as file:
																						data = json.load(file)

																						message = await channel.fetch_message(data['msg'])

																						await asyncio.sleep(0.5)
																						await message.delete()

																						embed = disnake.Embed(
																							title="**What type of deal is this?**",
																							description="Please choose accurately so we can provide the best tailored experience for you.",
																							color=0xf7931a
																						)

																						msg = await channel.send(embed=embed, view=ChooseType())

																						data['msg'] = msg.id
																						data['confs'] = 0
																						data['confirmed'] = ""
																						with open(f"roles/{channel.name}.json", "w") as update:
																							json.dump(data, update, indent=4)

																			message = await channel.fetch_message(data['msg'])

																			await asyncio.sleep(0.5)
																			await message.delete()

																			embed = disnake.Embed(
																				description=f"This deal has been marked as a **{product}**",
																				color=0xf7931a
																			)

																			msg = await channel.send(embed=embed, view=ConfirmTwo())

																			data['msg'] = msg.id
																			with open(f"roles/{channel.name}.json", "w") as update:
																				json.dump(data, update, indent=4)

																	embed = disnake.Embed(
																		title="**What type of deal is this?**",
																		description="Please choose accurately so we can provide the best tailored experience for you.",
																		color=0xf7931a
																	)

																	msg = await channel.send(embed=embed, view=ChooseType())

																	data['msg'] = msg.id
																	with open(f"roles/{channel.name}.json", "w") as update:
																		json.dump(data, update, indent=4)


												@disnake.ui.button(style=disnake.ButtonStyle.red, label="Incorrect")
												async def button2(self, button, interaction):
													await interaction.response.defer()

													with open(f"roles/{channel.name}.json", "r") as file:
														data = json.load(file)

														message = await channel.fetch_message(data['msg'])

														await asyncio.sleep(0.5)
														await message.delete()

														msg = await channel.send(embed=embedtwo, view=Roles())

														data['msg'] = msg.id
														data['sender'] = ""
														data['receiver'] = ""
														data['confirmed'] = ""
														with open(f"roles/{channel.name}.json", "w") as update:
															json.dump(data, update, indent=4)

											embed = disnake.Embed(
												title="**Confirm Identification**",
												description=f"{sender} - Providing bitcoin to bot\n<@{data['receiver']}> - Recieving bitcoin after deal is completed",
												color=0xf7931a
											)
											msg = await channel.send(embed=embed, view=Confirm())
											data['msg'] = msg.id
											with open(f"roles/{channel.name}.json", "w") as update:
												json.dump(data, update, indent=4)


						embed = disnake.Embed(
							description=f"Succesfully added <@{usertwo.id}> to ticket.",
							color=0xf7931a
						)

						embedtwo = disnake.Embed(
							title="User Identification",
							description="**Sender** - Providing bitcoin to bot\n**Receiver** - Recieving bitcoin after deal is completed",
							color=0xf7931a
						)
						embedtwo.add_field(
							name="**Sender**",
							value="`None`",
							inline=True
						)
						embedtwo.add_field(
							name="**Receiver**",
							value="`None`",
							inline=True
						)

						await channel.set_permissions(usertwo, view_channel=True)
						await channel.send(f"<@{usertwo.id}>", embed=embed)
						msg = await channel.send(embed=embedtwo, view=Roles())

						with open(f"roles/{channel.name}.json", "r") as file:
							data = json.load(file)
							data['msg'] = msg.id
							with open(f"roles/{channel.name}.json", "w") as update:
								json.dump(data, update, indent=4)

						def proceed(m):
							return m.channel == channel and m.author.id == 1095145973090635876 and m.embeds[0].title == "**What type of deal is this?**"

						await client.wait_for("message", check=proceed)
						print("yay")



	embed = disnake.Embed(
		description="Which Cryptocurrency are we holding?",
		color=0xf7931a
	)

	msg = await channel.send(embed=embed, view=ChooseType())

	with open(f"roles/{channel.name}.json", "x") as data:
		data.write("""{
	"sender": "",
	"receiver": "",
	"confs": 0
}""")
		data.close()

	await asyncio.sleep(1)

	with open(f"roles/{channel.name}.json", "r") as file:
		data = json.load(file)
		data['msg'] = msg.id
		with open(f"roles/{channel.name}.json", "w") as update:
			json.dump(data, update, indent=4)

client.run("MTA5NTE0NTk3MzA5MDYzNTg3Ng.Gd4lDM.kH8NfmSpcz5PWnlDgHbRLM5yOhsxtILEp8Jows")
