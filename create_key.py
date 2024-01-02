import credential;

# 公開鍵・秘密鍵を生成する
def main():
  secret_key, public_key = credential.create_keys()
  print("secret_key:" + secret_key)
  print("public_key:" + public_key)
  
if __name__ == "__main__":
  main()
