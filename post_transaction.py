# トランザクションを登録するクライアント機能
import requests
import json
import datetime

from credential import create_secret_key, create_signeture

def create_transaction(secret_key, sender_pub_key, reciever_pub_key, amount, desc):
  time = datetime.datetime.now().isoformat()
  unsigned_tran = {
    "time": time,
    "sender": sender_pub_key,
    "reciever": reciever_pub_key,
    "amount": amount,
    "description": desc
  }
  secret_key = create_secret_key(secret_key)
  json_unsigned_tran = json.dumps(unsigned_tran)
  signature_str = create_signeture(json_unsigned_tran, secret_key)

  singed_tran = {
    "time": time,
    "sender": sender_pub_key,
    "reciever": reciever_pub_key,
    "amount": amount,
    "description": desc,
    "signature": signature_str
  }
  return singed_tran

def main():
  # secret_key = "fa6148d0bbff1d93c744cb3f4e1763445fb0c5e548c3c4c2b4e1d875790d4d62"
  # sender_pub_key = "a1e1f4542b3ff5b4ebea0921825e3198115ab9cc2674ca0b6ae9da3e8217227610fd2f3714e51452d6e4603e4bf2b6c3cdf3a29df7e7cd3188e466c13fbd1957"
  # reciever_pub_key = "d3f9cb2f7d217d6d5295cc61c64caf63dcb2ad6f49baca4be967fa29d2214e25be99eaaf084c32aae81d1ef941ee89fac6b98b8740e2457f8457bb9627a9141c"
  secret_key = "2456056f9a0606197e3977033f6bd8a04f5b039f1f4865cb4f98e239dba1aee1"
  sender_pub_key = "d3f9cb2f7d217d6d5295cc61c64caf63dcb2ad6f49baca4be967fa29d2214e25be99eaaf084c32aae81d1ef941ee89fac6b98b8740e2457f8457bb9627a9141c"
  reciever_pub_key = "a1e1f4542b3ff5b4ebea0921825e3198115ab9cc2674ca0b6ae9da3e8217227610fd2f3714e51452d6e4603e4bf2b6c3cdf3a29df7e7cd3188e466c13fbd1957"
  amount = 222
  desc = "description"
  url = "http://127.0.0.1:8001/put_transaction/"
  # url = "https://blockchain-1-q4494128.deta.app/put_transaction"
  # url = "https://blockchain-3-q4494128.deta.app/put_transaction"
  # url = "https://bc-sample.onrender.com/put_transaction"
  # url = "https://bc-api-0z7g.onrender.com/put_transaction"

  transaction = create_transaction(secret_key, sender_pub_key, reciever_pub_key, amount, desc)
  res = requests.post(url, json.dumps(transaction))
  print(res)

if __name__ == "__main__":
  main()
