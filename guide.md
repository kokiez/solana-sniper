# Guide on how to run my project without errors!

## Chapter 1: Install the requirements.
1. Install `Python`. The version for python does not matter as long as it is above **3.0**.
2. Run the command `pip install -r requirements.txt` (Note: you machine might have `python3` and `pip3`).
3. If you get errors while installing, please copy and paste the error in chatgpt. **DO NOT Text ME THE ERROR**. Github is a developers community and you must know the basics already.

## Chapter 2: Config file.
### Section 1: Telegram.
1. Go to [Telegram API development tools](https://my.telegram.org/auth?to=apps).
2. Enter your number, you will receive the code in your telegram application. Enter code and press next.
3. Fill out the form as follows:
      - App Title: Solana Sniper
      - Short Name: SolBot
      - URL: https://my.telegram.org/
      - Platform: Desktop
4. You will receive `api_id` and `api_hash` which you should replace in config.ini file.
5. **Session name** can be anything. First time, when you run the bot, it will ask for your number and the code. At this point `telethon library` will create your telegram session.
6. **Sender Username**, it is the username of channels from where you will receive. Note that the sender in the channel is most likely having the same username as channel username. An example is given below:
![Example1](https://i.ibb.co/Cvqtbhx/Screenshot-2024-01-02-233151.png)

## Chapter 3: Investment
-  Config.ini already has description due to which I wont write about it here.

## Chapter 4: DISCORD Webhook URls
- You may skip it, but in order to get updates from bot while it is running. This is the best option.
1. Create a discord server, goto channel settings, goto integrations and create a webhook. Copy the url and add it to config file.

## Chapter 5: Wallet Key
- Every wallet has different settings. With intention of testing this bot, you must already have this information.
- But when you get the key, it may look something like this `asuhduiahsw812y98dajsdui172yashduiahsuidh11sjhdahduiashduh1892hdhsuahdh199d89hashANDSO1ON`

## Chapter 6: Birdeye
**Skip**

## Chapter 7: INFURA URL
1. Goto alchemy and create your endpoint for solana. Copy the https url and add it to config.ini

## Final
1. You can create a test channel and add the username to config.ini to test the bot.
2. Run `python main.py`.
3. It will display **Message Received** if telethon is working and CA will show up if the **senderusernames are correct**.