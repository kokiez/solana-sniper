import os, sys
from webhook import sendWebhook
from birdeye import getSymbol
import json

def write_token_to_file(token_address):
    file_path = os.path.join(sys.path[0], 'data', 'alreadyBoughtTokens.json')

    # Load the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Check if the 'tokens' key exists in the JSON object
    if 'tokens' in data:
        # If it exists, append the new tokens to the existing list
        data['tokens'].extend([token_address])
    else:
        # If it doesn't exist, create a new list with the new tokens
        data['tokens'] = [token_address]

    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Token address [{token_address}] saved in 'alreadyBoughtTokens.json'.")

# def check_if_already_bought(token_address):
def check_token_existence(token_to_check):
    token_symbol, SOl_Symbol = getSymbol(token_to_check)

    file_path = os.path.join(sys.path[0], 'data', 'alreadyBoughtTokens.json')

    # Open the JSON file in read mode ('r')
    with open(file_path, 'r') as file:
        # Load the JSON data into a dictionary
        token_data = json.load(file)

    # Check if the token exists in the JSON data
    if token_to_check in token_data['tokens']:
        print(f"[{token_to_check}] already exists in 'alreadyBoughtTokens.json'.")
        sendWebhook(f"a|Token SAVE {token_symbol}", f"[{token_to_check}] already exists in 'alreadyBoughtTokens.json'.")
        return True
    return False


def storeSettings(amm,
                  desired_token_address,
                  txB,
                  execution_time,
                  limit_order_sell_Bool,
                  take_profit_ratio,
                  trailing_stop_Bool,
                  trailing_stop_ratio,
                  Limit_and_Trailing_Stop_Bool,
                  bought_token_price):
    
    token_symbol, SOl_Symbol = getSymbol(desired_token_address)

    file_path = os.path.join(sys.path[0], 'data', 'previousSELLBUYINFO.json')

    # Define the settings
    settings = {
         'amm': amm,
            'txB': str(txB),
            'execution_time': execution_time,
            'limit_order_sell_Bool': limit_order_sell_Bool,
            'take_profit_ratio': take_profit_ratio,
            'trailing_stop_Bool': trailing_stop_Bool,
            'trailing_stop_ratio': trailing_stop_ratio,
            'Limit_and_Trailing_Stop_Bool': Limit_and_Trailing_Stop_Bool,
            'bought_token_price': bought_token_price
    }

    # Load the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Append the settings to the JSON object
    data[desired_token_address] = settings

    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print("Settings saved in 'previousSELLBUYINFO.json'.")
    sendWebhook(f"a|Token INFO SAVE {token_symbol}", f"Settings saved in 'previousSELLBUYINFO.json'.")


def soldToken(desired_token_address):
    print("Deleting saved token from previousSELLBUYINFO...")
    file_path = os.path.join(sys.path[0], 'data', 'previousSELLBUYINFO.json')
    # Load the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Check if the 'desired_token_address' key exists in the JSON object
    if desired_token_address in data:
        # If it exists, delete it
        del data[desired_token_address]

    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print("Deleting saved token from alreadyBoughtTokens...")
    file_path = os.path.join(sys.path[0], 'data', 'alreadyBoughtTokens.json')
    # Load the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Check if the 'tokens' key exists in the JSON object
    if 'tokens' in data:
        # If it exists, check if the token is in the list
        if desired_token_address in data['tokens']:
            # If it is, remove it
            data['tokens'].remove(desired_token_address)

    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)



def getSettings(token):
    file_path = os.path.join(sys.path[0], 'data', 'previousSELLBUYINFO.json')
    
    # Load the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Retrieve the settings for the desired_token_address
    settings = data.get(token)

    if settings is not None:
        print(f"Settings Retrieved for {token}")
        return settings

    else:
        return None

