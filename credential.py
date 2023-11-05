from ecdsa import SigningKey
from ecdsa import SECP256k1
import binascii

# 秘密鍵・公開鍵を生成する
def create_keys():
  secret_key = SigningKey.generate(curve=SECP256k1)
  public_key = secret_key.get_verifying_key()
  return secret_key.to_string().hex(), public_key.to_string().hex()

# 秘密鍵を生成する
def create_secret_key(pub_key):
  return SigningKey.from_string(binascii.unhexlify(pub_key), curve=SECP256k1)

# シグネチャを生成する
def create_signeture(json, secret_key):
  bytes_tran = bytes(json, encoding="utf-8")
  return secret_key.sign(bytes_tran).hex()