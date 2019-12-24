from .http import BaseHttpReq

class Wallet(BaseHttpReq):

    def __init__(self, url, version):
        super().__init__(url=url, version=version)

    def create_wallet(self, assurance_level='normal', backup_phrase=None, name=None, operation='create', spending_password=None):
        """
        Request:
        {
            "assuranceLevel": "strict",
            "backupPhrase": [
                "squirrel",
                "material",
                "silly",
                "twice",
                "direct",
                "slush",
                "pistol",
                "razor",
                "become",
                "junk",
                "kingdom",
                "flee"
            ],
            "name": "My Wallet",
            "operation": "restore",
            "spendingPassword": "0202010002000102020002010202010002020100000102020201020000020102"
        }
        """
        if backup_phrase is None:
            backup_phrase = [
                "squirrel",
                "material",
                "silly",
                "twice",
                "direct",
                "slush",
                "pistol",
                "razor",
                "become",
                "junk",
                "kingdom",
                "flee"
            ]
            
        json_data = {
            "assuranceLevel": assurance_level,
            "backupPhrase": backup_phrase,
            "name": name,
            "operation": operation,
            "spendingPassword": spending_password
        }
        print(json_data)
        path = 'wallets'
        return self.post(path, json=json_data)
    
    def update_wallet(self, wallet_id, assurance_level, name):
        """
        Request:
        {
            "assuranceLevel": "normal",
            "name": "My Wallet"
        }
        Response:
        {
            "data": {
                "assuranceLevel": "normal",
                "balance": 41984918983627330,
                "createdAt": "2032-07-26T13:46:01.035803",
                "hasSpendingPassword": false,
                "id": "J7rQqaLLHBFPrgJXwpktaMB1B1kQBXAyc2uRSfRPzNVGiv6TdxBzkPNBUWysZZZdhFG9gRy3sQFfX5wfpLbi4XTFGFxTg",
                "name": "My wallet",
                "spendingPasswordLastUpdate": "2029-04-05T12:13:13.241896",
                "syncState": {
                "data": null,
                "tag": "synced"
                }
            },
            "meta": {
                "pagination": {
                "page": 1,
                "perPage": 10,
                "totalEntries": 0,
                "totalPages": 0
                }
            },
            "status": "success"
        }
        """
        json_data = {
            "assurance_level": assurance_level,
            "name": name
        }
        return self.put(path='wallets', params=wallet_id, json=json_data)
    
    def update_password(self, wallet_id, old_password, new_password):
        """
        Request:
        {
            "old": "111111",
            "new": "222"
        }
        Response:
        {
            "data": {
                "assuranceLevel": "normal",
                "balance": 41984918983627330,
                "createdAt": "2032-07-26T13:46:01.035803",
                "hasSpendingPassword": false,
                "id": "J7rQqaLLHBFPrgJXwpktaMB1B1kQBXAyc2uRSfRPzNVGiv6TdxBzkPNBUWysZZZdhFG9gRy3sQFfX5wfpLbi4XTFGFxTg",
                "name": "My wallet",
                "spendingPasswordLastUpdate": "2029-04-05T12:13:13.241896",
                "syncState": {
                "data": null,
                "tag": "synced"
                }
            },
            "meta": {
                "pagination": {
                "page": 1,
                "perPage": 10,
                "totalEntries": 0,
                "totalPages": 0
                }
            },
            "status": "success"
        }
        """
        json_data = {
            "new": old_password,
            "old": new_password
        }
        path = 'wallet.{}.password'.format(wallet_id)
        return self.put(path, json=json_data)
    
    def get_wallets(self):
        """
        {
            Response:
            "data": [
                {
                "assuranceLevel": "normal",
                "balance": 41984918983627330,
                "createdAt": "2032-07-26T13:46:01.035803",
                "hasSpendingPassword": false,
                "id": "J7rQqaLLHBFPrgJXwpktaMB1B1kQBXAyc2uRSfRPzNVGiv6TdxBzkPNBUWysZZZdhFG9gRy3sQFfX5wfpLbi4XTFGFxTg",
                "name": "My wallet",
                "spendingPasswordLastUpdate": "2029-04-05T12:13:13.241896",
                "syncState": {
                    "data": null,
                    "tag": "synced"
                }
                }
            ],
            "meta": {
                "pagination": {
                "page": 1,
                "perPage": 10,
                "totalEntries": 0,
                "totalPages": 0
                }
            },
            "status": "success"
            }
        """
        return self.get('wallets')
    
    def get_wallet(self, wallet_id):
        """
        Response:
        {
            "data": {
                "assuranceLevel": "normal",
                "balance": 41984918983627330,
                "createdAt": "2032-07-26T13:46:01.035803",
                "hasSpendingPassword": false,
                "id": "J7rQqaLLHBFPrgJXwpktaMB1B1kQBXAyc2uRSfRPzNVGiv6TdxBzkPNBUWysZZZdhFG9gRy3sQFfX5wfpLbi4XTFGFxTg",
                "name": "My wallet",
                "spendingPasswordLastUpdate": "2029-04-05T12:13:13.241896",
                "syncState": {
                "data": null,
                "tag": "synced"
                }
            },
            "meta": {
                "pagination": {
                "page": 1,
                "perPage": 10,
                "totalEntries": 0,
                "totalPages": 0
                }
            },
            "status": "success"
        }
        """
        return self.get('wallets', params=wallet_id)
    
    def statistic_utxos(self, wallet_id):
        path = 'wallets.{}.statistics.utxos'.format(wallet_id)
        return self.get(path)
        