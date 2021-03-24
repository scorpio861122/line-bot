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

line_bot_api = LineBotApi('l4n2N8rQrHsGUx3loLoP/dPRHZWSjU6VY8h23CB8uPKNeO+BOVx3pZnWUWi4kNB9Yun/DHMhNqrgF8hqL0mp5loFq0XJDYoR1qj9rsygdFKcu6u8OzOeP+8w2Gu+M4svvz6DD6qVRE9ETbNWS+J0JwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('324daf3a7501581cbaa501838e091d0b')


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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if usage == 'create':
    rich_menu_to_create = RichMenu(
        size=RichMenuSize(width=2500, height=843),
        selected=False,
        name="Nice richmenu",  # display name
        chat_bar_text="我是測試使用",
        areas=[RichMenuArea(  # 這邊是陣列的格式，可以動態設定自己要的區域想要有什麼功能
            bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
            action=URIAction(label='Go to line.me', uri='https://line.me'))]
    )
    rich_menu_id = self.line_bot_api.create_rich_menu(
        rich_menu=rich_menu_to_create)
    print(rich_menu_id)
    return {'id': rich_menu_id}, 200

if __name__ == "__main__":
    app.run()