# from Wallet_Info import get_wallet_Info
from webhook import sendWebhook

from alreadyBought import soldToken 

from raydium.sell_swap import sell
from birdeye import get_price, getSymbol
from monitor_price_strategy import limit_order, trailing_stop_loss_func, take_profit_and_trailing_stop

import time

def raydium_swap(config, ctx, payer, desired_token_address, txB, execution_time, limit_order_sell_Bool, take_profit_ratio, trailing_stop_Bool, trailing_stop_ratio, Limit_and_Trailing_Stop_Bool, bought_token_price):


    token_symbol, SOl_Symbol = getSymbol(desired_token_address)
    
    txB =  str(txB)   
    # saveTokenTime()
    
    sell_NOW = True
    if limit_order_sell_Bool:
        sell_NOW = limit_order(bought_token_price,desired_token_address, take_profit_ratio, execution_time, txB)
    elif trailing_stop_Bool:
        sell_NOW = trailing_stop_loss_func(bought_token_price,desired_token_address, trailing_stop_ratio, execution_time, txB)

    elif Limit_and_Trailing_Stop_Bool:
        sell_NOW = take_profit_and_trailing_stop(bought_token_price,desired_token_address, trailing_stop_ratio, take_profit_ratio, execution_time, txB)

    # Call Sell Method - returns transaction hash (txS= tx for sell)
    if sell_NOW == False:
        bought_token_curr_price = get_price(desired_token_address)
        start_time = time.time()
        txS = sell(ctx, desired_token_address, payer)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Total Sell Execution time: {execution_time} seconds")

        if str(txS) != 'failed':
            txS =  str(txS)   

            print("-" * 79)
            print(f"| {'Sold Price':<15} | {'Tx Sell':<40} |")
            print("-" * 79)
            print(f"| {bought_token_curr_price:.12f} | {txS:<40} |")

            sendWebhook(f"msg_s|SELL INFO [Raydium] - {token_symbol}",f"Token Address: {desired_token_address}\nSold at: {bought_token_curr_price:.12f}\nTotal Sell Execution time: {execution_time} seconds\nSell TXN: https://solscan.io/tx/{txS}\n------------------- END -------------------")

            print("-" * 79)

            soldToken(desired_token_address)