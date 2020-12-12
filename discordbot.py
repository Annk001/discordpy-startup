from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は処理しない
    if message.author.bot:
        return
#サーバーの起動
    if message.content == '/start':
        await message.channel.send('Server starting up...')
        await message.channel.send('※「start up」が表示されるまで他のコマンドを実行させないこと※')
        os.system('gcloud --account=<サービスアカウント名>@<プロジェクト名>.iam.gserviceaccount.com compute instances start <インスタンス名> --project <プロジェクト名> --zone <ゾーン名>')
        await message.channel.send('up .minecraft_server starting...')
        time.sleep(60)
        await message.channel.send('start up')
#サーバーの停止
    if message.content == '/stop':
        await message.channel.send('Server is stopping')
        await message.channel.send('※「down」が表示されるまで他のコマンドを実行させないこと※')
        os.system('gcloud --account=<サービスアカウント名>@<プロジェクト名>.iam.gserviceaccount.com compute instances stop <インスタンス名> --project <プロジェクト名> --zone <ゾーン名>')
        await message.channel.send('down')

#ヘルプの表示
    if message.content == '/help':
        await message.channel.send('/start : サーバの起動')
        await message.channel.send('/stop : サーバの停止') 
        
@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
