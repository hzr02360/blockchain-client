# トランザクションを登録するクライアント機能
import os
import sys
import requests
import json
import datetime
import yaml
from credential import create_secret_key, create_signeture

# シグネチャ付きのトランザクションデータを生成する
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

# 引数チェック
def check_arg():
  if (len(sys.argv) <= 1):
    print("parameter file is required.")
    sys.exit(4)

  yaml_file = sys.argv[1]
  if os.path.exists(yaml_file) == False:
    print(f"{yaml_file} is not found.")
    sys.exit(4)
  return yaml_file

# トランザクションデータ登録クライアント
def main():
  yaml_file = check_arg()
  with open(yaml_file, 'r') as f:
    arg = yaml.safe_load(f)
    
  transaction = create_transaction(
    arg['secret_key'],
    arg['sender_pub_key'],
    arg['reciever_pub_key'],
    arg['amount'],
    arg['desc'])
  print(transaction)
  print(f"URL: {arg['url']}")
  res = requests.post(arg['url'], json.dumps(transaction))
  print(res)

if __name__ == "__main__":
  main()
