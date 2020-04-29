## Smart Contract Vulnerabilities

Read and understand the following smart contracts. Find, exploit, and fix
their vulnerabilities.

**Note:** The smart contracts must be compiled using solidity v0.4.10.

RESPONSES BY AINUL MARDHIYYAH 1003115

### Question 1

```
pragma solidity ^0.4.10;

contract Auction {

    address winner;
    uint lastBid;

    function Auction() public {
        winner = msg.sender;
        lastBid = 0;
    }

    function bid() public payable {
        assert(msg.value > lastBid);
        if (lastBid > 0) {
            assert(winner.call.value(lastBid)());
        }
        winner = msg.sender;
        lastBid = msg.value;
    }

    function getWinner() public returns(address) {
        return winner;
    }

}
```

==RESPONSE==

The vulnerability in Question 1 is due to the "assert..." line in the code within the if-block. An attacker can cause a Denial-of-Service attack by rejecting then reverting the refund of the lastBid value. As a result, the attacker can remain as the winner simply by rejecting the refund called in the if-block.

This vulnerability can be fixed by implementing a pull payment system in which refunds are recorded for later withdrawal (pull) by the users-to-be-refunded, rather than have the refunds automatically be pushed to them.

### Question 2

```
pragma solidity ^0.4.10;

contract Bank {

    mapping(address => uint) balances;

    function deposit() public payable {
        balances[msg.sender] = balances[msg.sender] + msg.value;
    }

    function withdrawAll() public {
        uint amount = balances[msg.sender];
        assert(msg.sender.call.value(amount)());
        balances[msg.sender] = 0;
    }

    function getBalance(address _address) public returns(uint) {
        return(balances[_address]);
    }

}
```

==RESPONSE==

The vulnerability lies in the withdrawAll function where the external assert call is done before the balance of the sender is set to zero i.e. the setting of balance to zero is only done at the very end. Therefore, an attacker can exploit this by calling the withdrawAll function multiple times.

A simple fix would be to move the assert code in withdrawAll after setting balances[msg.sender] to zero, so that internal changes can be done prior to external calls.
