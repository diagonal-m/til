# HTTPの基本

- TCP/IPとは何か
- クライアントで行われること/サーバで行われること

## TCP/IPとは何か

- HTTPはTCP/IPをベースにしている。TCP(Transmission Control Protocol)とIP(Internet Protocol)は、インターネットの基盤を構成する重要なネットワークプロトコルである。

### 階層型プロトコル

- インターネットのネットワークプロトコルは階層型になっている

| アプリケーション層<br />HTTP,NTP,SSH,SMTP,DNS        |
| ---------------------------------------------------- |
| **トランスポート層**<br />UDP, TCP                   |
| **インターネット層**<br />IP                         |
| **ネットワークインターフェース層**<br />イーサネット |

### ネットワークインターフェース層

- 物理的なケーブルやネットワークアダプタに相当

### インターネット層

- ネットワークでデータを実際にやり取りする部分を担当→TCP/IPではIPが相当
- IPではデータの基本的な通信単位を「パケット」(Packet)と呼ぶ
- IPでは、自分のネットワークインターフェースでデータを送り出すことだけを保障している

### トランスポート層

- IPが保証しなかったデータの転送を保証するのがトランスポート層の役割→TCP/IPではTCPが担当
- TCPでは接続先の相手に対してコネクションを張る。
  - コネクションを使ってデータの抜け漏れをチェックし、データの到達を保証する
- TCPで接続したコネクションで転送するデータが、どのアプリケーションに渡るのかを決定するのがポート番号。
  - ポート番号は1~65535の数値

### アプリケーション層

- 具体的なインターネットアプリケーション、たとえばメールやDNS、HTTPを実現する層
- TCPでプログラムを作るときは、ソケット(Socket)と呼ばれるライブラリを使うのが一般的
  - Socketはネットワークでのデータのやりとりを抽象化したAPI
  - 接続、送信、受信、切断等の基本的な機能を備えている
  - HTTPサーバやブラウザはソケットを用いて実装する

## クライアントとサーバ

- Webはアーキテクチャスタイルにクライアント/サーバを採用している
  - クライアント(Webブラウザ)が情報を提供するサーバ(Webサーバ)に接続し
  - 各種のリクエスト(Request, 要求)を出してレスポンス(Response, 返答)を受け取る

## リクエストとレスポンス

- HTTPではクライアントが出したリクエストをサーバで処理してレスポンスを返す

  → このようなプロトコルをリクエスト/レスポンス型のプロトコルと呼ぶ

### クライアントで行われること

- クライアントでは１つのリクエストを送信しレスポンスを受信する際に次のことを行う
  1. リクエストメッセージの構築
  2. リクエストメッセージの送信
  3. (レスポンスが返るまで待機)
  4. レスポンスメッセージの受信
  5. レスポンスメッセージの解析
  6. クライアントの目的を達成するために必要な処理

### サーバで行われること

- クライアントからリクエストを受けたサーバは次のことを行う
  1. (リクエストの待機)
  2. リクエストメッセージの受信
  3. リクエストメッセージの解析
  4. 適切なアプリケーションプログラムへの処理の委譲
  5. アプリケーションプログラムから結果を取得
  6. レスポンスメッセージの構築
  7. レスポンスメッセージの送信

