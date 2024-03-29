# Gatsby 公式のプラグイン・テーマまとめ

![Gatsby](https://raw.githubusercontent.com/gh640/gatsby-plugins-themes-ja/main/assets/gatsbyjs_com.png)

React ベースの静的サイトジェネレーター [Gatsby](https://www.gatsbyjs.com/) が公式に提供するプラグインとテーマについてまとめました。

正確には、公式の monorepo リポジトリ ↓ に含まれているプラグインとテーマの一覧です。

- [gatsby/packages at master · gatsbyjs/gatsby · GitHub](https://github.com/gatsbyjs/gatsby/tree/master/packages)
- [themes/packages at master · gatsbyjs/themes · GitHub](https://github.com/gatsbyjs/themes/tree/master/packages)

対象の Gatsby のバージョンは `gatsby@2` です。

- [プラグイン](#プラグイン)
- [テーマ](#テーマ)

## プラグイン

Gatsby プラグインの名前にはルールがあって、おおよそ次のとおりとなっています。

- `gatsby-source-`: データソースからコンテンツを取得するもの
- `gatsby-transformer-`: 取得したコンテンツをパースしたり変換したりするもの
- `gatsby-plugin-`: その他の機能を提供するプラグイン

また、 `gatsby-transformer-remark` のサブプラグインの先頭は `gatsby-remark-` になっています。

| 名前 | 説明 |
| --- | --- |
| [`gatsby-plugin-canonical-urls`](https://www.gatsbyjs.com/plugins/gatsby-plugin-canonical-urls) | HTML の `<head>` 内に `canonical` リンクを追加するためにプラグインです。 |
| [`gatsby-plugin-catch-links`](https://www.gatsbyjs.com/plugins/gatsby-plugin-catch-links) | `gatsby-link` を使わずに作られたサイト内リンクに `gatsby-link` の挙動を反映するためのプラグインです。 Markdown ファイルの中でサイト内リンクを使っているとき等に便利です。 |
| [`gatsby-plugin-coffeescript`](https://www.gatsbyjs.com/plugins/gatsby-plugin-coffeescript) | CoffeeScript と CJSX を利用するためのプラグインです。 |
| [`gatsby-plugin-create-client-paths`](https://www.gatsbyjs.com/plugins/gatsby-plugin-create-client-paths) | 動的に動くパスを持った、動的と静的のハイブリッドな Gatsby アプリを作るためのプラグインです。 |
| [`gatsby-plugin-cxs`](https://www.gatsbyjs.com/plugins/gatsby-plugin-cxs) | css-in-js の [cxs](https://github.com/cxs-css/cxs) を利用するためのプラグインです。 |
| [`gatsby-plugin-emotion`](https://www.gatsbyjs.com/plugins/gatsby-plugin-emotion) | css-in-js の [Emotion](https://github.com/emotion-js/emotion)　を利用するためのプラグインです。 |
| [`gatsby-plugin-facebook-analytics`](https://www.gatsbyjs.com/plugins/gatsby-plugin-facebook-analytics) | [Facebook Analytics](https://analytics.facebook.com/) を利用するためのプラグインです。 |
| [`gatsby-plugin-feed`](https://www.gatsbyjs.com/plugins/gatsby-plugin-feed) | RSS フィードを生成するためのプラグインです。 |
| [`gatsby-plugin-flow`](https://www.gatsbyjs.com/plugins/gatsby-plugin-flow) | Flow を利用するためのプラグインです。 |
| [`gatsby-plugin-fullstory`](https://www.gatsbyjs.com/plugins/gatsby-plugin-fullstory) | 解析サービスの [Fullstory](https://www.fullstory.com/) を利用するためのプラグインです。 |
| [`gatsby-plugin-gatsby-cloud`](https://www.gatsbyjs.com/plugins/gatsby-plugin-gatsby-cloud) | Gatsby Cloud 用のプラグインです。 HTTP ヘッダーの追加や `_headers.json` ・ `_redirects.json` ファイルの生成を行います。 |
| [`gatsby-plugin-glamor`](https://www.gatsbyjs.com/plugins/gatsby-plugin-glamor) | css-in-js の [Glamor](https://github.com/threepointone/glamor)を利用するためのプラグインです。 |
| [`gatsby-plugin-google-analytics`](https://www.gatsbyjs.com/plugins/gatsby-plugin-google-analytics) | Google Analytics を利用するためのプラグインです。 |
| [`gatsby-plugin-google-gtag`](https://www.gatsbyjs.com/plugins/gatsby-plugin-google-gtag) | Google global site tag （ `gtag.js` ）を利用するためのプラグインです。 |
| [`gatsby-plugin-google-tagmanager`](https://www.gatsbyjs.com/plugins/gatsby-plugin-google-tagmanager) | Google Tag Manager を利用するためのプラグインです。 |
| [`gatsby-plugin-graphql-config`](https://www.gatsbyjs.com/plugins/gatsby-plugin-graphql-config) | ESLint や IDE などで利用できるように、 Gatsby GraphQL のスキーマやフラグメントや GraphQL Config ファイルを `.cache` ディレクトリに保存します。 |
| [`gatsby-plugin-guess-js`](https://www.gatsbyjs.com/plugins/gatsby-plugin-guess-js) | [Guess.js](https://github.com/guess-js/guess) を利用するためのプラグインです。 |
| [`gatsby-plugin-image`](https://www.gatsbyjs.com/plugins/gatsby-plugin-image) | サイトのパフォーマンス向上のために、ページの埋め込み画像の最適化（複数のサイズ・フォーマットの画像の生成）を行います。公式サイトでは [Gatsby Image Plugin](https://www.gatsbyjs.com/docs/reference/built-in-components/gatsby-plugin-image/) と呼ばれています。前身は `gatsby-image` というパッケージで、 Gatby の v2.26 で β 版が導入され v3.0 で正式導入されました。 |
| [`gatsby-plugin-jss`](https://www.gatsbyjs.com/plugins/gatsby-plugin-jss) | css-in-js の [JSS](https://github.com/cssinjs/react-jss) を利用するためのプラグインです。 |
| [`gatsby-plugin-layout`](https://www.gatsbyjs.com/plugins/gatsby-plugin-layout) | ページをまたがって存在するレイアウトコンポーネントを追加するためのプラグインです。 `gatsby@2` で Gatsby 本体から削除された `gatsby@1` のレイアウトコンポーネントを実装するものです。 |
| [`gatsby-plugin-less`](https://www.gatsbyjs.com/plugins/gatsby-plugin-less) | CSS を拡張した [LESS](http://lesscss.org/) を利用するためのプラグインです。 |
| [`gatsby-plugin-lodash`](https://www.gatsbyjs.com/plugins/gatsby-plugin-lodash) | Lodash を利用するための Webpack と Babel のプラグインを提供します。 |
| [`gatsby-plugin-manifest`](https://www.gatsbyjs.com/plugins/gatsby-plugin-manifest) | PWA 仕様を満たすのに必要な web app manifest （ `manifest.webmanifest` ）をサポートするためのプラグインです。 manifest の生成の他に、複数のサイズのアイコンの生成、 favicon 追加等の機能も備えています。 `gatsby-plugin-offline` と併用することが推奨されています。 |
| [`gatsby-plugin-mdx`](https://www.gatsbyjs.com/plugins/gatsby-plugin-mdx) | [MDX](https://mdxjs.com/) を利用するためのプラグインです。 MDX は JSX の中に Markdown が書けるフォーマットです。 |
| [`gatsby-plugin-netlify-cms`](https://www.gatsbyjs.com/plugins/gatsby-plugin-netlify-cms) | [Netlify CMS](https://www.netlifycms.org/) を利用するためのプラグインです。パス `admin/index.html` に Netlify CMS を生成します。 |
| [`gatsby-plugin-netlify`](https://www.gatsbyjs.com/plugins/gatsby-plugin-netlify) | Netlify に対応するためのプラグインです。デフォルトでは、 Netlify のヘッダーとリダイレクトの設定のために `_headers` と `_redirects` という 2 つのファイルを public フォルダのルートに設置します。 |
| [`gatsby-plugin-no-sourcemaps`](https://www.gatsbyjs.com/plugins/gatsby-plugin-no-sourcemaps) | ソースマップを生成しないようにするためのプラグインです。 Webpack の設定のためのほんの数行のコードからなるプラグインです。 |
| [`gatsby-plugin-nprogress`](https://www.gatsbyjs.com/plugins/gatsby-plugin-nprogress) | [Nprogress.js](http://ricostacruz.com/nprogress/) を利用するためのプラグインです。 |
| [`gatsby-plugin-offline`](https://www.gatsbyjs.com/plugins/gatsby-plugin-offline) | ネットワーク環境が悪い場合でもサイトがなるべく動くようにするためのプラグインです。 Service Worker を追加します。 `gatsby-plugin-manifest` と併用することが推奨されています。 |
| [`gatsby-plugin-page-creator`](https://www.gatsbyjs.com/plugins/gatsby-plugin-page-creator) | 指定されたパスの下の React コンポーネントを含むファイルからページを自動生成するためのプラグインです。 Gatsby 本体が利用しており、デフォルトでは `src/pages` 以下のファイルが対象になっています。 |
[`gatsby-plugin-postcss`](https://www.gatsbyjs.com/plugins/gatsby-plugin-postcss) | [PostCSS](https://postcss.org/) を利用するためのプラグインです。 |
| [`gatsby-plugin-preact`](https://www.gatsbyjs.com/plugins/gatsby-plugin-preact) | React の軽量版である [Preact](https://preactjs.com/) を利用するためのプラグインです。 |
| [`gatsby-plugin-preload-fonts`](https://www.gatsbyjs.com/plugins/gatsby-plugin-preload-fonts) | パフォーマンス改善のために、ページで使われているフォントを `<link rel="preload">` で先読みするためのプラグインです。 |
| [`gatsby-plugin-react-css-modules`](https://www.gatsbyjs.com/plugins/gatsby-plugin-react-css-modules) | React コンポーネント内の `styleName` を `className` に変換するプラグインです。 Gatsby は CSS モジュールをデフォルトでサポートしているため、このプラグインは通常必要ありません。 |
| [`gatsby-plugin-react-helmet`](https://www.gatsbyjs.com/plugins/gatsby-plugin-react-helmet) | [React Helmet](https://github.com/nfl/react-helmet) を利用するためのプラグインです。 HTML の `<head>` タグ内に `<title>` や `<meta>` 等のタグがかんたんに追加できます。 |
| [`gatsby-plugin-remove-trailing-slashes`](https://www.gatsbyjs.com/plugins/gatsby-plugin-remove-trailing-slashes) | パスの末尾の `/` （スラッシュ）を削除するためのプラグインです。 **Gatsby v4.7 で本体に同じ機能が追加されたため本プラグインは deprecated となりました** （ [参考 1](https://www.gatsbyjs.com/docs/reference/config-files/gatsby-config/#trailingslash) [参考 2](https://www.gatsbyjs.com/docs/reference/release-notes/v4.7/#trailingslash-option) ）。 |
| [`gatsby-plugin-sass`](https://www.gatsbyjs.com/plugins/gatsby-plugin-sass) | Sass/SCSS を利用するためのプラグインです。 |
| [`gatsby-plugin-schema-snapshot`](https://www.gatsbyjs.com/plugins/gatsby-plugin-schema-snapshot) | GraphQL のスキーマのスナップショットファイルを生成するためのプラグインです。デフォルトで `schema.gql` という名前のファイルに出力します。 |
| [`gatsby-plugin-sharp`](https://www.gatsbyjs.com/plugins/gatsby-plugin-sharp) | 画像処理ライブラリの sharp を利用するためのプラグインです。画像をレスポンシブ化する際によく利用されます。 |
| [`gatsby-plugin-sitemap`](https://www.gatsbyjs.com/plugins/gatsby-plugin-sitemap) | マシン向けのサイトマップ（ `sitemap.xml` ）を生成するためのプラグインです。 |
| [`gatsby-plugin-styled-components`](https://www.gatsbyjs.com/plugins/gatsby-plugin-styled-components) | [`styled-components`](https://github.com/styled-components/styled-components) を利用するためのプラグインです。 |
| [`gatsby-plugin-styled-jsx`](https://www.gatsbyjs.com/plugins/gatsby-plugin-styled-jsx) | [`styled-jsx`](https://github.com/vercel/styled-jsx) を利用するためのプラグインです。 |
| [`gatsby-plugin-styletron`](https://www.gatsbyjs.com/plugins/gatsby-plugin-styletron) | [Styletron](https://github.com/styletron/styletron) を利用するためのプラグインです。 |
| [`gatsby-plugin-stylus`](https://www.gatsbyjs.com/plugins/gatsby-plugin-stylus) | [Stylus](https://www.stylus.com/) を利用するためのプラグインです。 |
| [`gatsby-plugin-subfont`](https://www.gatsbyjs.com/plugins/gatsby-plugin-subfont) | Google fonts 等のウェブフォントの配信を最適化するためのライブラリ [Subfont](https://github.com/Munter/subfont#readme) を利用するためのプラグインです。 |
| [`gatsby-plugin-twitter`](https://www.gatsbyjs.com/plugins/gatsby-plugin-twitter) | Twitter のツイートやタイムラインやシェアボタンをページに埋め込むためのプラグインです。 |
| [`gatsby-plugin-typescript`](https://www.gatsbyjs.com/plugins/gatsby-plugin-typescript) | TypeScript を利用するためのプラグインです。 Gatsby 本体が利用しています。 |
| [`gatsby-plugin-typography`](https://www.gatsbyjs.com/plugins/gatsby-plugin-typography) | タイポグラフィー・フォント周りの設定を行うための [Typography](https://kyleamathews.github.io/typography.js/) を利用するためのプラグインです。 |
| [`gatsby-remark-autolink-headers`](https://www.gatsbyjs.com/plugins/gatsby-remark-autolink-headers) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内の各見出し（ `h1` - `h6` ）にリンク付きのアイコンを付けられるプラグインです（ GitHub の README にあるようなものです）。 |
| [`gatsby-remark-code-repls`](https://www.gatsbyjs.com/plugins/gatsby-remark-code-repls) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内でウェブ上で JS コードを試せる Codepen 等のサービスへのリンクを生成できるプラグインです。 |
| [`gatsby-remark-copy-linked-files`](https://www.gatsbyjs.com/plugins/gatsby-remark-copy-linked-files) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内でリンクで参照されているファイルを public フォルダにコピーするプラグインです。 |
| [`gatsby-remark-custom-blocks`](https://www.gatsbyjs.com/plugins/gatsby-remark-custom-blocks) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内で使えるカスタムブロックを定義して利用できるプラグインです。 [`remark-custom-blocks`](https://github.com/zestedesavoir/zmarkdown/tree/master/packages/remark-custom-blocks) を使用します。 |
| [`gatsby-remark-embed-snippet`](https://www.gatsbyjs.com/plugins/gatsby-remark-embed-snippet) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内でファイルの中身をコードスニペットとして埋め込めるプラグインです。動作には `gatsby-remark-prismjs` が必要です。 |
| [`gatsby-remark-graphviz`](https://www.gatsbyjs.com/plugins/gatsby-remark-graphviz) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内の [Graphviz](https://www.graphviz.org/) のコードブロックを SVG 画像に変換してくれるプラグインです。しかし、このプラグインが利用する [Viz.js](https://github.com/mdaines/viz.js/) の開発が終了しています。 |
| [`gatsby-remark-images`](https://www.gatsbyjs.com/plugins/gatsby-remark-images) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内の画像をレスポンシブ化するためのプラグインです。 `png` と `jpg` をサポートしています。 |
| [`gatsby-remark-images-contentful`](https://www.gatsbyjs.com/plugins/gatsby-remark-images-contentful) | `gatsby-transformer-remark` のサブプラグインで、 Contentful の Image API を使って Markdown 内の画像をレスポンシブ化するためのプラグインです。 |
| [`gatsby-remark-katex`](https://www.gatsbyjs.com/plugins/gatsby-remark-katex) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内に数式を書くためのプラグインです。 |
| [`gatsby-remark-prismjs`](https://www.gatsbyjs.com/plugins/gatsby-remark-prismjs) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内のコードブロックにシンタックスハイライトを追加できるプラグインです。シンタックスハイライト用のライブラリ [Prism](https://prismjs.com/) を使用します。 |
| [`gatsby-remark-responsive-iframe`](https://www.gatsbyjs.com/plugins/gatsby-remark-responsive-iframe) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内の `<iframe>` タグの縦横比を維持するためのプラグインです。 |
| [`gatsby-remark-smartypants`](https://www.gatsbyjs.com/plugins/gatsby-remark-smartypants) | `gatsby-transformer-remark` のサブプラグインで、 Markdown 内のアルファベットの句読点をきれいな形に変換してくれるプラグインです。 |
| [`gatsby-source-contentful`](https://www.gatsbyjs.com/plugins/gatsby-source-contentful) | ヘッドレス CMS （ API ファースト CMS ）の [Contentful](https://www.contentful.com/) からコンテンツデータを取得するためのプラグインです。 |
| [`gatsby-source-drupal`](https://www.gatsbyjs.com/plugins/gatsby-source-drupal) | CMS Drupal からコンテンツデータを取得するためのプラグインです。 |
| [`gatsby-source-faker`](https://www.gatsbyjs.com/plugins/gatsby-source-faker) | フェイクデータ（テストや検証のためのデータ）を生成するライブラリ [`faker.js`](https://github.com/marak/Faker.js/) を使ってフェイクコンテンツを取得するためのプラグインです。 |
| [`gatsby-source-filesystem`](https://www.gatsbyjs.com/plugins/gatsby-source-filesystem) | ローカルのファイルシステムからコンテンツデータを取得するためのプラグインです。 |
| [`gatsby-source-graphql`](https://www.gatsbyjs.com/plugins/gatsby-source-graphql) | 任意の GraphQL API からデータを取得するためのプラグインです。 |
| [`gatsby-source-hacker-news`](https://www.gatsbyjs.com/plugins/gatsby-source-hacker-news) | [Hacker News API](https://github.com/HackerNews/API) からコンテンツデータを取得するためのプラグインです。 |
| [`gatsby-source-lever`](https://www.gatsbyjs.com/plugins/gatsby-source-lever) | リクルーティング活動支援のウェブサービス [Lever](https://www.lever.co/) からデータを取得するためのプラグインです。 |
| [`gatsby-source-medium`](https://www.gatsbyjs.com/plugins/gatsby-source-medium) | Medium の非公式の JSON エンドポイントからコンテンツデータを取得するためのプラグインです。ただし取得できる内容・件数がかぎられています。 |
| [`gatsby-source-mongodb`](https://www.gatsbyjs.com/plugins/gatsby-source-mongodb) | MongoDB のコレクションからデータを取得するためのプラグインです。 |
| [`gatsby-source-npm-package-search`](https://www.gatsbyjs.com/plugins/gatsby-source-npm-package-search) | Yarn の Algolia の機能を使って npm のパッケージ情報を取得するためのプラグインです。 |
| [`gatsby-source-shopify`](https://www.gatsbyjs.com/plugins/gatsby-source-shopify) | EC サービス [Shopify](https://www.shopify.com/) のストアから Shopify Storefront API を使ってデータを取得するためのプラグインです。 |
| [`gatsby-source-wikipedia`](https://www.gatsbyjs.com/plugins/gatsby-source-wikipedia) | Wikipedia から記事データを取得するためのプラグインです。 |
| [`gatsby-source-wordpress`](https://www.gatsbyjs.com/plugins/gatsby-source-wordpress) | WordPress サイトから WordPress REST API を使ってコンテンツデータを取得するためのプラグインです。 |
| [`gatsby-transformer-asciidoc`](https://www.gatsbyjs.com/plugins/gatsby-transformer-asciidoc) | AsciiDoc ファイルをコンテンツソースとしてパースするためのプラグインです。 |
| [`gatsby-transformer-csv`](https://www.gatsbyjs.com/plugins/gatsby-transformer-csv) | CSV ファイルをコンテンツソースとしてパースするためのプラグインです。 |
| [`gatsby-transformer-documentationjs`](https://www.gatsbyjs.com/plugins/gatsby-transformer-documentationjs) | JavaScript のコードから JSDoc のデータを抽出するためのプラグインです。 |
| [`gatsby-transformer-excel`](https://www.gatsbyjs.com/plugins/gatsby-transformer-excel) | Excel ファイルをコンテンツソースとしてパースするためのプラグインです。 |
| [`gatsby-transformer-hjson`](https://www.gatsbyjs.com/plugins/gatsby-transformer-hjson) | Hjson ファイルをコンテンツソースとしてパースするためのプラグインです。 |
| [`gatsby-transformer-javascript-frontmatter`](https://www.gatsbyjs.com/plugins/gatsby-transformer-javascript-frontmatter) | JavaScript ファイルの `exports.frontmatter` をコンテンツソースとして抽出するためのプラグインです。 |
| [`gatsby-transformer-javascript-static-exports`](https://www.gatsbyjs.com/plugins/gatsby-transformer-javascript-static-exports) | JavaScript ファイルの `exports.data` をコンテンツソースとして抽出するためのプラグインです。 |
| [`gatsby-transformer-json`](https://www.gatsbyjs.com/plugins/gatsby-transformer-json) | JSON ファイルをコンテンツソースとしてパースするためのプラグインです。 |
| [`gatsby-transformer-pdf`](https://www.gatsbyjs.com/plugins/gatsby-transformer-pdf) | PDF ファイルのテキストデータをコンテンツソースとして抽出するためのプラグインです。 |
| [`gatsby-transformer-react-docgen`](https://www.gatsbyjs.com/plugins/gatsby-transformer-react-docgen) | React のコンポーネントの情報を [`react-docgen`](https://github.com/reactjs/react-docgen) を使ってコンテンツソースとして抽出するためのプラグインです。 |
| [`gatsby-transformer-remark`](https://www.gatsbyjs.com/plugins/gatsby-transformer-remark) | Markdown ファイルを [`remark`](http://remark.js.org/) を使ってコンテンツソースとしてパースするためのプラグインです。 Gatsby のテキストデータを取得する transformer の中で最も多く使われています。 |
| [`gatsby-transformer-screenshot`](https://www.gatsbyjs.com/plugins/gatsby-transformer-screenshot) | AWS Lambda Function を使ってウェブサイトのスクリーンショットを生成するプラグインです。 |
| [`gatsby-transformer-sharp`](https://www.gatsbyjs.com/plugins/gatsby-transformer-sharp) | 画像処理ライブラリ [`sharp`](https://github.com/lovell/sharp) を使って画像にリサイズ・切り抜き・レスポンシブ化を施してコンテンツソースとして提供するプラグインです。 |
| [`gatsby-transformer-sqip`](https://www.gatsbyjs.com/plugins/gatsby-transformer-sqip) | 非常に軽量なサムネイル画像を生成するプラグインです。 |
| [`gatsby-transformer-toml`](https://www.gatsbyjs.com/plugins/gatsby-transformer-toml) | TOML ファイルをコンテンツソースとしてパースするためのプラグインです。 |
| [`gatsby-transformer-xml`](https://www.gatsbyjs.com/plugins/gatsby-transformer-xml) | XML ファイルをコンテンツソースとしてパースするためのプラグインです。 |
| [`gatsby-transformer-yaml`](https://www.gatsbyjs.com/plugins/gatsby-transformer-yaml) | YAML ファイルをコンテンツソースとしてパースするためのプラグインです。 |

## テーマ

テーマは名前が `gatsby-theme-` で始まります。

| 名前 | 説明 |
| --- | --- |
| [`gatsby-theme-blog`](https://www.gatsbyjs.com/plugins/gatsby-theme-blog) | シンプルなブログ作成用のテーマです。 `gatsby-theme-blog-core` を親テーマとして利用しています。 |
| [`gatsby-theme-blog-core`](https://www.gatsbyjs.com/plugins/gatsby-theme-blog-core) | シンプルなブログ作成用のテーマです。通常は子テーマの `gatsby-theme-blog` を使うことが想定されています。 |
| [`gatsby-theme-blog-darkmode`](https://www.gatsbyjs.com/plugins/gatsby-theme-blog-darkmode) | `gatsby-theme-blog` にダークモード機能を追加できるテーマです。利用するときには `gatsby-theme-blog` といっしょに利用する必要があります。 |
| [`gatsby-theme-i18n`](https://www.gatsbyjs.com/plugins/gatsby-theme-i18n) | Gatsby サイトを多言語対応（ i18n support ）させるためのテーマです。 |
| [`gatsby-theme-i18n-lingui`](https://www.gatsbyjs.com/plugins/gatsby-theme-i18n-lingui) | 多言語対応サイトを [LinguiJS](https://lingui.js.org/) で各言語に翻訳（ l10n ）するためのテーマです。 |
| [`gatsby-theme-i18n-react-i18next`](https://www.gatsbyjs.com/plugins/gatsby-theme-i18n-react-i18next) | 多言語対応サイトを [`readct-i18next`](https://react.i18next.com/) で各言語に翻訳（ l10n ）するためのテーマです。 |
| [`gatsby-theme-i18n-react-intl`](https://www.gatsbyjs.com/plugins/gatsby-theme-i18n-react-intl) | 多言語対応サイトを [React Intl](https://formatjs.io/docs/react-intl/) で各言語に翻訳（ l10n ）するためのテーマです。 |
| [`gatsby-theme-notes`](https://www.gatsbyjs.com/plugins/gatsby-theme-notes) | メモ集サイト用のテーマです。 |
| [`gatsby-theme-ui-preset`](https://www.gatsbyjs.com/plugins/gatsby-theme-ui-preset) | 他の公式テーマが使うための Theme UI の設定だけを提供するテーマです（と公式に書かれていますが、他の公式テーマでこれを使っているものは現状無いようです）。 |
