from adapy.nodeada import NodeAda
from adapy.wallet import Wallet
import hashlib
'''
{'data': {'id': '2cWKMJemoBakEUmdoCBWmG3b1ya6aa9hcmGF5UY6eqZbXcpzkcwNuEoXMrGvcRW1mDxjA', 'name': 'sencoinedev1', 'balance': 0, 'hasSpendingPassword': True, 'spendingPasswordLastUpdate': '2019-12-23T07:19:17.044258', 'createdAt': '2019-12-23T07:19:17.044258', 'assuranceLevel': 'normal', 'syncState': {'tag': 'synced', 'data': None}}, 'status': 'success', 'meta': {'pagination': {'totalPages': 1, 'page': 1, 'perPage': 1, 'totalEntries': 1}}}
37btjrVyb4KFgB83igJEUcGyMj4A6qxtD4nseCRHXsXaz5T8BVPABbTYwNkQtn1HgCTkk97TMJ1ajV6hwQEpQ3Ggu4y2YM4YwjommwgureFUM1BGND
37btjrVyb4KDZLvnWygx7dg8uYeWkPMMHeehp269LtnPd9qg66kGysTUBrfRDPGRMv8VW8EGamL2Xi7bGYgnybauEvibSg7eCJCqMTtpEv2gSxvaDS
'''

no = NodeAda(url='https://localhost:8090/api', version='v1')
wl = Wallet(url='https://localhost:8090/api', version='v1')

spending_password = '46734b4a5a6454556c6137356c616171797573793549676864445a6741756c55'
params = {'wallet_id': '2cWKMJemoBakEUmdoCBWmG3b1ya6aa9hcmGF5UY6eqZbXcpzkcwNuEoXMrGvcRW1mDxjA', 'account_index': 2520553453, 'created_at': 'RANGE[2019-12-24T07:25:18.788036, 2019-12-24T07:25:18.788036]', 'page': 1, 'sort_by': 'DES', 'per_page': 20}
#print(no.get_trxs(params))
#print(no.create_address(2520553453, "46734b4a5a6454556c6137356c616171797573793549676864445a6741756c55","2cWKMJemoBakEUmdoCBWmG3b1ya6aa9hcmGF5UY6eqZbXcpzkcwNuEoXMrGvcRW1mDxjA"))
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
#trx ={'destinations': [{'address': '37btjrVyb4KFvN8yuz3ELJedPx76J85sZfNwPCELiddUyGFdchSr7kkzAo7xakBbjMp8r3CG3E7a6jEcnie6JHGjNwhZ8zdvYAzrqRyMMpgsxWCgww', 'amount': '10000000'}], 'groupingPolicy': 'OptimizeForHighThroughput', 'source': {'accountIndex': 2520553453, 'walletId': '2cWKMJemoBakEUmdoCBWmG3b1ya6aa9hcmGF5UY6eqZbXcpzkcwNuEoXMrGvcRW1mDxjA'}, 'spendingPassword': '46734b4a5a6454556c6137356c616171797573793549676864445a6741756c55'}
# print(no.get_wallet(wallet_id='2cWKMJemoBakEUmdoCBWmG3b1ya6aa9hcmGF5UY6eqZbXcpzkcwNuEoXMrGvcRW1mDxjA'))
# print(no.get_balance(account_id=2520553453, wallet_id='2cWKMJemoBakEUmdoCBWmG3b1ya6aa9hcmGF5UY6eqZbXcpzkcwNuEoXMrGvcRW1mDxjA'))
try:
    result = no.send_trx(trx_data=trx)
    print(result)
except Exception as ex:
    print(ex)