# ブロックチェーンクライアント

以下の機能を実装する

- 公開鍵と秘密鍵を生成するコマンド
- ブロックチェーンサーバにトランザクションを登録するコマンド

## 環境

- python3 と以下のフレームワーク・ライブラリ

| ライブラリ名                                   | 用途                                |
| ---------------------------------------------- | ----------------------------------- |
| [requests](https://pypi.org/project/requests/) | Python で使われる HTTP ライブラリ   |
| [pyyaml](https://pypi.org/project/PyYAML/)     | yaml ファイルを扱うためのライブラリ |

- Ubuntu 22.04.3 LTS

## 実行方法

### 公開鍵と秘密鍵を生成する

```bash
$ python create_key.py
secret_key:fa6148d0bbff1d93c744cb3f4e1763445fb0c5e548c3c4c2b4e1d875790d4d62
public_key:a1e1f4542b3ff5b4ebea0921825e3198115ab9cc2674ca0b6ae9da3e8217227610fd2f3714e51452d6e4603e4bf2b6c3cdf3a29df7e7cd3188e466c13fbd1957
```

### トランザクションを登録する

- 送信者／受信者の公開鍵と秘密鍵をそれぞれ生成する
- 生成した鍵を `data` 配下のデータファイルに反映する

```yaml
secret_key: "fa6148d0bbff1d93c744cb3f4e1763445fb0c5e548c3c4c2b4e1d875790d4d62"
sender_pub_key: "a1e1f4542b3ff5b4ebea0921825e3198115ab9cc2674ca0b6ae9da3e8217227610fd2f3714e51452d6e4603e4bf2b6c3cdf3a29df7e7cd3188e466c13fbd1957"
reciever_pub_key: "d3f9cb2f7d217d6d5295cc61c64caf63dcb2ad6f49baca4be967fa29d2214e25be99eaaf084c32aae81d1ef941ee89fac6b98b8740e2457f8457bb9627a9141c"
amount: 198
desc: "A -> B"
url: "http://127.0.0.1:8003/put_transaction/"
```

- データファイルを指定してトランザクションを登録する

```bash
$ python post_transaction.py data/local-03_a2b.yml
{'time': '2023-11-05T17:06:49.854296', 'sender': 'd3f9cb2f7d217d6d5295cc61c64caf63dcb2ad6f49baca4be967fa29d2214e25be99eaaf084c32aae81d1ef941ee89fac6b98b8740e2457f8457bb9627a9141c', 'reciever': 'a1e1f4542b3ff5b4ebea0921825e3198115ab9cc2674ca0b6ae9da3e8217227610fd2f3714e51452d6e4603e4bf2b6c3cdf3a29df7e7cd3188e466c13fbd1957', 'amount': 222, 'description': 'B -> A', 'signature': '8821dc89639ee519090d4a3ae4461adaef3fe0fbdbde4bb0475d4f54fcd4858b04f8b00e7b7e7b26a2c466634a817ee1b7ba76637b1da42ac4696dc491384604'}
URL: http://127.0.0.1:8002/put_transaction/
```

## 実装

### フォルダとファイル構成

```
../blockchain-client/
├── Readme.md
├── __pycache__
├── create_key.py
├── credential.py
├── data
│   ├── blockchain-api-01_a2b.yml
│   ├── blockchain-api-02_b2a.yml
│   ├── local-01_b2a.yml
│   └── local-03_a2b.yml
└── post_transaction.py
```

### ソースコード一覧

| ファイル名            | 用途 　                          |
| --------------------- | -------------------------------- |
| `create_key.py`       | 秘密鍵・公開鍵を生成する         |
| `post_transaction.py` | トランザクションデータを登録する |
| `credential.py`       | 秘密鍵・公開鍵関連の共通部品     |
