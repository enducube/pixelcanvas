import discord
from PIL import Image

class PlaceBot(discord.Bot):
    async def on_ready(self):
        print(f"ready to go {self.user}")


client = PlaceBot()

colours = {
    "red": (255, 0, 0),
    "orange": (255, 128, 0),
    "yellow": (255, 255, 0),
    "green": (0, 255, 0),
    "cyan": (0, 255, 255),
    "blue": (0, 0, 255),
    "indigo": (180, 0 ,255),
    "purple": (180, 0, 180),
    "magenta": (255, 0, 180),
    "pink": (255, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
   
}

@client.slash_command(name="help")
async def help(ctx):
    e = discord.Embed(title="pixelcanvas bot commands")
    e.add_field(name="/canvas", value="display the canvas", inline=False)
    e.add_field(name="/colours", value="lists the available colours", inline=False)
    e.add_field(name="/pixel", value="places a pixel on the canvas from a list of colours", inline=False)
    e.add_field(name="/pixelrgb", value="places a pixel on the canvas from rgb values", inline=False)
    e.set_footer(text="if you encounter any issues/bugs then too bad - enducube#1211")
    await ctx.respond(embed=e)

@client.slash_command(name="canvas", description="display the canvas")
async def view(ctx):
    #user = ctx.author
    img = Image.open("place.png")
    simg = img.resize((128,128), resample=Image.Resampling.BOX)
    simg.save("pr.png")
    file=discord.File("pr.png")
    e = discord.Embed(title=str("the canvas"))
    e.set_image(url="attachment://pr.png")
    width, height = img.size
    e.set_footer(text=f"size: {width}, {height}")
    await ctx.respond(embed=e, file=file)

@client.slash_command(name="pixel", description="places a pixel on the canvas from a list of colours")
async def pixelrgb(ctx, x: int, y: int, colour: str):
    user = ctx.author
    img = Image.open("place.png")
    pixels = img.load()
    try:
        pixels[x,y] = colours[colour.lower()]
    except:
        await ctx.respond(text="please choose x and y values from 0 to 31")
        return
    img.save("place.png")
    simg = img.resize((128,128), resample=Image.Resampling.BOX)
    simg.save("pr.png")
    file=discord.File("pr.png")
    e = discord.Embed(title=f"{user.name} has placed a pixel at {x}, {y}")
    e.set_image(url="attachment://pr.png")
    await ctx.respond(embed=e, file=file)

@client.slash_command(name="pixelrgb", description="places a pixel on the canvas from rgb values")
async def pixelrgb(ctx, x: int, y: int, red: int, green: int, blue: int):
    user = ctx.author
    img = Image.open("place.png")
    pixels = img.load()
    try:
        pixels[x,y] = (red, green, blue)
    except:
        await ctx.respond(text="please choose x and y values from 0 to 31")
        return
    img.save("place.png")
    simg = img.resize((128,128), resample=Image.Resampling.BOX)
    simg.save("pr.png")
    file=discord.File("pr.png")
    e = discord.Embed(title=f"{user.name} has placed a pixel at {x}, {y}")
    e.set_image(url="attachment://pr.png")
    await ctx.respond(embed=e, file=file)
    
@client.slash_command(name="colours", description="lists the available colours")
async def listcolours(ctx):
    e = discord.Embed(title=f"list of colours")
    for colour in colours.keys():
        e.add_field(name=colour, value=str(colours[colour]), inline=True)
    e.set_footer(text="you can also use /pixelrgb to set an rgb value to your pixel")
    await ctx.respond(embed=e)
client.run('TOKEN')
