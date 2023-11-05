# トランザクションを登録するクライアント機能
import requests
import json
import datetime

def main():
  transaction = {
    "time": datetime.datetime.now().isoformat(),
    "sender": "Sato",
    "reciever": "Mori",
    "amount": 999,
    "description": "bc02",
    "signature": "234567890ab"
  }
  # url = "http://127.0.0.1:8001/put_transaction/"
  # url = "https://blockchain-1-q4494128.deta.app/put_transaction"
  # url = "https://blockchain-3-q4494128.deta.app/put_transaction"
  # url = "https://bc-sample.onrender.com/put_transaction"
  url = "https://bc-api-0z7g.onrender.com/put_transaction"
  res = requests.post(url, json.dumps(transaction))
  print(res.json())

if __name__ == "__main__":
  main()
