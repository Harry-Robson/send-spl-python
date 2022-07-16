# send-spl-python
Send Solana SPL tokens by pushing commands the command line and interacting with spl-token and the Solana Tool Suite.

## Prerequisites 
* [Solana Tool Suite](https://docs.solana.com/cli/install-solana-cli-tools)
* [spl-token command line utility](prerequisite)
* [Python 3.10 or higher](https://www.python.org/download/releases/3.1/)

## Getting Started
### Create and set keypair
* Open the command prompt and generate a new keypair. To do this, type ```solana-keygen new --outfile <path>```
* Set your default keypair in the Solana Tool Suite by typing ```solana config set -k <path of keyfile we just created>```

### Fund your wallet
* Either by importing your keypair into Phantom wallet or by using the ```solana address``` command you will be able to see your address. Fund this address on the devnet by using ```solana airdrop 1 <address>``` or on mainnet by sending Solana from an exchange.
* Confirm that you are funded by using command ```solana balance```

### Create an SPL token
For more detailled token creation instructions refer to the spl-token docs. This method creates a default token with an unfixed supply of 100 as well as an account to hold them.

* ```spl-token create-token``` will create a token and print token address
* ```spl-token create-account <token address>``` will create an account for said token
* ```spl-token mint <token address> 100``` mint 100 of said token to default wallet

### Declare function variables in send_spl.py
* ```token_address``` is the address of the token (including NFTs) that you would like to send
* ```recipient_address``` is the address of the recipient
* ```amount``` is the number of tokens you will send

*I'll be adding more options soon...*

### Call the send_spl() function
```send_spl(token_address, recipient_address, amount)```

The function will either print ```ERROR``` or ```SUCCESS``` depending on the subprocess exitcode. If there is an error the returncode will be provided.