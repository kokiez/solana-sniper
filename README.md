# Solana Sniper Bot

The Solana Sniper is a powerful Python-based tool designed to automate the process of buying and selling coins on the Solana blockchain. It allows you to set stop loss and limit orders, enabling you to execute trades automatically based on your predefined criteria. The sniper will snipe tokens from telegram channels based on CA or a birdeye url.

## Requirements

To use the Solana Sniper, you will need the following:

- Python 3.x installed on your machine.
- A Solana wallet with sufficient funds for trading and must have the private key in the form of alphanumeric string.
- Access to Telegram channels for receiving trade signals.
- Discord Webhook urls.
- Telegram bot api keys.
- Solana RPC Provider's HTTPS URL

## Getting Started

1. Clone the repository:
    ```shell
    git clone https://github.com/kokiez/solana-sniper.git
    ```

2. Install the required dependencies:
    ```shell
    pip install -r requirements.txt
    ```

3. Configure the Solana Sniper by editing the `./data/config.py` file. Set your wallet private key or a json file of your keypair, Telegram API keys, and other necessary parameters. Each of the required item has a description written in config file, if you do not fill the config.ini correctly, the sniper may crash or not work at all.

4. Run the Solana Sniper:
    ```shell
    python main.py
    ```
## Donations

If you find the Solana Sniper useful, consider making a donation to support its development and maintenance. Your contribution will help us continue to improve the tool and add new features.

Solana Wallet Address: `KoqQCqxD2ca1St64U4Sc3tBnNfXo6761dETUK4dSpDt`

## FAQS
### 1. How to install requirements?
Each OS is different from mine, I cannot assist you and guide you step by step on how to install requirements... In the current world, chatgpt exists, you may ask chatgpt such questions. Its simple run the command, if you get error then read it and try to understand what the error is saying or check the error on chatgpt.
### 2. Program did not show up anything and stopped!
Most likely your config.ini is missing, you have to put the right data in it e.g. Required sections are [TELEGRAM], [DISCORD], [WALLET] and [INFURA_URL]
### 3. What is senderUserNames in config.ini section TELEGRAM?
It is the username of channel where the tokens are pasted, the bot would like to know those usernames and then snipe the tokens.

## Contact

For any business inquiries or support, please reach out to us:

- Discord: `kokiez4000`
- Telegram: `kokiez4000`

Happy trading with the Solana Sniper!

