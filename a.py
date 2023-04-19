class Roles(disnake.ui.View):
		def __init__(self):
			super().__init__(timeout=None)

		sender = ""
		reciever = ""
	
		@disnake.ui.button(style=disnake.ButtonStyle.gray, label="I am Sender")
		async def button1(self, interaction, button):
			interaction = await client.wait_for("button_click", check=lambda i: i.component.label)
			await interaction.response.defer()

			print("clicked send")
			
			with open(f"roles/{channel.name}.json", "r") as file:
				data = json.load(file)
				sender = data['sender']
				reciever = data['reciever']
				print(sender)
				print(reciever)

				if reciever == interaction.author.id:
					data['reciever'] = ""
					reciever = ""

				if sender == interaction.author.id:
					data['sender'] = ""
					with open(f"roles/{channel.name}.json", "w") as update:
						json.dump(data, update, indent=4)
						
					messageid = data['msg']
					
					if type(reciever) == str:
						reciever = "`None`"

					embed = disnake.Embed(
						title="User Identification",
						description="**Sender** - Providing bitcoin to bot\n**Reciever** - Recieving bitcoin after deal is completed",
						color=0xf7931a
					)
					embed.add_field(
						name="**Sender**",
						value="`None`",
						inline=True
					)
					embed.add_field(
						name="**Reciever**",
						value=f"{reciever}",
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

					if type(reciever) == str:
						reciever = "None"

					embed = disnake.Embed(
						title="User Identification",
						description="**Sender** - Providing bitcoin to bot\n**Reciever** - Recieving bitcoin after deal is completed",
						color=0xf7931a
					)
					embed.add_field(
						name="**Sender**",
						value=f"<@{data['sender']}>",
						inline=True
					)
					embed.add_field(
						name="**Reciever**",
						value=f"`{reciever}`",
						inline=True
					)
					
					message = await channel.fetch_message(messageid)
					await message.edit(embed=embed)

			
		@disnake.ui.button(style=disnake.ButtonStyle.gray, label="I am Reciever")
		async def button2(self, interaction, button):
			interaction = await client.wait_for("button_click", check=lambda i: i.component.label)
			await interaction.response.defer()
			print("clicked recieve")
			
			with open(f"roles/{channel.name}.json", "r") as file:
				data = json.load(file)
				sender = data['sender']
				reciever = data['reciever']

				if sender == interaction.author.id:
					data['sender'] = ""
					sender = ""

				if reciever == interaction.author.id:
					data['reciever'] = ""
					with open(f"roles/{channel.name}.json", "w") as update:
						json.dump(data, update, indent=4)
						
					messageid = data['msg']
					
					if type(sender) == str:
						sender = "None"

					embed = disnake.Embed(
						title="User Identification",
						description="**Sender** - Providing bitcoin to bot\n**Reciever** - Recieving bitcoin after deal is completed",
						color=0xf7931a
					)
					embed.add_field(
						name="**Sender**",
						value=f"`{sender}`",
						inline=True
					)
					embed.add_field(
						name="**Reciever**",
						value="`None`",
						inline=True
					)
					
					message = await channel.fetch_message(messageid)
					await message.edit(embed=embed)

				else:
					data['reciever'] = interaction.author.id
					reciever = interaction.author.id
					with open(f"roles/{channel.name}.json", "w") as update:
						json.dump(data, update, indent=4)

					messageid = data['msg']

					if type(sender) == str:
						sender = "None"

					embed = disnake.Embed(
						title="User Identification",
						description="**Sender** - Providing bitcoin to bot\n**Reciever** - Recieving bitcoin after deal is completed",
						color=0xf7931a
					)
					embed.add_field(
						name="**Sender**",
						value=f"`{sender}`",
						inline=True
					)
					embed.add_field(
						name="**Reciever**",
						value=f"<@{data['reciever']}>",
						inline=True
					)
					
					message = await channel.fetch_message(messageid)
					await message.edit(embed=embed)