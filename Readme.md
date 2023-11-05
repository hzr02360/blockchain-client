# Overview

以下の機能を実装する

- 公開鍵と秘密鍵を生成する
- ブロックチェーンサーバにトランザクションを登録する

# Usage

## 公開鍵と秘密鍵を生成

```bash
$ python create_key.py
secret_key:fa6148d0bbff1d93c744cb3f4e1763445fb0c5e548c3c4c2b4e1d875790d4d62
public_key:a1e1f4542b3ff5b4ebea0921825e3198115ab9cc2674ca0b6ae9da3e8217227610fd2f3714e51452d6e4603e4bf2b6c3cdf3a29df7e7cd3188e466c13fbd1957
$
```

## トランザクションを登録

- 送信者／受信者の公開鍵と秘密鍵をそれぞれ生成する
- 生成した鍵を post_transaction.py に反映する

```bash
$ python post_transaction.py
$
```
