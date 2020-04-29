import json
from flask import Flask, render_template
import web3
from solcx import compile_source
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
NUM_OF_CANDIDATES = 2

from web3 import Web3
GANACHE_URL = "http://127.0.0.1:8545/"
w3 = Web3(Web3.HTTPProvider(GANACHE_URL))

contract_source_code = None
contract_source_code_file = os.path.join(THIS_FOLDER,'contracts/Election.sol')
with open(contract_source_code_file, 'r') as file:
    contract_source_code = file.read()

contract_compiled = compile_source(contract_source_code)
contract_interface = contract_compiled['<stdin>:Election']
Election = w3.eth.contract(abi=contract_interface['abi'], 
                          bytecode=contract_interface['bin'])

w3.eth.defaultAccount = w3.eth.accounts[0]
candidateNames = ["Ca"]
   

tx_hash = Election.constructor().transact({'from':w3.eth.accounts[0]})
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# Contract Object
election = w3.eth.contract(address=tx_receipt.contractAddress, abi=contract_interface['abi'])



# Web service initialization

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello():
    print("Default acc: "+ w3.eth.defaultAccount)
    return render_template('vote_menu.html', candidateNames=candidateNames, contractAddress = lottery.address.lower(), contractABI = json.dumps(contract_interface['abi']))

if __name__ == '__main__':
    app.run()
