from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('GT1ov7ToSY1D9CXvmrGEfB0bdr69ZME9rPSXDHF4M/K80pv5eAWkSFF1QQYdOSOVPTdaHODrT/RAPT5j9cfh1UkWMNlGCjOL580zrEVaomR9P29HJ2XVj/N2qTK79XlLp6MKup8i0gJO3b5DE8JxEQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ddc9447db59e76883e563d54bd9505a6')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='哈哈哈'))


if __name__ == "__main__":
    app.run()