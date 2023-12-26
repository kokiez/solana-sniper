import base64, json, requests, time, os, sys
from solders.transaction import VersionedTransaction
from solders.message import to_bytes_versioned
from solders.signature import Signature

from solana.rpc.api import RPCException

from webhook import sendWebhook
from checkBalance import checkB
from birdeye import getSymbol


LAMPORTS_PER_SOL = 1000000000
def buy(payer, ctx, amount_of_sol_to_swap, TOKEN_TO_SWAP_BUY, config):
    token_symbol, SOl_Symbol = getSymbol(TOKEN_TO_SWAP_BUY)

    slippageBps = int(config.get("INVESTMENT", "slippage"))
    computeUnitPriceMicroLamports = int(config.get("INVESTMENT", "computeUnitPriceMicroLamports"))
    RPC_HTTPS_URL = config.get("INFURA_URL", "infuraURL")


    txnBool = True
    while txnBool:
        Attempt = True
        while Attempt:
            # Swap Info
            print("3. Get Route for swap...")

            quote_response = requests.get('https://quote-api.jup.ag/v6/quote', params={
                'inputMint': 'So11111111111111111111111111111111111111112',
                'outputMint': TOKEN_TO_SWAP_BUY,
                'amount': amount_of_sol_to_swap,
                'slippageBps': slippageBps
            }).json()

            try:
                if quote_response["error"]:
                    print("Quote Response [ERROR] - NOT ENOUGH LIQUIDITY: ",quote_response["error"])
                    temp = str(quote_response["error"])
                    sendWebhook(f"e|BUY ERROR {token_symbol} - NOT ENOUGH LIQUIDITY: ",f"{temp}")
                    return "failed"
            except:
                a = 1
                
# ========================================================================================================
            print("4. Get the serialized transactions to perform the swap...")
            # Get the serialized transactions to perform the swap
            url = "https://quote-api.jup.ag/v6/swap"
            payload = json.dumps({
            "userPublicKey": str(payer.pubkey()),
            "wrapAndUnwrapSol": True,
            'computeUnitPriceMicroLamports': computeUnitPriceMicroLamports,
            "quoteResponse": quote_response
            })
            headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            if (response.status_code == 200):
                instructions_all = (response).json()
                Attempt = False
            else:
                print("Retying...")
        swap_instruction = instructions_all["swapTransaction"]
        raw_tx = VersionedTransaction.from_bytes(base64.b64decode(swap_instruction))
# ========================================================================================================
        print("5. Sign Transaction...")
        signature = payer.sign_message(to_bytes_versioned(raw_tx.message))
        signed_tx = VersionedTransaction.populate(raw_tx.message, [signature])
# ========================================================================================================
        try:
            print("6. Execute Transaction...")
            start_time = time.time()
            txid = (ctx.send_transaction(
                signed_tx
            ))

            print(f"Transaction ID: {txid.value}")
            print(f"Transaction URL: https://solscan.io/tx/{txid.value}")

            txid_string_sig = Signature.from_string(str(txid.value))
            checkTxn = True
            while checkTxn:
                try:
                    status = ctx.get_transaction(txid_string_sig,"jsonParsed", max_supported_transaction_version=0)
                    FeesUsed = (status.value.transaction.meta.fee) / LAMPORTS_PER_SOL
                    if status.value.transaction.meta.err == None:
                        print("Transaction Success")
                        print("Transaction Fees: {:.10f} SOL".format(FeesUsed))

                        end_time = time.time()
                        execution_time = end_time - start_time
                        print(f"Execution time: {execution_time} seconds")

                        checkTxn = False
                        txnBool = False
                        
                        return txid_string_sig
                    else:
                        print("Transaction Failed: ", status.value.transaction.meta.err)

                        end_time = time.time()
                        execution_time = end_time - start_time
                        print(f"Execution time: {execution_time} seconds")

                        checkTxn = False

                except Exception as e:
                    sendWebhook(f"e|BUY ERROR {token_symbol}",f"{e}")
                    time.sleep(2)
                    print("Sleeping...")
            
        
        except RPCException as e:
            print(f"Error: [{e.args[0].message}]...\nRetrying...")
            sendWebhook(f"e|BUY ERROR {token_symbol}",f"{e.args[0].message}")
            time.sleep(1)
            # txnBool = False
            # return "failed"
        except Exception as e:
            print(f"Error: [{e}]...\nEnd...")
            sendWebhook(f"e|BUY Exception ERROR {token_symbol}",f"{e}")
            txnBool = False
            return "failed"