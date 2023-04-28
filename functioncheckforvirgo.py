import asyncio


@asyncio.coroutine
def check_for_virgo(message,):
    if "я фанатка вірго" in message.content.lower() and message.author != client.user:
        response = "я фанатка вірго"
        yield from message.reply(response)