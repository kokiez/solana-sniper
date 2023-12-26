
import time
from birdeye import get_price, getSymbol
from webhook import sendWebhook


"""If you have ton of trades then best to use Simulate Transaction and modify this part of code to your needs"""


"""
Only Take Profit
"""
def limit_order(bought_token_price,desired_token_address, take_profit_ratio, execution_time, txB):
    token_symbol, SOl_Symbol = getSymbol(desired_token_address)
    # CALCULATE SELL LIMIT
    sell_limit_token_price = bought_token_price  *  take_profit_ratio
    
    print("-" * 79)
    print(f"| {'Bought Price':<12} | {'Sell Limit':<12} |  {'Tx Buy':<50} |")
    print("-" * 79)
    print(f"|{bought_token_price:.12f} | {sell_limit_token_price:.12f}  {txB:<50} |")
    print("-" * 79)

    sendWebhook(f"msg_b|BUY INFO {token_symbol}",f"Bought Price: {bought_token_price:.12f}\n**Sell Limit: {sell_limit_token_price:.15f}**\nTotal Buy Execution time: {execution_time} seconds\nBuy TXN: https://solscan.io/tx/{txB} |")

    # LOOP = CHECK IF PRICE >= SELL LIMIT |  checks price every 5 seconds
    priceLow = True
    # while priceLow and isTimePassed(time_limit) == False:
    while priceLow:
        # Check if time limit has been passed for the token bought or not
        bought_token_curr_price = get_price(desired_token_address)
        if bought_token_curr_price  >= sell_limit_token_price:
            print(f"Price limit reached: {bought_token_curr_price}")
            priceLow = False # break the loop
        else:
            time.sleep(15)

    return priceLow


"""
Only Trailing Stop loss
"""
def trailing_stop_loss_func(bought_token_price,desired_token_address, trailing_stop_ratio, execution_time, txB):
    token_symbol, SOl_Symbol = getSymbol(desired_token_address)


    # Set initial trailing stop loss limit
    trailing_ratio_of_Price = (trailing_stop_ratio / 100) * bought_token_price
    initial_trailing_stop_loss_token_price = bought_token_price - trailing_ratio_of_Price
    
    print("-" * 79)
    print(f"| {'Bought Price':<12} | {'Initial Trailing Stop Loss Limit':<12} |  {'Tx Buy':<50} |")
    print("-" * 79)
    print(f"|{bought_token_price:.12f} | {initial_trailing_stop_loss_token_price:.12f} | {txB:<50} |")
    print("-" * 79)

    sendWebhook(f"msg_b|BUY [TRAILING] INFO {token_symbol}",f"Bought Price: {bought_token_price:.12f}\n**Initial Trailing Stop Loss Limit: {initial_trailing_stop_loss_token_price:.15f}**\nTotal Buy Execution time: {execution_time} seconds\nBuy TXN: https://solscan.io/tx/{txB} |")

    # LOOP = CHECK IF PRICE >= SELL LIMIT |  checks price every 5 seconds
    priceLow = True
    # while priceLow and isTimePassed(time_limit) == False:
    time.sleep(5)
    print(f"+|+ {'Trailing Stop Loss [Update]':<12} +|+")
    print("-" * 50)
    startingPrice=bought_token_price

    trailing_ratio_of_Price = (trailing_stop_ratio / 100) * startingPrice
    latest_sell_stop_loss_token_price = startingPrice - trailing_ratio_of_Price 
    while priceLow:

        bought_token_curr_price = get_price(desired_token_address)

        # if time limit has been passed for the token bought or not
        if bought_token_curr_price  <= latest_sell_stop_loss_token_price:
            print(f"Trailing Price limit reached: {bought_token_curr_price:.12f}")
            priceLow = False # break the loop
        elif bought_token_curr_price > startingPrice:
            
            trailing_ratio_of_Price = (trailing_stop_ratio / 100) * bought_token_curr_price
            latest_sell_stop_loss_token_price = bought_token_curr_price - trailing_ratio_of_Price 

            startingPrice = bought_token_curr_price
        else:
            time.sleep(15)
            print(f"=|= {'Bought Price':<12} =|= {'Latest Trailing Stop Loss Limit':<12} =|=")
            print("-" * 79)
            print(f"=|={bought_token_price:.12f} =|= {latest_sell_stop_loss_token_price:.12f} =|=")
            print("-" * 50)

    print("-" * 79)
    print(f"| {'Bought Price':<12} | {'Latest Trailing Stop Loss Limit':<12} |  {'Tx Buy':<50} |")
    print("-" * 79)
    print(f"|{bought_token_price:.12f} | {latest_sell_stop_loss_token_price:.12f} | {txB:<50} |")
    print("-" * 79)

    sendWebhook(f"a|BUY [TRAILING] INFO {token_symbol}",f"Bought Price: {bought_token_price:.12f}\n**Latest Trailing Stop Loss Limit: {latest_sell_stop_loss_token_price:.15f}**\nTotal Buy Execution time: {execution_time} seconds\nBuy TXN: https://solscan.io/tx/{txB} |")

    return priceLow

"""
Trailing Stop + Take Profit
"""
def take_profit_and_trailing_stop(bought_token_price,desired_token_address, trailing_stop_ratio, take_profit_ratio, execution_time, txB):
    token_symbol, SOl_Symbol = getSymbol(desired_token_address)
    
    # CALCULATE SELL LIMIT
    sell_limit_token_price = bought_token_price  *  take_profit_ratio

    # Set initial trailing stop loss limit
    trailing_ratio_of_Price = (trailing_stop_ratio / 100) * bought_token_price
    initial_trailing_stop_loss_token_price = bought_token_price - trailing_ratio_of_Price
    
    print("-" * 79)
    print(f"| {'Bought Price':<12} | {'Sell Limit Price':<12} | {'Initial Trailing Stop Loss Limit':<12} |  {'Tx Buy':<50} |")
    print("-" * 79)
    print(f"|{bought_token_price:.12f} | {sell_limit_token_price:.12f} | {initial_trailing_stop_loss_token_price:.12f} | {txB:<50} |")
    print("-" * 79)

    sendWebhook(f"msg_b|BUY [TRAILING+Limit] INFO {token_symbol}",f"Bought Price: {bought_token_price:.12f}\n\n**Sell Take Profit Limit: {sell_limit_token_price:.15f}**\n**Initial Trailing Stop Loss Limit: {initial_trailing_stop_loss_token_price:.15f}**\n\nTotal Buy Execution time: {execution_time} seconds\nBuy TXN: https://solscan.io/tx/{txB} |")

    # LOOP = CHECK IF PRICE >= SELL LIMIT |  checks price every 5 seconds
    priceLow = True
    # while priceLow and isTimePassed(time_limit) == False:
    time.sleep(5)
    print(f"+|+ {'TRAILING+Limit [Update]':<12} +|+")
    print("-" * 50)
    startingPrice=bought_token_price

    trailing_ratio_of_Price = (trailing_stop_ratio / 100) * startingPrice
    latest_sell_stop_loss_token_price = startingPrice - trailing_ratio_of_Price
    Up = 0 
    while priceLow:

        bought_token_curr_price = get_price(desired_token_address)

        # if time limit has been passed for the token bought or not
        if bought_token_curr_price  >= sell_limit_token_price:
            print(f"Sell limit reached: {bought_token_curr_price:.12f}")
            priceLow = False # break the loop
        elif bought_token_curr_price  <= latest_sell_stop_loss_token_price:
            print(f"Trailing Price limit reached: {bought_token_curr_price:.12f}")
            priceLow = False # break the loop
        elif bought_token_curr_price > startingPrice:
            
            trailing_ratio_of_Price = (trailing_stop_ratio / 100) * bought_token_curr_price
            latest_sell_stop_loss_token_price = bought_token_curr_price - trailing_ratio_of_Price 

            startingPrice = bought_token_curr_price
            
        if priceLow != False:
            print(f"=|= {'Bought Price':<12} =|=  {'Current Price':<12} =|= {'Sell Limit Price':<12} =|= {'Latest Trailing Stop Loss Limit':<12} =|======== {Up}")
            print("-" * 79)
            print(f"=|={bought_token_price:.12f} =|= {bought_token_curr_price:.12f} =|= {sell_limit_token_price:.12f} =|= {latest_sell_stop_loss_token_price:.12f} =|=")
            print("-" * 50)
            time.sleep(15)
            Up = Up + 1


    print("-" * 79)
    print(f"| {'Bought Price':<12} | {'Sell Limit Price':<12} | {'Latest Trailing Stop Loss Limit':<12} |  {'Tx Buy':<50} |")
    print("-" * 79)
    print(f"|{bought_token_price:.12f} | {sell_limit_token_price:.12f} | {latest_sell_stop_loss_token_price:.12f} | {txB:<50} |")
    print("-" * 79)

    sendWebhook(f"a|BUY [TRAILING+Limit] INFO {token_symbol}",f"Bought Price: {bought_token_price:.12f}\n**Sell Limit Price: {sell_limit_token_price:.15f}**\n**Latest Trailing Stop Loss Limit: {latest_sell_stop_loss_token_price:.15f}**\nTotal Buy Execution time: {execution_time} seconds\nBuy TXN: https://solscan.io/tx/{txB} |")


    return priceLow