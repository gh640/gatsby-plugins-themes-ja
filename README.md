# Gatsby 公式のプラグイン・テーマまとめ

静的サイトジェネレータ（ SSG ）である Gatsby が公式に提供するプラグインとテーマの一覧です。

正確には「公式の monorepo リポジトリに含まれているプラグインとテーマ」の一覧です。

- [gatsby/packages at master · gatsbyjs/gatsby · GitHub](https://github.com/gatsbyjs/gatsby/tree/master/packages)

対象の Gatsby のバージョンは `gatsby@2` です。

- プラグイン
- テーマ

## プラグイン

プラグインの名前にルールがあって、先頭が `gatsby-source-` のものはデータソースからコンテンツを取得するもの、 `gatsby-transformer-` のものは取得したコンテンツをパースしたり変換したりするもの、 `gatsby-plugin-` のものはその他の機能を提供するプラグインです。
また、 `gatsby-transformer-remark` のサブプラグインの先頭は `gatsby-remark-` になっています。

| 名前 | 説明 |
| --- | --- |
| [`gatsby-plugin-canonical-urls`](https://www.gatsbyjs.org/packages/gatsby-plugin-canonical-urls) | HTML の `<head>` 内に `canonical` リンクを追加するためにプラグインです。 |
| [`gatsby-plugin-catch-links`](https://www.gatsbyjs.org/packages/gatsby-plugin-catch-links) | `gatsby-link` を使わずに作られたサイト内リンクに `gatsby-link` の挙動を反映するためのプラグインです。 Markdown ファイルの中でサイト内リンクを使っているとき等に便利です。 |
| [`gatsby-plugin-coffeescript`](https://www.gatsbyjs.org/packages/gatsby-plugin-coffeescript) | CoffeeScript と CJSX を利用するためのプラグインです。 |
| [`gatsby-plugin-create-client-paths`](https://www.gatsbyjs.org/packages/gatsby-plugin-create-client-paths) | 動的に動くパスを持った、動的と静的のハイブリッドな Gatsby アプリを作るためのプラグインです。 | gatsby-plugin-cxs
| css-in-js の [cxs](https://github.com/cxs-css/cxs) を利用するためのプラグインです。 |
| [`gatsby-plugin-emotion`](https://www.gatsbyjs.org/packages/gatsby-plugin-emotion) | css-in-js の [Emotion](https://github.com/emotion-js/emotion)　を利用するためのプラグインです。 |
| [`gatsby-plugin-facebook-analytics`](https://www.gatsbyjs.org/packages/gatsby-plugin-facebook-analytics) | [Facebook Analytics](https://analytics.facebook.com/) を利用するためのプラグインです。 |
| [`gatsby-plugin-feed`](https://www.gatsbyjs.org/packages/gatsby-plugin-feed) | RSS フィードを生成するためのプラグインです。 |
| [`gatsby-plugin-flow`](https://www.gatsbyjs.org/packages/gatsby-plugin-flow) | Flow を利用するためのプラグインです。 |
| [`gatsby-plugin-fullstory`](https://www.gatsbyjs.org/packages/gatsby-plugin-fullstory) | 解析サービスの [Fullstory](https://www.fullstory.com/) を利用するためのプラグインです。 |
| [`gatsby-plugin-glamor`](https://www.gatsbyjs.org/packages/gatsby-plugin-glamor) | css-in-js の [Glamor](https://github.com/threepointone/glamor)を利用するためのプラグインです。 |
| [`gatsby-plugin-google-analytics`](https://www.gatsbyjs.org/packages/gatsby-plugin-google-analytics) | Google Analytics を利用するためのプラグインです。 |
| [`gatsby-plugin-google-gtag`](https://www.gatsbyjs.org/packages/gatsby-plugin-google-gtag) | Google global site tag （ `gtag.js` ）を利用するためのプラグインです。 |
| [`gatsby-plugin-google-tagmanager`](https://www.gatsbyjs.org/packages/gatsby-plugin-google-tagmanager) | Google Tag Manager を利用するためのプラグインです。 |
| [`gatsby-plugin-guess-js`](https://www.gatsbyjs.org/packages/gatsby-plugin-guess-js) | [Guess.js](https://github.com/guess-js/guess) を利用するためのプラグインです。 |
| [`gatsby-plugin-jss`](https://www.gatsbyjs.org/packages/gatsby-plugin-jss) | css-in-js の [JSS](https://github.com/cssinjs/react-jss) を利用するためのプラグインです。 |
| [`gatsby-plugin-layout`](https://www.gatsbyjs.org/packages/gatsby-plugin-layout) | ページをまたがって存在するレイアウトコンポーネントを追加するためのプラグインです。 `gatsby@2` で Gatsby 本体から削除された `gatsby@1` のレイアウトコンポーネントを実装するものです。 |
| [`gatsby-plugin-less`](https://www.gatsbyjs.org/packages/gatsby-plugin-less) | CSS を拡張した [LESS](http://lesscss.org/) を利用するためのプラグインです。 |
| [`gatsby-plugin-lodash`](https://www.gatsbyjs.org/packages/gatsby-plugin-lodash) | Lodash を利用するための Webpack と Babel のプラグインを提供します。 |
| [`gatsby-plugin-manifest`](https://www.gatsbyjs.org/packages/gatsby-plugin-manifest) | PWA 仕様を満たすのに必要な web app manifest （ `manifest.webmanifest` ）をサポートするためのプラグインです。 manifest の生成の他に、複数のサイズのアイコンの生成、 favicon 追加等の機能も備えています。 `gatsby-plugin-offline` と併用することが推奨されています。 |
| [`gatsby-plugin-mdx`](https://www.gatsbyjs.org/packages/gatsby-plugin-mdx) | [MDX](https://mdxjs.com/) を利用するためのプラグインです。 MDX は JSX の中に Markdown が書けるフォーマットです。 |
| [`gatsby-plugin-netlify-cms`](https://www.gatsbyjs.org/packages/gatsby-plugin-netlify-cms) | [Netlify CMS](https://www.netlifycms.org/) を利用するためのプラグインです。パス `admin/index.html` に Netlify CMS を生成します。 |
| [`gatsby-plugin-netlify`](https://www.gatsbyjs.org/packages/gatsby-plugin-netlify) | Netlify に対応するためのプラグインです。デフォルトでは、 Netlify のヘッダーとリダイレクトの設定のために `_headers` と `_redirects` という 2 つのファイルを public フォルダのルートに設置します。 |
| [`gatsby-plugin-no-sourcemaps`](https://www.gatsbyjs.org/packages/gatsby-plugin-no-sourcemaps) | ソースマップを生成しないようにするためのプラグインです。 Webpack の設定のためのほんの数行のコードからなるプラグインです。 |
| [`gatsby-plugin-nprogress`](https://www.gatsbyjs.org/packages/gatsby-plugin-nprogress) | [Nprogress.js](http://ricostacruz.com/nprogress/) を利用するためのプラグインです。 |
| [`gatsby-plugin-offline`](https://www.gatsbyjs.org/packages/gatsby-plugin-offline) | ネットワーク環境が悪い場合でもサイトがなるべく動くようにするためのプラグインです。 Service Worker を追加します。 `gatsby-plugin-manifest` と併用することが推奨されています。 |
| [`gatsby-plugin-page-creator`](https://www.gatsbyjs.org/packages/gatsby-plugin-page-creator) | 指定されたパスの下の React コンポーネントを含むファイルからページを自動生成するためのプラグインです。 Gatsby 本体が利用しており、デフォルトでは `src/pages` 以下のファイルが対象になっています。 | gatsby-plugin-postcss
| [PostCSS](https://postcss.org/) を利用するためのプラグインです。 |
| [`gatsby-plugin-preact`](https://www.gatsbyjs.org/packages/gatsby-plugin-preact) | React の軽量版である [Preact](https://preactjs.com/) を利用するためのプラグインです。 |
| [`gatsby-plugin-preload-fonts`](https://www.gatsbyjs.org/packages/gatsby-plugin-preload-fonts) | パフォーマンス改善のために、ページで使われているフォントを `<link rel="preload">` で先読みするためのプラグインです。 |
| [`gatsby-plugin-react-css-modules`](https://www.gatsbyjs.org/packages/gatsby-plugin-react-css-modules) | React コンポーネント内の `styleName` を `className` に変換するプラグインです。 Gatsby は CSS モジュールをデフォルトでサポートしているため、このプラグインは通常必要ありません。 |
| [`gatsby-plugin-react-helmet`](https://www.gatsbyjs.org/packages/gatsby-plugin-react-helmet) | [React Helmet](https://github.com/nfl/react-helmet) を利用するためのプラグインです。 HTML の `<head>` タグ内に `<title>` や `<meta>` 等のタグがかんたんに追加できます。 |
| [`gatsby-plugin-remove-trailing-slashes`](https://www.gatsbyjs.org/packages/gatsby-plugin-remove-trailing-slashes) | パスの末尾の `/` （スラッシュ）を削除するためのプラグインです。 |
| [`gatsby-plugin-sass`](https://www.gatsbyjs.org/packages/gatsby-plugin-sass) | Sass/SCSS を利用するためのプラグインです。 |
| [`gatsby-plugin-schema-snapshot`](https://www.gatsbyjs.org/packages/gatsby-plugin-schema-snapshot) | GraphQL のスキーマのスナップショットファイルを生成するためのプラグインです。デフォルトで `schema.gql` という名前のファイルに出力します。 |
| [`gatsby-plugin-sharp`](https://www.gatsbyjs.org/packages/gatsby-plugin-sharp) | 画像処理ライブラリの sharp を利用するためのプラグインです。画像をレスポンシブ化する際によく利用されます。 |
| [`gatsby-plugin-sitemap`](https://www.gatsbyjs.org/packages/gatsby-plugin-sitemap) | マシン向けのサイトマップ（ `sitemap.xml` ）を生成するためのプラグインです。 |
| [`gatsby-plugin-styled-components`](https://www.gatsbyjs.org/packages/gatsby-plugin-styled-components) | [`styled-components`](https://github.com/styled-components/styled-components) を利用するためのプラグインです。 |
| [`gatsby-plugin-styled-jsx`](https://www.gatsbyjs.org/packages/gatsby-plugin-styled-jsx) | [`styled-jsx`](https://github.com/vercel/styled-jsx) を利用するためのプラグインです。 |
| [`gatsby-plugin-styletron`](https://www.gatsbyjs.org/packages/gatsby-plugin-styletron) | [Styletron](https://github.com/styletron/styletron) を利用するためのプラグインです。 |
| [`gatsby-plugin-stylus`](https://www.gatsbyjs.org/packages/gatsby-plugin-stylus) | [Stylus](https://www.stylus.com/) を利用するためのプラグインです。 |
| [`gatsby-plugin-subfont`](https://www.gatsbyjs.org/packages/gatsby-plugin-subfont) | Google fonts 等のウェブフォントの配信を最適化するためのライブラリ [Subfont](https://github.com/Munter/subfont#readme) を利用するためのプラグインです。 |
| [`gatsby-plugin-twitter`](https://www.gatsbyjs.org/packages/gatsby-plugin-twitter) | Twitter のツイートやタイムラインやシェアボタンをページに埋め込むためのプラグインです。 |
| [`gatsby-plugin-typescript`](https://www.gatsbyjs.org/packages/gatsby-plugin-typescript) | TypeScript を利用するためのプラグインです。 Gatsby 本体が利用しています。 |
| [`gatsby-plugin-typography`](https://www.gatsbyjs.org/packages/gatsby-plugin-typography) | タイポグラフィー・フォント周りの設定を行うための [Typography](https://kyleamathews.github.io/typography.js/) を利用するためのプラグインです。 |
| [`gatsby-remark-autolink-headers`](https://www.gatsbyjs.org/packages/gatsby-remark-autolink-headers) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内の各見出し（ `h1` - `h6` ）にリンク付きのアイコンを付けられるプラグインです（ GitHub の README にあるようなものです）。 |
| [`gatsby-remark-code-repls`](https://www.gatsbyjs.org/packages/gatsby-remark-code-repls) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内でウェブ上で JS コードを試せる Codepen 等のサービスへのリンクを生成できるプラグインです。 |
| [`gatsby-remark-copy-linked-files`](https://www.gatsbyjs.org/packages/gatsby-remark-copy-linked-files) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内でリンクで参照されているファイルを public フォルダにコピーするプラグインです。 |
| [`gatsby-remark-custom-blocks`](https://www.gatsbyjs.org/packages/gatsby-remark-custom-blocks) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内で使えるカスタムブロックを定義して利用できるプラグインです。 [`remark-custom-blocks`](https://github.com/zestedesavoir/zmarkdown/tree/master/packages/remark-custom-blocks) を使用します。 |
| [`gatsby-remark-embed-snippet`](https://www.gatsbyjs.org/packages/gatsby-remark-embed-snippet) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内でファイルの中身をコードスニペットとして埋め込めるプラグインです。動作には `gatsby-remark-prismjs` が必要です。 |
| [`gatsby-remark-graphviz`](https://www.gatsbyjs.org/packages/gatsby-remark-graphviz) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内の [Graphviz](https://www.graphviz.org/) のコードブロックを SVG 画像に変換してくれるプラグインです。しかし、このプラグインが利用する [Viz.js](https://github.com/mdaines/viz.js/) の開発が終了しています。 |
| [`gatsby-remark-images`](https://www.gatsbyjs.org/packages/gatsby-remark-images) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内の画像をレスポンシブ化するためのプラグインです。 `png` と `jpg` をサポートしています。 |
| [`gatsby-remark-images-contentful`](https://www.gatsbyjs.org/packages/gatsby-remark-images-contentful) | `gatsby-transformer-remark` のサブプラグインで、 Contentful の Image API を使って Markdown 内の画像をレスポンシブ化するためのプラグインです。 |
| [`gatsby-remark-katex`](https://www.gatsbyjs.org/packages/gatsby-remark-katex) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内に数式を書くためのプラグインです。 |
| [`gatsby-remark-prismjs`](https://www.gatsbyjs.org/packages/gatsby-remark-prismjs) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内のコードブロックにシンタックスハイライトを追加できるプラグインです。シンタックスハイライト用のライブラリ [Prism](https://prismjs.com/) を使用します。 |
| [`gatsby-remark-responsive-iframe`](https://www.gatsbyjs.org/packages/gatsby-remark-responsive-iframe) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内の `<iframe>` タグの縦横比を維持するためのプラグインです。 |
| [`gatsby-remark-smartypants`](https://www.gatsbyjs.org/packages/gatsby-remark-smartypants) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内のアルファベットの句読点をきれいな形に変換してくれるプラグインです。 |
| [`gatsby-source-contentful`](https://www.gatsbyjs.org/packages/gatsby-source-contentful) | ヘッドレス CMS （ API ファースト CMS ）の [Contentful](https://www.contentful.com/) からコンテンツデータを取得するためのプラグインです。 |
| [`gatsby-source-drupal`](https://www.gatsbyjs.org/packages/gatsby-source-drupal) | CMS Drupal からコンテンツデータを取得するためのプラグインです。 |
| [`gatsby-source-faker`](https://www.gatsbyjs.org/packages/gatsby-source-faker) | フェイクデータ（テストや検証のためのデータ）を生成するライブラリ [`faker.js`](https://github.com/marak/Faker.js/) を使ってフェイクコンテンツを取得するためのプラグインです。 |
| [`gatsby-source-filesystem`](https://www.gatsbyjs.org/packages/gatsby-source-filesystem) | ローカルのファイルシステムからコンテンツデータを取得するためのプラグインです。 |
| [`gatsby-source-graphql`](https://www.gatsbyjs.org/packages/gatsby-source-graphql) | 任意の GraphQL API からデータを取得するためのプラグインです。 |
| [`gatsby-source-hacker-news`](https://www.gatsbyjs.org/packages/gatsby-source-hacker-news) | [Hacker News API](https://github.com/HackerNews/API) からコンテンツデータを取得するためのプラグインです。 |
| [`gatsby-source-lever`](https://www.gatsbyjs.org/packages/gatsby-source-lever) | リクルーティング活動支援のウェブサービス [Lever](https://www.lever.co/) からデータを取得するためのプラグインです。 |
| [`gatsby-source-medium`](https://www.gatsbyjs.org/packages/gatsby-source-medium) | Medium の非公式の JSON エンドポイントからコンテンツデータを取得するためのプラグインです。ただし取得できる内容・件数がかぎられています。 |
| [`gatsby-source-mongodb`](https://www.gatsbyjs.org/packages/gatsby-source-mongodb) | MongoDB のコレクションからデータを取得するためのプラグインです。 |
| [`gatsby-source-npm-package-search`](https://www.gatsbyjs.org/packages/gatsby-source-npm-package-search) | Yarn の Algolia の機能を使って npm のパッケージ情報を取得するためのプラグインです。 |
| [`gatsby-source-shopify`](https://www.gatsbyjs.org/packages/gatsby-source-shopify) | EC サービス [Shopify](https://www.shopify.com/) のストアから Shopify Storefront API を使ってデータを取得するためのプラグインです。 |
| [`gatsby-source-wikipedia`](https://www.gatsbyjs.org/packages/gatsby-source-wikipedia) | Wikipedia から記事データを取得するためのプラグインです。 |
| [`gatsby-source-wordpress`](https://www.gatsbyjs.org/packages/gatsby-source-wordpress) | WordPress サイトから WordPress REST API を使ってコンテンツデータを取得するためのプラグインです。 |
| [`gatsby-transformer-asciidoc`](https://www.gatsbyjs.org/packages/gatsby-transformer-asciidoc) | AsciiDoc ファイルをコンテンツソースとしてパースするためのプラグインです。 |
| [`gatsby-transformer-csv`](https://www.gatsbyjs.org/packages/gatsby-transformer-csv) | CSV ファイルをコンテンツソースとしてパースするためのプラグインです。 |
| [`gatsby-transformer-documentationjs`](https://www.gatsbyjs.org/packages/gatsby-transformer-documentationjs) | JavaScript のコードから JSDoc のデータを抽出するためのプラグインです。 |
| [`gatsby-transformer-excel`](https://www.gatsbyjs.org/packages/gatsby-transformer-excel) | Excel ファイルをコンテンツソースとしてパースするためのプラグインです。 |
| [`gatsby-transformer-hjson`](https://www.gatsbyjs.org/packages/gatsby-transformer-hjson) | Hjson ファイルをコンテンツソースとしてパースするためのプラグインです。 |
| [`gatsby-transformer-javascript-frontmatter`](https://www.gatsbyjs.org/packages/gatsby-transformer-javascript-frontmatter) | JavaScript ファイルの `exports.frontmatter` をコンテンツソースとして抽出するためのプラグインです。 |
| [`gatsby-transformer-javascript-static-exports`](https://www.gatsbyjs.org/packages/gatsby-transformer-javascript-static-exports) | JavaScript ファイルの `exports.data` をコンテンツソースとして抽出するためのプラグインです。 |
| [`gatsby-transformer-json`](https://www.gatsbyjs.org/packages/gatsby-transformer-json) | JSON ファイルをコンテンツソースとしてパースするためのプラグインです。 |
| [`gatsby-transformer-pdf`](https://www.gatsbyjs.org/packages/gatsby-transformer-pdf) | PDF ファイルのテキストデータをコンテンツソースとして抽出するためのプラグインです。 |
| [`gatsby-transformer-react-docgen`](https://www.gatsbyjs.org/packages/gatsby-transformer-react-docgen) | React のコンポーネントの情報を [`react-docgen`](https://github.com/reactjs/react-docgen) を使ってコンテンツソースとして抽出するためのプラグインです。 |
| [`gatsby-transformer-remark`](https://www.gatsbyjs.org/packages/gatsby-transformer-remark) | Markdown ファイルを [`remark`](http://remark.js.org/) を使ってコンテンツソースとしてパースするためのプラグインです。 Gatsby のテキストデータを取得する transformer の中で最も多く使われています。 |
| [`gatsby-transformer-screenshot`](https://www.gatsbyjs.org/packages/gatsby-transformer-screenshot) | AWS Lambda Function を使ってウェブサイトのスクリーンショットを生成するプラグインです。 |
| [`gatsby-transformer-sharp`](https://www.gatsbyjs.org/packages/gatsby-transformer-sharp) | 画像処理ライブラリ [`sharp`](https://github.com/lovell/sharp) を使って画像にリサイズ・切り抜き・レスポンシブ化を施してコンテンツソースとして提供するプラグインです。 |
| [`gatsby-transformer-sqip`](https://www.gatsbyjs.org/packages/gatsby-transformer-sqip) | 非常に軽量なサムネイル画像を生成するプラグインです。 |
| [`gatsby-transformer-toml`](https://www.gatsbyjs.org/packages/gatsby-transformer-toml) | TOML ファイルをコンテンツソースとしてパースするためのプラグインです。 |
| [`gatsby-transformer-xml`](https://www.gatsbyjs.org/packages/gatsby-transformer-xml) | XML ファイルをコンテンツソースとしてパースするためのプラグインです。 |
| [`gatsby-transformer-yaml`](https://www.gatsbyjs.org/packages/gatsby-transformer-yaml) | YAML ファイルをコンテンツソースとしてパースするためのプラグインです。 |

## テーマ

テーマは名前が `gatsby-theme-` で始まります。

| 名前 | 説明 |
| --- | --- |
| [`gatsby-theme-blog-core`](https://www.gatsbyjs.org/packages/gatsby-theme-blog-core) | シンプルなブログ作成用のテーマです。通常は子テーマの `gatsby-theme-blog` を使うことが想定されています。 | [`gatsby-theme-blog`](https://www.gatsbyjs.org/packages/gatsby-theme-blog) | シンプルなブログ作成用のテーマです。 `gatsby-theme-blog-core` を親テーマとして利用しています。 |
| [`gatsby-theme-notes`](https://www.gatsbyjs.org/packages/gatsby-theme-notes) | メモ集サイト用のテーマです。 |
| [`gatsby-theme-ui-preset`](https://www.gatsbyjs.org/packages/gatsby-theme-ui-preset) | 他の公式テーマが使うための Theme UI の設定だけを提供するテーマです（と公式に書かれていますが、他の公式テーマでこれを使っているものは現状無いようです）。 |
