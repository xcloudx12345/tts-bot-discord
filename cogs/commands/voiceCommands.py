import discord
from discord.ext import commands
from gtts import gTTS
from zalo_tts import ZaloTTS
import gtts
import zalo_tts
import nacl
from discord import FFmpegPCMAudio
from mutagen.mp3 import MP3
import configparser

class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.settings = configparser.ConfigParser(comment_prefixes='/', allow_no_value=True)
        self.settings.read('settings.ini')
        self.commandPrefix = self.settings['DEFAULT']['commandPrefix']
    
    @commands.guild_only()
    @commands.command(name="connect", 
                    description="Gọi 8 vào channel voice đang ngồi.", 
                    brief="Voice")
    async def connect(self, ctx):
        if ctx.author.voice != None:
            if ctx.voice_client == None:
                await ctx.author.voice.channel.connect()
            else:
                sameChannel = False
                for voice_client in self.client.voice_clients:
                    if voice_client.channel == ctx.author.voice.channel:
                        sameChannel = True
                        break
                if not sameChannel:
                    await ctx.voice_client.disconnect()
                    await ctx.author.voice.channel.connect()
        else:
            await ctx.send("Vào channel nào đi rồi gọi chị nha cưng.")

    @commands.guild_only()
    @commands.command(name="disconnect", 
                    description="Bot thoát channel", 
                    brief="Voice")
    async def disconnect(self, ctx):
        if ctx.voice_client != None:
            await ctx.voice_client.disconnect()

    @commands.guild_only()
    @commands.command(name="s", 
                    description="Giọng nữ miền nam. \n nhắn tối đa 200 ký tự.", 
                    brief="Voice")
    async def s(self, ctx, *, args=""):
        if len(args) < 200 and len(args) > 0:
            if ctx.author.voice != None:
                if ctx.voice_client == None:
                    await ctx.author.voice.channel.connect()
                else:
                    sameChannel = False
                    for voice_client in self.client.voice_clients:
                        if voice_client.channel == ctx.author.voice.channel:
                            sameChannel = True
                            break
                    if not sameChannel:
                        await ctx.voice_client.disconnect()
                        await ctx.author.voice.channel.connect()
            else:
                await ctx.send("Vào channel nào đi rồi gọi chị nha cưng.")

            if not ctx.voice_client.is_playing():
                try:
                    language = self.settings['sever.languages'][str(ctx.guild.id)]
                except:
                    language = "en"
                try:
                    tts = ZaloTTS(speaker=ZaloTTS.SOUTH_WOMEN,api_key='pQwVAuXeXCsipiVtOFGsdLMbhwtJkXaf')
                    tts.text_to_audio(args,f".ttsTemp{ctx.guild.id}.mp3")
                except:
                    await ctx.send("Something went wrong while trying to reach the api.")

                source = FFmpegPCMAudio(f".ttsTemp{ctx.guild.id}.mp3")
                player = ctx.voice_client.play(source)
        else:
            await ctx.send("Tin nhắn phải trong khoảng >0 và <200 ký tự")

    @commands.guild_only()
    @commands.command(name="s2", 
                    description="Giọng nữ miền bắc. \n nhắn tối đa 200 ký tự.", 
                    brief="Voice")
    async def s2(self, ctx, *, args=""):
        if len(args) < 200 and len(args) > 0:
            if ctx.author.voice != None:
                if ctx.voice_client == None:
                    await ctx.author.voice.channel.connect()
                else:
                    sameChannel = False
                    for voice_client in self.client.voice_clients:
                        if voice_client.channel == ctx.author.voice.channel:
                            sameChannel = True
                            break
                    if not sameChannel:
                        await ctx.voice_client.disconnect()
                        await ctx.author.voice.channel.connect()
            else:
                await ctx.send("Vào channel nào đi rồi gọi chị nha cưng.")

            if not ctx.voice_client.is_playing():
                try:
                    language = self.settings['sever.languages'][str(ctx.guild.id)]
                except:
                    language = "en"
                try:
                    tts = ZaloTTS(speaker=ZaloTTS.NORTHERN_WOMEN,api_key='pQwVAuXeXCsipiVtOFGsdLMbhwtJkXaf')
                    tts.text_to_audio(args,f".ttsTemp{ctx.guild.id}.mp3")
                except:
                    await ctx.send("Something went wrong while trying to reach the api.")

                source = FFmpegPCMAudio(f".ttsTemp{ctx.guild.id}.mp3")
                player = ctx.voice_client.play(source)
        else:
            await ctx.send("Tin nhắn phải trong khoảng >0 và <200 ký tự")
    @commands.guild_only()
    @commands.command(name="s3", 
                    description="Giọng nữ nam miền nam. \n nhắn tối đa 200 ký tự.", 
                    brief="Voice")
    async def s3(self, ctx, *, args=""):
        if len(args) < 200 and len(args) > 0:
            if ctx.author.voice != None:
                if ctx.voice_client == None:
                    await ctx.author.voice.channel.connect()
                else:
                    sameChannel = False
                    for voice_client in self.client.voice_clients:
                        if voice_client.channel == ctx.author.voice.channel:
                            sameChannel = True
                            break
                    if not sameChannel:
                        await ctx.voice_client.disconnect()
                        await ctx.author.voice.channel.connect()
            else:
                await ctx.send("Vào channel nào đi rồi gọi chị nha cưng.")

            if not ctx.voice_client.is_playing():
                try:
                    language = self.settings['sever.languages'][str(ctx.guild.id)]
                except:
                    language = "en"
                try:
                    tts = ZaloTTS(speaker=ZaloTTS.SOUTH_MEN,api_key='pQwVAuXeXCsipiVtOFGsdLMbhwtJkXaf')
                    tts.text_to_audio(args,f".ttsTemp{ctx.guild.id}.mp3")
                except:
                    await ctx.send("Something went wrong while trying to reach the api.")

                source = FFmpegPCMAudio(f".ttsTemp{ctx.guild.id}.mp3")
                player = ctx.voice_client.play(source)
        else:
            await ctx.send("Tin nhắn phải trong khoảng >0 và <200 ký tự")
    @commands.guild_only()
    @commands.command(name="s4", 
                    description="Giọng nữ nam miền bắc. \n nhắn tối đa 200 ký tự.", 
                    brief="Voice")
    async def s4(self, ctx, *, args=""):
        if len(args) < 200 and len(args) > 0:
            if ctx.author.voice != None:
                if ctx.voice_client == None:
                    await ctx.author.voice.channel.connect()
                else:
                    sameChannel = False
                    for voice_client in self.client.voice_clients:
                        if voice_client.channel == ctx.author.voice.channel:
                            sameChannel = True
                            break
                    if not sameChannel:
                        await ctx.voice_client.disconnect()
                        await ctx.author.voice.channel.connect()
            else:
                await ctx.send("Vào channel nào đi rồi gọi chị nha cưng.")

            if not ctx.voice_client.is_playing():
                try:
                    language = self.settings['sever.languages'][str(ctx.guild.id)]
                except:
                    language = "en"
                try:
                    tts = ZaloTTS(speaker=ZaloTTS.NORTHERN_MEN,api_key='pQwVAuXeXCsipiVtOFGsdLMbhwtJkXaf')
                    tts.text_to_audio(args,f".ttsTemp{ctx.guild.id}.mp3")
                except:
                    await ctx.send("Something went wrong while trying to reach the api.")

                source = FFmpegPCMAudio(f".ttsTemp{ctx.guild.id}.mp3")
                player = ctx.voice_client.play(source)
        else:
            await ctx.send("Tin nhắn phải trong khoảng >0 và <200 ký tự")
    @commands.guild_only()
    @commands.command(name="gg", 
                    description="Chị Google", 
                    brief="Voice")
    async def gg(self, ctx, *, args=""):
        if len(args) < 200 and len(args) > 0:
            if ctx.author.voice != None:
                if ctx.voice_client == None:
                    await ctx.author.voice.channel.connect()
                else:
                    sameChannel = False
                    for voice_client in self.client.voice_clients:
                        if voice_client.channel == ctx.author.voice.channel:
                            sameChannel = True
                            break
                    if not sameChannel:
                        await ctx.voice_client.disconnect()
                        await ctx.author.voice.channel.connect()
            else:
                await ctx.send("Vào channel nào đi rồi gọi chị nha cưng.")

            if not ctx.voice_client.is_playing():
                try:
                    language = self.settings['sever.languages'][str(ctx.guild.id)]
                except:
                    language = "vi"
                try:
                    gTTS(text=args, lang=language, slow=False).save(f".ttsTemp{ctx.guild.id}.mp3")
                except:
                    await ctx.send("Something went wrong while trying to reach the api.")

                source = FFmpegPCMAudio(f".ttsTemp{ctx.guild.id}.mp3")
                player = ctx.voice_client.play(source)
        else:
            await ctx.send("Tin nhắn phải trong khoảng >0 và <200 ký tự")
    @commands.guild_only()
    @commands.command(name="setlang", 
                    description="Chỉnh ngôn ngữ cho chị google.", 
                    brief="Voice")
    async def setlang(self, ctx, *, args=""):
        languages = ""
        languageCodes = []
        for key, value in gtts.lang.tts_langs().items():
            languages = languages + f"`{key}`: {value} \n"
            languageCodes.append(key)

        if args in languageCodes:
            self.settings['sever.languages'][str(ctx.guild.id)] = args
            with open('settings.ini', 'w') as settingsfile:
                self.settings.write(settingsfile)
            await ctx.send(f"Đã set ngôn ngữ sang `{args}`")

            self.settings.read('settings.ini')
        elif args == "" or args == None or args == " ":
            await ctx.send(f"Hãy gõ mã ngôn ngữ cần set. \nGõ `{self.commandPrefix}supportedlanguages` để xem danh sách ngôn ngữ.")
        else:
            await ctx.send(f"Mã bị sai. \nGõ `{self.commandPrefix}supportedlanguages` để xem danh sách ngôn ngữ.")
        
    @commands.command(name="suplang", 
                    description="Xem danh sách ngôn ngữ của chị google.", 
                    brief="Voice")
    async def suplang(self, ctx):
        languages = ""
        for key, value in gtts.lang.tts_langs().items():
            languages = languages + f"`{key}`: {value} \n"

        await ctx.send(languages)

def setup(bot):
    bot.add_cog(Voice(bot))