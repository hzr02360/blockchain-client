from ecdsa import SigningKey
from ecdsa import SECP256k1

# 秘密鍵・公開鍵を生成する
def create_keys():
  secret_key = SigningKey.generate(curve=SECP256k1)
  public_key = secret_key.get_verifying_key()
  return secret_key.to_string().hex(), public_key.to_string().hex()
    
