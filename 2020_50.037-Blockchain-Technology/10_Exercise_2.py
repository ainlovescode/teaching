from web3 import Web3
from web3.auto import w3
from solcx import compile_source


### QUESTION 2 ###

contract_source_code = None
contract_source_code_file = 'Fib.sol'

with open(contract_source_code_file, 'r') as file:
    contract_source_code = file.read()

# Compile the contract
contract_compiled = compile_source(contract_source_code)
contract_interface = contract_compiled['<stdin>:Fib']


ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Set the default account
w3.eth.defaultAccount = w3.eth.accounts[0]

# Contract abstraction
Fib = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# Create an instance, i.e., deploy on the blockchain
tx_hash = Fib.constructor().transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# Contract Object
fib = w3.eth.contract(address=tx_receipt.contractAddress, abi=contract_interface['abi'])

print('Calling contracts functions')
print('Contract address: ', fib.address)
print('obj.getOwner(): ', fib.functions.getOwner().call())

fiboAHash = fib.functions.fibonacciA(10).transact({"from":w3.eth.accounts[0],"value": web3.toWei(1,'ether')})
fiboAReceipt = w3.eth.waitForTransactionReceipt(fiboAHash)
print("fibonacciA gas cost: {}".format(fiboAReceipt.gasUsed))

fiboBHash = fib.functions.fibonacciB(10).transact()
fiboBReceipt = w3.eth.waitForTransactionReceipt(fiboBHash)
print("fibonacciB gas cost: {}".format(fiboBReceipt.gasUsed))
print(fiboBReceipt)

fiboBetterHash = fib.functions.fibonacciBetter(10).transact()
fiboBetterReceipt = w3.eth.waitForTransactionReceipt(fiboBetterHash)
print("fibonacciBetter gas cost: {}".format(fiboBetterReceipt.gasUsed))



