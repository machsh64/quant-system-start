import requests
from flask import Flask, request
from letta_client import Letta, MessageCreate, TextContent

app = Flask(__name__)


def chat_with_letta(messages):
    letta_client = Letta(
        base_url="http://192.168.188.4:8283",
        token="lett.+",
        project="default-project"
    )

    letta_response = letta_client.agents.messages.create(
        agent_id="agent-4f9969c554cad0",
        messages=[
            MessageCreate(
                role="user",
                content=[
                    TextContent(
                        text=messages,
                    )
                ],
            )
        ],
    )

    reasoning = next((msg.reasoning for msg in letta_response.messages
                      if msg.message_type == 'reasoning_message' and hasattr(msg, 'reasoning')), "")
    assistant = next((msg.content for msg in letta_response.messages
                      if msg.message_type == 'assistant_message' and hasattr(msg, 'content')), "")

    if reasoning and assistant:
        return assistant
    elif assistant:
        return assistant
    else:
        return reasoning


@app.route("/dingding/callback", methods=["POST"])
def dingding_callback():
    body = request.json
    print("收到钉钉事件：", body)

    # 1. 获取消息文本
    text_obj = body.get("text", {})
    content = body.get("senderNick", "无名用户") + " : " + text_obj.get("content", "")

    # 2. 获取 sessionWebhook
    session_webhook = body.get("sessionWebhook")

    if not session_webhook:
        return "no sessionWebhook", 400

    # 3. 构造回复内容
    reply = {
        "msgtype": "text",
        "text": {
            "content": chat_with_letta(content)
        }
    }

    # 4. 调用 sessionWebhook 回复群消息
    try:
        resp = requests.post(session_webhook, json=reply, headers={"Content-Type": "application/json"})
        print("发送结果：", resp.status_code, resp.text)
    except Exception as e:
        print("发送失败：", e)
        return "error", 500

    # 返回 success，表示事件已处理
    return "success"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8189, debug=True)
