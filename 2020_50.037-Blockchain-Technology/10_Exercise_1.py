from web3 import Web3

### QUESTION 1 ###

# initialise ganache-cli
ganache_url = "http://127.0.0.1:8545"

account_A = "0xb7E3ce48db46bb49E9140C607FC004170B53541F"
account_B = "0x80385Ac99d7d9811eF407B97f92AFdab72B14988"

private_key_A = "0xc75a9d122d28f100248f4dd638c83118a91fcb60cb9d215f4484bd940b1c89a3"


# connect Web3py to Ganache
web3 = Web3(Web3.HTTPProvider(ganache_url))

# make transactions between Ganache accounts
nonce = web3.eth.getTransactionCount(account_A)

tx = {
    'nonce': nonce,
    'to': account_B,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}

signed_tx = web3.eth.account.signTransaction(tx, private_key_A)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))

# get information (number, gasLimit, gasUsed, ...) of the latest block
block_info = web3.eth.getBlock('latest')
print("For the latest block mined:".format("2000000"))
print(block_info)

# get and print a receipt of a conducted transaction
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

print("================Transaction Receipt==============")
print(tx_receipt)