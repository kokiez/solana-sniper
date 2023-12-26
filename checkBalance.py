from solders.pubkey import Pubkey
from solana.rpc.types import TokenAccountOpts

"""
Check balance of the token in your wallet
"""
def checkB(TOKEN_TO_SWAP_SELL, payer, ctx):

    tokenPk = Pubkey.from_string(TOKEN_TO_SWAP_SELL)

    accountProgramId = ctx.get_account_info_json_parsed(tokenPk)
    programid = accountProgramId.value.owner

    accounts = ctx.get_token_accounts_by_owner_json_parsed(payer.pubkey()  ,TokenAccountOpts(program_id=programid)).value
    for account in accounts:
        tokenBalanceLamports = int(account.account.data.parsed['info']['tokenAmount']['amount'])
        mint = account.account.data.parsed['info']['mint']
        if tokenBalanceLamports > 0 and mint == TOKEN_TO_SWAP_SELL:
            return True
    return False