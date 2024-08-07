from web3 import Web3

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Your account (receiver) address
RECEIVER_ADDRESS = '0x299d1F01F80455E798a6Fe61334E2eE522C63363' 


def get_transaction_data(from_address, to_address, amount):
    nonce = w3.eth.get_transaction_count(from_address)
    tx = {
        'from': from_address,  # Include the from address
        'nonce': nonce,
        'to': to_address,
        'value': w3.to_wei(amount, 'ether'),
        'gas': 2000000,
        'gasPrice': w3.eth.gas_price
    }
    return tx

