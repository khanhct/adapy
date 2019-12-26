# Adapy library
The library now supports create address, push and get transactions for both python 2.7 and 3.x
# Installation
## Linux
```sh
# create virtual environment
mkdir -p ~/envs/adaspy
virtualenv ~/envs/adapy
# activate the environment
source ~/envs/eospy/bin/activate
# install from github
# look [here](https://github.com/khanhct/adapy/releases) for the latest release.
pip install git+https://github.com/khanhct/adapy.git@<release>
# install the library from pip
pip install adapy
```
## Docker Container
```sh
docker-compose up
```

# API Endpoints
For a more complete list of API endpoints check out:
https://cardanodocs.com/technical/wallet/api/

# Example
## Create Address
```sh
from adapy.nodeada import NodeAda
from adapy.wallet import Wallet
import hashlib
no = NodeAda(url='https://localhost:8090/api', version='v1')
wl = Wallet(url='https://localhost:8090/api', version='v1')
print(no.create_address(2520553453, "46734b4a5a6454556c6137356c616171797573793549676864445a6741756c55","2cWKMJemoBakEUmdoCBWmG3b1ya6aa9hcmGF5UY6eqZbXcpzkcwNuEoXMrGvcRW1mDxjA"))
```
## Get transactions
```sh
from adapy.nodeada import NodeAda
from adapy.wallet import Wallet
import hashlib
no = NodeAda(url='https://localhost:8090/api', version='v1')
wl = Wallet(url='https://localhost:8090/api', version='v1')
params = {'wallet_id': '2cWKMJemoBakEUmdoCBWmG3b1ya6aa9hcmGF5UY6eqZbXcpzkcwNuEoXMrGvcRW1mDxjA', 'account_index': 2520553453, 'created_at': 'RANGE[2019-12-24T07:25:18.788036, 2019-12-24T07:25:18.788036]', 'page': 1, 'sort_by': 'DES', 'per_page': 20}
print(no.get_trxs(params))
```

## Push transaction
```sh
from adapy.nodeada import NodeAda
from adapy.wallet import Wallet
import hashlib
no = NodeAda(url='https://localhost:8090/api', version='v1')
wl = Wallet(url='https://localhost:8090/api', version='v1')
trx = {
    "destinations": [
        {
        "address": "37btjrVyb4KDhZhhAQ2yK2RoJ1k4fQAxoFZJ78sgPhsZiQWV2KwgDhqRsjhA2JsiKs6N74V98GPVwSGdjopFv22ksggjCc5xVyW3pGQ954okXPQ5Yj",
        "amount": 500 * 1000000
        }
    ],
    "groupingPolicy": "OptimizeForHighThroughput",
    "source": {
        "accountIndex":2520553453,
        "walletId": "2cWKMJemoBakEUmdoCBWmG3b1ya6aa9hcmGF5UY6eqZbXcpzkcwNuEoXMrGvcRW1mDxjA"
    },
    "spendingPassword": "46734b4a5a6454556c6137356c616171797573793549676864445a6741756c55"
}
try:
    result = no.send_trx(trx_data=trx)
    print(result)
except Exception as ex:
    print(ex)
```
