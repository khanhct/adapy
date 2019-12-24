from .http import BaseHttpReq
from .wallet import Wallet

class NodeAda(BaseHttpReq):

    def __init__(self, url, version):
        super().__init__(url=url, version=version)
        self._wallet = Wallet(url=url, version=version)
    
    def get_node_info(self):
        return self.get('node-info')
    
    def create_account(self, wallet_id, account_name, spending_password):
        path = "wallets.{}.accounts".format(wallet_id)
        json_data = {
            "name": account_name,
            "spendingPassword": spending_password
        }
        return self.post(path, json=json_data)
        
    def get_account(self, account_id, wallet_id):
        path = 'wallets.{}.accounts.{}'.format(wallet_id, account_id)
        return self.get(path.rstrip())

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

    def get_balance(self, wallet_id, account_id):
        path = 'wallets.{}.accounts.{}'.format(wallet_id, account_id)
        result = self.get(path)
        return result['data'].get('amount')
    
    def delete_account(self, wallet_id, account_id):
        path = 'wallets.{}.accounts.{}'.format(wallet_id, account_id)
        return self.delete(path)

    def create_address(self, account_idx, spending_password, wallet_id):
        json_data = {
            "accountIndex": account_idx,
            "spendingPassword": spending_password,
            "walletId": wallet_id
        }
        return self.post('addresses', json=json_data)

    def get_addresses(self, address):
        '''
        {
            "data": {
                "changeAddress": false,
                "id": "2Tp1cYozcWTnzCJquF2wqpqYofU89jEyDB6z9PDjvJqUA6xeA56iK5HzkBqFNCvwfFLbB61f2HQVw5rDnLDgHCsVHvbUx52xBLU7kUgHd298og4vWfu37hoByu4Ni79v84PGbutuPgzwb1KFeLDL1ShCoiqUfnQAcZrJda4qtoyvh6zfRtwkxs3WiUbPMcT1pPWSQ2VVuPpKY5pmUr8vzpGmSBfCj6vN9k35pSYR3q6pn",
                "ownership": "ambiguousOwnership",
                "used": true
            },
            "meta": {
                "pagination": {}
            },
            "status": "success"
        }
        '''
        if address is None:
            return self.get('addresses')
        else:
            return self.get('addresses.{}'.format(address))
    
    def get_trxs(self, params):
        return self.get('transactions', params=params)

    def send_trx(self, trx_data):
        """
        Request:
        {
            "destinations": [
                {
                "address": "LDTseZq14n8z9d48NnMLb5F5jPK3myRvrDW7EDCeuqAFssvXTXiAtg1YftZFCRHAmCTiKEbv2rNKb5v5miYQZJnpnD6s12nPzEfX93nvV5yH7CiadLch5bC988QGd7FEvTSBAYbdwBHVY3vRCbtETm9jx88vtFCxXp9MqHrsjDkthMuhpEWSdYKMv3h7uynQdBhJ1sTKBhftPDBFpJtVed3oLbZGHk4MxHL3puENZqC",
                "amount": 7893389421760074
                },
                {
                "address": "9C7ENmch8B5UFDYeXSYatfXkSsPMViXw2GG2qgLhYQJFn7xPK9KuZWQqz8Lg1PuxoHAF28LnVW6uyvxq4jvGQ55SkAGtqd5BZTDE2geb1TCpxLRVNSL66LdPZ9dn9ob9JuYCgfq48HNoa6FW3yTQpZvujznPYoinb9p61ouAVukwZYoWmst2QxkTRAM7ThdeL9qB4UZY7PkdgrLhCtXK4okhgLZXUT1NR1uvmx8LK4hBmRiFteoRWwQpiFMYAY1Fz3qnyJ3LU3XEywteZR1EwBHQBno2gGpCUW1vYYFXP9iuadtBCGKpfzRwsk3MDZ4Sty8mUsT2nJVgqV6PmgJ",
                "amount": 23867890792708364
                }
            ],
            "groupingPolicy": "OptimizeForHighThroughput",
            "source": {
                "accountIndex": 2185829225,
                "walletId": "J7rQqaLLHBFPrgJXwpktaMB1B1kQBXAyc2uRSfRPzNVGiv6TdxBzkPNBUWysZZZdhFG9gRy3sQFfX5wfpLbi4XTFGFxTg"
            },
            "spendingPassword": "0200020100010100020202010000000201020000020002020200010200010102"
        }
        Response:
        {
            "data": {
                "amount": 28311699119270856,
                "confirmations": 4,
                "creationTime": "1977-09-26T13:35:28.425218",
                "direction": "outgoing",
                "id": "848d6fadc04dcd9af1bc462df5938ecfbe810c5ecb50971db1cf7ae224bb5955",
                "inputs": [
                {
                    "address": "9C7ENmch8B5WHJiRLFVogY6TfQJwd85osxtKubsQda5N8P2X61WLDRw1BNhAJ6hCQ4fwcNjgjTDoKnoi9WzxEcwdteWbh7gw6vjCAYfpDWWq6MjjJKb8wS8kDVH51DuyYahvVUKCkSGrfxcgqk5hAj7XtRTmnzxH9ZkW7KPt94UcEyCdRjMsh4vKoKEaZzjK7gKXyZPE7frQTKHhjteqyNgKDeZAw7KF3HqV7WjseHocAUMcUQRBHW3DsAtt5rDo4oZkBGNmcSogDkXTCdzmQi7YVwD634cUy5xpJE9DFqbUAsGt48G6MQ3yeQusJ9mgnAntLjN5UVUKLLQttDA",
                    "amount": 6374888950522614
                },
                {
                    "address": "2441xhDQ65ixn9BDToFk8SvdfbecLtn6PpDYTYpD9L4QHDj3Cix7erZAzHQ3YVBVQNYvnBMQGMSmebZdmKxHVmxN2FkBBhY2dj9SDxASQUv3zDBWy7qLdQwWS",
                    "amount": 36892870043518670
                },
                {
                    "address": "LrKNkKxZoMeMGtUAe39j1P3pn2kef63inkxmT3wLPtwaqHLpmFpaYJAki8BSwc6Wk8M9crSiMbS4SPq5vPS7bUuzwNbEnmcpAgyzJPgiNLPg7QZZRrbtHXttLySGiY2tUaohxFpiiFcHUBwiL7q7SEZWKbZM1yeWB79YThxtubL3nF73S6B",
                    "amount": 42128232960387050
                },
                {
                    "address": "2cWKMJemoBam7gg1y5K2aFDhAm5L8fVc96NfxgcGhdLMFTsToNAU9t5HVdBBQKy4iDswL",
                    "amount": 16412596055594312
                }
                ],
                "outputs": [
                {
                    "address": "3Etp4Fs328mY5kvjC1RECHf129dyA2N85Ra9GETYpKeXQuGsMkJhG9qHpoXKQjNgN4unvBrPKdr77gADwzpeHkKQJACVBEgVgTY7LACDdgEthwenY7gs5BABEncwCrjdXyYRKWaY9GL5op6mwHBGpAA5UmEou7ATU1U4qn9KhKD31BnzyqapNVood",
                    "amount": 12346308348677984
                },
                {
                    "address": "YQdiVKZwx4SuCmAGcAZhRwDabqs7YMh1uTNqVCkPWEcsjUGAZyKoiKBu3YBhFyvoR4C2eYQ",
                    "amount": 3299396411509641
                },
                {
                    "address": "zCx6iXuvtn6P9m2KQ9mbZg8sxhknmSibuPZA4yyYLCtkMFjjdGQEjbRaWPjHdev67mNjhzewG7rCgbuwNYVsoHqzVu6NikeF5qA4hugUJVsu9N8U8hzdtrUK1bem4oMfaujTgm6mx8GmP5haT2j1sqjmQuNJ8QvranW1XSbkPxqU9CJa2Q2CCuHmzB4vGy7uM3qP8cuMmjmp3NuGKWTYv6U7riZQyU2AZ31mqkVi",
                    "amount": 11255318654184132
                },
                {
                    "address": "2Fc9FhbWKyhEGnFnqeat6M2bvZrs88sjaVovtqeDouXwc1zZHESBN4oixxSArJnqesPQbowsN2mX4nD87eWAYUYS8C2wW8TSFhCRz1AcFWE9mhrq3ExqYEAgowurBLuCgkno34rHsbvF2PLw8gWR8qnZafr1H7trVrY8WKxUppXgiQp83uzLuUZWFHMtDcWx26H3cy34jrEHgQHpzGHNepqdPCcJ2B3LEcEVHynDNE88FkFwe2uCANtatm3RuUQdFd3QYqoBXjppFLo8aX5ztPEEyKEHCXEfUmxxSRCxpwDo8JbwoSYBYtnrynXXbSYPhqPnkYNpMPfGfM",
                    "amount": 3709889702173341
                }
                ],
                "status": {
                "data": {},
                "tag": "persisted"
                },
                "type": "foreign"
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
        return self.post('transactions', json=trx_data)