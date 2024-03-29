# HTTPとDNS

## 構築する環境

 [![Image from Gyazo](https://i.gyazo.com/41e028d2377aa1b95f8b7ef838821dde.png)](https://gyazo.com/41e028d2377aa1b95f8b7ef838821dde)



### 名前とは

- hoge.diagonalm.comは人間に読みやすい・覚えやすい名前
- アクセスする際に使われているのはIPアドレス
- hoge.diagonalm.comのIPアドレスは？

### 名前解決

- hoge.diagonalm.com = 103.86.62.62, 104.26.40.89
- DNSを使ってドメイン名をIPアドレスに紐づける



## HTTP Hypertext Transfer Protocol

### Hypertext Transfer Protocol

- 汎用的なテキストベースでやり取りの為のプロトコル
  - やり取りはテキストベースでも送るデータは自由
- Google Chrome等のブラウザは裏でHTTPを使っている
  - 送られたHTMLを良い感じに解釈してくれるだけ



## HTTPリクエスト

### Method

- GET: リソースを取得
- POST：リソースを送る、処理を依頼する
- DELETE ：リソースを消す
- PUT：サーバーが持っているリソースを置き換える
- PATCH：リソースを部分的に更新する

### Target

- サーバーのどのリソース・エンドポイントに対しての要求を指定
  - 単純なファイル(データ)
  - 動的なファイルコンテンツ

### Version

- どのHTTPバージョンを使うかを指定
  - HTTP/1.0
  - HTTP/1.1
  - HTTP/2
  - HTTP/3

### ヘッダー

- リクエストに対する追加情報
- Host：同じIPアドレスで複数サービスを立てる時に必要

### Body

- 使うHTTP methodによってクライアントからデータを送る場合もある
  - POST/PUT等
- その時はヘッダーの後にリクエストの中身(body)を入れる

## HTTPレスポンス

### Status code

- リクエストの処理結果
- 1xx：コネクション情報
- 2xx：成功系
- 3xx：リダイレクト系
- 4xx：クライアント側のエラー
- 5xx：サーバー側のエラー

### 追加リクエスト

- Status codeによってクライアントに追加処理が発生する
  - リダイレクトを追う
  - 認証情報の入力要求

### Reason

- Status codeに合わせて理由がつくこともある
  - 例えば200の場合：OK
- 主に人間に読まれるためにある

### 動的コンテンツ

- HTTPサーバーは、受け取ったHTTPリクエストに対し、反応する
- HTTPレスポンスをどうやって生成するか
  - ファイルをそのまま送る
  - 内容を動的に生成して送る

## HTTPS

### HTTP Secure

- HTTPは平文プロトコル=攻撃者が簡単に情報を盗める
- HTTPS:HTTPをTLSの上に構築
  - TLS：Transport Layer Security
- 暗号化されるので盗聴されても解読が難しい

### TLSで守りたいもの・守り方

- 通信相手が本物であること→デジタル署名
  - (クライアント視点で)本物のサーバーか？
  - (サーバー視点で)本物のクライアントか？
- 通信内容が盗聴されないこと→対称暗号
  - クレジットカード番号などが漏えいしないように
- 通信内容が改窮されないこと→メッセージ認証コード

### SSL証明書の発行

- 公開鍵と非公開鍵を使う