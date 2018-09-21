import discord
from discord.ext import commands
from utils import vars, perms, usage

class Brackets:

    slots = ("bot")

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="brackets enable", aliases=["b!enable"])
    async def cmd_brackets_enable(self, ctx): # Enable brackets for this server
        guild_id = ctx.guild.id
        await ctx.send(ctx.author.mention + " Not implemented yet.")
        usage.update(ctx)
        return ctx.command.name

    @commands.command(name="brackets disable", aliases=["b!disable"])
    async def cmd_brackets_disable(self, ctx): # Disable brackets for this server
        guild_id = ctx.guild.id
        await ctx.send(ctx.author.mention + " Not implemented yet.")
        usage.update(ctx)
        return ctx.command.name

    @commands.command(name="brackets addgroup", aliases=["b!addgroup"])
    async def cmd_brackets_addgroup(self, ctx, name): # Adds a group for this server
        guild_id = ctx.guild.id
        await ctx.send(ctx.author.mention + " Not implemented yet.")
        usage.update(ctx)
        return ctx.command.name