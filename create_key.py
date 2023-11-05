import credential;

def main():
  secret_key, public_key = credential.create_keys()
  print("secret_key:" + secret_key)
  print("public_key:" + public_key)
  
if __name__ == "__main__":
  main()
