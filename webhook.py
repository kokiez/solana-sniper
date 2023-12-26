import os, sys, json, requests
from configparser import ConfigParser
config = ConfigParser()
config.read(os.path.join(sys.path[0], 'data', 'config.ini'))
webhook_url =  config.get("DISCORD", "webhook_url")
error_webhook = config.get("DISCORD", "error_webhook")
colors = {
    "Aqua": 1752220,
    "DarkAqua": 1146986,
    "Green": 5763719,
    "DarkGreen": 2067276,
    "Blue": 3447003,
    "DarkBlue": 2123412,
    "Purple": 10181046,
    "DarkPurple": 7419530,
    "LuminousVividPink": 15277667,
    "DarkVividPink": 11342935,
    "Gold": 15844367,
    "DarkGold": 12745742,
    "Orange": 15105570,
    "DarkOrange": 11027200,
    "Red": 15548997,
    "DarkRed": 10038562,
    "Grey": 9807270,
    "DarkGrey": 9936031,
    "DarkerGrey": 8359053,
    "LightGrey": 12370112,
    "Navy": 3426654,
    "DarkNavy": 2899536,
    "Yellow": 16776960
}


def webhook(title, color, description, webhook_url):
    # Message content
    message_content = {
        "embeds": [
            {
                "title": title,
                "color": color,  # Green color (decimal)
                "description": description
            }
        ]
    }

    # Convert message content to JSON
    data = json.dumps(message_content)

    # Send the POST request to the webhook URL
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=data, headers=headers)

    # Check the response status
    if response.status_code == 204:
        print("[Discord Webhook] Discord Webhook sent")
    else:
        print(f"[Discord Webhook] Failed. Status code: {response.status_code}")
        print(response.text)  # Print any error response from Discord


def sendWebhook(title_type_info, description):
    global error_webhook
    global webhook_url
    title = ""
    title_type = title_type_info.split("|")
    if title_type[0] == "msg":
        title = title_type[1]
        color = colors["Green"]
        webhook(title, color, description, webhook_url)
    
    elif title_type[0] == "msg_b":
        title = title_type[1]
        color = colors["DarkAqua"]
        webhook(title, color, description, webhook_url)

    elif title_type[0] == "msg_s":
        title = title_type[1]
        color = colors["DarkAqua"]
        webhook(title, color, description, webhook_url)

    elif title_type[0] == "i_s": #invest or slippage was changed etc
        title = title_type[1]
        color = colors["DarkPurple"]
        webhook(title, color, description, webhook_url)
    
    elif title_type[0] == "e": #error
        title = title_type[1]
        color = colors["DarkRed"]
        webhook(title, color, description, error_webhook)

    elif title_type[0] == "a": #alert
        title = title_type[1]
        color = colors["LuminousVividPink"]
        webhook(title, color, description, webhook_url)

    elif title_type[0] == "w": #wallet info
        title = title_type[1]
        color = colors["Gold"]
        webhook(title, color, description, webhook_url)

