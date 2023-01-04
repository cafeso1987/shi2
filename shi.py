from web3 import Web3
import json
import time
import requests
telegram = "https://api.telegram.org/bot5446900133:AAETo4P_46myx2MAu8WO0-qc9zqxvV0Aj60/sendMessage?chat_id=-613559981&text="
abi = json.loads('[{ "inputs": [{ "internalType": "uint256", "name": "tokenId", "type": "uint256" }], "name": "nestingPeriod", "outputs": [{ "internalType": "bool", "name": "nesting", "type": "bool" }, { "internalType": "uint256", "name": "current", "type": "uint256" }, { "internalType": "uint256", "name": "total", "type": "uint256" }], "stateMutability": "view", "type": "function" }]')
address = "0x23581767a106ae21c074b2276D25e5C3e136a68b"
w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.alchemyapi.io/v2/rkVLtauY33cK6EfDWJlbl3Ii1UUE5qCH"))

mb = w3.eth.contract(address=address, abi=abi)

while True:
    try:
        mb_nesting_3465 = mb.functions.nestingPeriod(3465).call()
        time.sleep(10)
        mb_nesting_7899 = mb.functions.nestingPeriod(7899).call()

        secs_3465 = mb_nesting_3465[1]
        secs_7899 = mb_nesting_7899[1]
        date_3465 = f'{360 - secs_3465/3600/24} days until nesting ends'
        date_7899 = f'{360 - secs_7899/3600/24} days until nesting ends'
        
        requests.post(telegram+f'3465:\nnesting is {mb_nesting_3465[0]}\n{date_3465} \n\n 7899: \nnesting is {mb_nesting_7899[0]}\n{date_7899}')

        if mb_nesting_3465[0] == True:
            print('3465хрень')
        elif mb_nesting_3465[0] == False:
            while True:
                requests.post(telegram+'3465 @OneMillionDoIIars @profiabc')
                time.sleep(10)
        time.sleep(10)
        
        if mb_nesting_7899[0] == True:
            print('7899хрень')
        elif mb_nesting_7899[0] == False:
            while True:
                requests.post(telegram+'7899 @OneMillionDoIIars @profiabc')
                time.sleep(10)
        time.sleep(15)
    except Exception as e:
        print(e)
        continue
