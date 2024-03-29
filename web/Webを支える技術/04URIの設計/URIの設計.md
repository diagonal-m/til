# URIの設計

## クールなURIは変わらない

- 良いURIやきれいなURIのことを「クールURI」と呼ぶ
- URIは変わらないべきである。変わらないURIこそが最上のURI
  - クールURI

## URIを変わりにくくするには

### プログラミング言語に依存した拡張子やパスを含めない

- URIを変えにくくするためにまずするべきことは、プログラミング言語に依存した部分の排除

  - e.g.) Webサイト共通のログインページ `http://example.jp/cgi-bin/login.pl`

  - ↑のURIは２つの実装依存箇所がある。「cgi-bin」というパスと、「.pl」という拡張子

  - ↑のようなURIは前世紀によく見かけたが、２つの理由から２１世紀には見つからなくなっていった

    - CGIが廃れた。→ リクエストのたびにプロセスを起動するCGI方式は性能面で難点があったため、そのほかの手法にとって代わられた。
    - 実装言語の選択肢が増加したこと→CGIの時代はほとんどのWebサービスがPerlで書かれていた。

  - e.g.2) 

    ```
    http://example.jp/servlet/LoginServlet
    ```

    - パスの「servlet」は特定のサーブレットコンテナのデフォルトパスであって、システムをサーブレットからPHPに変えたとたんに変更になる

### メソッド名やセッションIDを含めない

- e.g.) 

  ```
  http://example.jp/Login.do?action=showPage
  ```

  - Webアプリケーションフレームワークとして古いStrutsを採用すると、このようなURIになる。→Struts特有の拡張子である「.do」も問題。
  - より問題なのはshowPageというメソッド名がURIに入っていること
    - システムをリファクタリングしてメソッド名を変更した途端にURIが変更になってしまう

- e.g.2) 

  ```
  http://exaple.jp/home.jsp?jsessinod=12345678
  ```

  - セッションIDを含んだURI
  - セッションIDはログインのたびに変わるので、このURIはシステムにログインし直すと変更になる

### URIはリソースを表現する名詞にする

- URIはリソースの名前→URIは名詞であるべきである→この作法は守られないことが往々にある

- 初期のRuby on Railsでは次のようなURIが一般的だった

- ```
  http://example.jp/sample/people/show/123
  ```

  - これはIDが123である人物のリソースのURIである
  - パスの部分はsampleアプリケーションのPeopleコントローラのshowメソッドに由来している
  - 最後の「123」はデータベースのIDである
  - 一見するとシンプルで良いURIに見えるが「show」が問題である。
  - HTTPではリソースに対して特定のHTTPメソッドだけを適用する。
  - あるリソースを取得するのか更新するのかは、URIで指定するのではなく、URIに適用するHTTPメソッドで決定する
  - つまり、URIとHTTPメソッドの関係は、名詞と動詞の関係にある
  - したがってURIは、全体として名詞となるように設計するべきである

### URIの設計指針

- URIにプログラミング言語依存の拡張子を利用しない
- URIに実装依存のパス名を利用しない
- URIにプログラミング言語のメソッド名を利用しない
- URIにセッションIDを含めない
- URIはそのリソースを表現

## URIのユーザビリティ

- シンプルなURIにはユーザビリティが高まるとい利点もある
  - `http:://example.jp/servlet/LoginServlet`
  - `http:://example.jp/login`
  - → まず文字数が違う。文字数は、Web以外のメディアにURIを記載する際に重要

## URIを変更したい時

- どうしてもURIを変更したい時は、できる限りリダイレクトするようにする
- リダイレクトとは、古いURIを新しいURIに転送するHTTPのしくみのことである

## URI設計のテクニック

### 拡張子で表現を指定する

- 実装に依存していない拡張子は良い側面を持つ場合もある

- 拡張子の良い側面として、リソースの表現を特定する拡張子の使い方に関して

  - 例としてプレスリリースをWebで公開するケース

  - グローバルに活動する企業では、プレスリリースを複数の言語で記述することが一般的である→ここでは同じ内容のプレスリリースが日本語と英語で書かれているとする

  - 2010年5月1日に発表したプレスリリースの場合、URIはたとえば次のようになる

  - e.g.) 

    ```
    http://example.jp/2010/05/01/press
    ```

    - HTTPにはコンテントネゴシエーションという便利な機能があり
    - 日本語版のOSを使っているユーザには日本語を、英語版のOSを使っているユーザには英語を返せる

### マトリクスURI

- URIはスラッシュ(/)を使って階層を表現できる。例えば2010年5月1日の日記のURI
- `http://example.jp/diary/2010/05/01`
- ↑のように表現できる。これは日付情報が年→月→日という階層構造を持っているからである

## URIの不透明性

- シンプルなURIは可読性が高いため、ユーザがURIの構造を推測しやすくなる

## URIを強く意識する

- URIは、Webアプリケーションフレームワークが隠蔽し、通常のプログラマはあまり意識をしなくても良い存在になってしまいがち
- しかし、URIは次の点でとても重要である
  - URIはリソースの名前である
  - URIは寿命が長い
  - URIはブラウザがアドレス欄に表示する

→ URIはWebサービスやWeb APIの設計において最も重視するべきパーツであるといえる。