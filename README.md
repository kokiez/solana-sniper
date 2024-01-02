# This project was uploaded for educational purposes and an alternative to bots like bonkbot, this is not a pre-launch token sniper!
# Solana Sniper Bot

The Solana Sniper is a powerful Python-based tool designed to automate the process of buying and selling coins on the Solana blockchain. It allows you to set stop loss and limit orders, enabling you to execute trades automatically based on your predefined criteria. The sniper will snipe tokens from telegram channels based on CA or a birdeye url. Raydium has been added too because Jupiter does not support low liquidity coins.

## Requirements

To use the Solana Sniper, you will need the following:

- Python 3.x installed on your machine.
- A Solana wallet with sufficient funds for trading and must have the private key in the form of alphanumeric string.
- Access to Telegram channels for receiving trade signals.
- Discord Webhook urls.
- Telegram bot api keys.
- Solana RPC Provider's HTTPS URL

## Getting Started

1. Clone the repository and move to the directory:
    ```shell
    git clone https://github.com/kokiez/solana-sniper.git
    cd solana-sniper
    ```
2. Read it here in detail, [CLick me](https://github.com/kokiez/solana-sniper/blob/main/guide.md)


## Donations

If you find the Solana Sniper useful, consider making a donation to support its development and maintenance. Your contribution will help us continue to improve the tool and add new features.

Solana Wallet Address: `KoqQCqxD2ca1St64U4Sc3tBnNfXo6761dETUK4dSpDt`

## Contact

For any business inquiries or support, please reach out to us:

- Discord: `kokiez4000`
- Telegram: `kokiez4000`

Happy trading with the Solana Sniper!

## Proof of its working

**Note**: The result is a bit different from the version in github (prices are changed to worth) as I work on the bot everyday almost to improve it. 

![1](https://github.com/kokiez/solana-sniper/assets/105941365/2131ce16-1b5c-4cd2-8838-ff0427edbd71)
![2](https://github.com/kokiez/solana-sniper/assets/105941365/f54fb612-23de-4db1-85f2-39ded1ccc516)


## Contributors:
- Update CA pattern: [Moka51](https://github.com/Moka51)

## FAQS
### 1. How to install requirements?
Each OS is different from mine _(e.g. amount/types of garbage in my OS)_, I cannot assist you and guide you step by step on how to install requirements... In the current world, chatgpt exists, you may ask chatgpt such questions. Its simple run the command, if you get error then read it and try to understand what the error is saying or check the error on chatgpt.
### 2. Program did not show up anything and stopped!
Most likely your config.ini is missing, you have to put the right data in it e.g. Required sections are [TELEGRAM], [DISCORD], [WALLET] and [INFURA_URL]
### 3. What is senderUserNames in config.ini section TELEGRAM?
It is the username of channel where the tokens are pasted, the bot would like to know those usernames and then snipe the tokens.
