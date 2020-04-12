## Ethereum DApp - Back-end

### Question 1

Using Ganache [1] and Web3py [2] do the following:

* connect Web3py to Ganache
* make transactions between Ganache accounts
* get information (`number`, `gasLimit`, `gasUsed`, ...) of the latest block
* get and print a receipt of a conducted transaction

### RESPONSE TO QUESTION 1
After running ganache-cli in Command Prompt, I connect Web3 to Ganache in my Python script and choose two account addresses to be account_A and account b, I create a transaction with account_A sending some Ether to account_B.

Sending this transaction will return the transaction hash similar to the one below:
    <pre>0x5435440cf7083d117a6ba1f839c239633e0d983773465afba383437ddc2dca05</pre>

I can then get the information of the latest block, as shown below:
<pre>
AttributeDict({'number': 1, 'hash': HexBytes('0x3057f9f51828c928bdf77813bb58c06081212edbb1c3850ca5bcd73152225cdb'),
.
.
.,
'gasLimit': 6721975, 'gasUsed': 21000, 'timestamp': 1586704045, 'transactions': [HexBytes('0x5435440cf7083d117a6ba1f839c239633e0d983773465afba383437ddc2dca05')], 'uncles': []}) </pre>

With the earlier transaction hash, I can also output the transaction receipt:
<pre>AttributeDict({'transactionHash': HexBytes('0x5435440cf7083d117a6ba1f839c239633e0d983773465afba383437ddc2dca05'), 'transactionIndex': 0, 'blockHash': HexBytes('0x3057f9f51828c928bdf77813bb58c06081212edbb1c3850ca5bcd73152225cdb'), 'blockNumber': 1, 'from': '0xb7E3ce48db46bb49E9140C607FC004170B53541F', 'to': '0x80385Ac99d7d9811eF407B97f92AFdab72B14988', 'gasUsed': 21000, 'cumulativeGasUsed': 21000, 'contractAddress': None, 'logs': [], 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')})
</pre>

### Question 2

Using Ganache, Web3py, and a Solidity compiler [3, 4], compile and deploy the
smart contract below, and:

* execute available functions (notice the different between the `call()` and
  `transact()` methods)
* which Fibonacci function is more efficient? (in terms of gas cost)
* would `fibonacciA` be cheaper if it is non-payable?
* optimize `fibonacciB`

### RESPONSE TO QUESTION 2
I frst run ganache-cli in Command Prompt.

After initialising the required objects and compiling and deploying the Solidity contract, I <b>transact</b> to create the Contract instance.

I can then <b>call</b> the simple getter function getOwner, and <b>transact</b> my fibonacci functions. Below are snippets of the output:
<pre>Contract address:  0x75A5b6f13A5873Adfcb2049548354ccEC90ACC81
obj.getOwner():  0xb7E3ce48db46bb49E9140C607FC004170B53541F
fibonacciA gas cost: 44960
fibonacciB gas cost: 133759</pre>

<b>fibonacciA is more efficient as it has a lower gas cost than fibonacciB.</b>

<b>fibonacciA would be cheaper if it becomes non-payable.</b>

<b>fibonacciB can be optimised by using memoisation.</b>
Here is a code snippet of the optimised fibonacciB, called fibonacciBetter:

<pre>function fibonacciBetter(uint n) public returns(uint) {

    uint[] memory memo = new uint[](n+1);
    for (uint i = 0; i <= n; i++) {
        if (i <= 1) {
            memo[i] = i;
        } else {
            memo[i] = memo[i -1] + memo[i -2];    
        }
    }
    return memo[n];

}
    </pre>

<hr/>
### Given data for Q2

```js
pragma solidity ^0.4.25;

contract Fib {

    uint constant FEE = 1 ether;

    address private owner;
    uint private previousFirst;
    uint private previousSecond;
    uint private next;

    constructor() public {
        owner = msg.sender;
    }

    function getOwner() public view returns(address) {
        return(owner);
    }

    function fibonacciA(uint n) public payable returns(uint) {
        require(msg.value == FEE, "You must pay to execute this");
        if(n == 0){return(0);}
        if(n == 1){return(1);}
        else{return(fibonacciA(n - 1) + fibonacciA(n - 2));}
    }

    function fibonacciB(uint n) public returns(uint) {
        previousFirst = 0;
        previousSecond = 1;
        next = 1;
        for(uint i = 2; i <= n; i++) {
            next = previousFirst + previousSecond;
            previousFirst = previousSecond;
            previousSecond = next;
        }
        return(next);
    }

    function fibonacciBetter(uint n, varmemo) public returns(uint) {
        previousFirst = 0;
        previousSecond = 1;
        next = 1;
        for(uint i = 2; i <= n; i++) {
            next = previousFirst + previousSecond;
            previousFirst = previousSecond;
            previousSecond = next;
        }
        return(next);
    }

}
```


[1] https://truffleframework.com/ganache <br />
[2] https://web3py.readthedocs.io/en/stable <br />
[3] https://solidity.readthedocs.io/en/v0.4.25/installing-solidity.html#solcjs <br />
[4] https://github.com/ethereum/py-solc <br />


### Cheatsheet: Minimum working example of contract deployment

Preliminaries:
```console
(install Ganache)
$ pip3 install py-solc web3
$ python3 -m solc.install v0.4.25
$ export PATH=$HOME/.py-solc/solc-v0.4.25/bin:$PATH
```

Example smart contract:
```js
pragma solidity ^0.4.25;

contract Example {

    address private owner;

    constructor() public {
        owner = msg.sender;
    }

    function getOwner() public view returns(address) {
        return(owner);
    }

}
```

Code to deploy and use it:
```python
'''
Once Ganache is installed, run its GUI or execute the following command:
$ ganache-cli -p 8545 -h 0.0.0.0 -n
'''

from solc import compile_source
from web3.auto import w3

contract_source_code = None
contract_source_code_file = 'example.sol'

with open(contract_source_code_file, 'r') as file:
    contract_source_code = file.read()

# Compile the contract
contract_compiled = compile_source(contract_source_code)
contract_interface = contract_compiled['<stdin>:Example']

# Set the default account
w3.eth.defaultAccount = w3.eth.accounts[0]

# Contract abstraction
Example = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# Create an instance, i.e., deploy on the blockchain
tx_hash = Example.constructor().transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# Contract Object
example = w3.eth.contract(address=tx_receipt.contractAddress, abi=contract_interface['abi'])

print('Calling contract functions')
print('Contract address: ', example.address)
print('obj.getOwner(): ', example.functions.getOwner().call())
```
