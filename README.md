# Gatsby 公式のプラグイン・テーマまとめ

静的サイトジェネレータ（ SSG ）である Gatsby が公式に提供するプラグインとテーマの一覧です。

正確には「公式の monorepo リポジトリに含まれているプラグインとテーマ」の一覧です。

- [gatsby/packages at master · gatsbyjs/gatsby · GitHub](https://github.com/gatsbyjs/gatsby/tree/master/packages)

対象の Gatsby のバージョンは `gatsby@2` です。

- プラグイン
- テーマ

## プラグイン

| 名前 | 説明 |
| --- | --- |
gatsby-plugin-canonical-urls
| HTML の `<head>` 内に `canonical` リンクを追加するためにプラグインです。 |
gatsby-plugin-catch-links
| `gatsby-link` を使わずに作られたサイト内リンクに `gatsby-link` の挙動を反映するためのプラグインです。 Markdown ファイルの中でサイト内リンクを使っているとき等に便利です。 |
gatsby-plugin-coffeescript
| CoffeeScript と CJSX を利用するためのプラグインです。 |
gatsby-plugin-create-client-paths
| 動的に動くパスを持った、動的と静的のハイブリッドな Gatsby アプリを作るためのプラグインです。 |
gatsby-plugin-cxs
| css-in-js の [cxs](https://github.com/cxs-css/cxs) を利用するためのプラグインです。 |
gatsby-plugin-emotion
| css-in-js の [Emotion](https://github.com/emotion-js/emotion)　を利用するためのプラグインです。 |
gatsby-plugin-facebook-analytics
| [Facebook Analytics](https://analytics.facebook.com/) を利用するためのプラグインです。 |
gatsby-plugin-feed
| RSS フィードを生成するためのプラグインです。 |
gatsby-plugin-flow
| Flow を利用するためのプラグインです。 |
gatsby-plugin-fullstory
| 解析サービスの [Fullstory](https://www.fullstory.com/) を利用するためのプラグインです。 |
gatsby-plugin-glamor
| css-in-js の [Glamor](https://github.com/threepointone/glamor)を利用するためのプラグインです。 |
gatsby-plugin-google-analytics
| Google Analytics を利用するためのプラグインです。 |
gatsby-plugin-google-gtag
| Google global site tag （ `gtag.js` ）を利用するためのプラグインです。 |
gatsby-plugin-google-tagmanager
| Google Tag Manager を利用するためのプラグインです。 |
gatsby-plugin-guess-js
| [Guess.js](https://github.com/guess-js/guess) を利用するためのプラグインです。 |
gatsby-plugin-jss
| css-in-js の [JSS](https://github.com/cssinjs/react-jss) を利用するためのプラグインです。 |
gatsby-plugin-layout
| ページをまたがって存在するレイアウトコンポーネントを追加するためのプラグインです。 `gatsby@2` で Gatsby 本体から削除された `gatsby@1` のレイアウトコンポーネントを実装するものです。 |
gatsby-plugin-less
| CSS を拡張した [LESS](http://lesscss.org/) を利用するためのプラグインです。 |
gatsby-plugin-lodash
| Lodash を利用するための Webpack と Babel のプラグインを提供します。 |
gatsby-plugin-manifest
| PWA 仕様を満たすのに必要な web app manifest （ `manifest.webmanifest` ）をサポートするためのプラグインです。 manifest の生成の他に、複数のサイズのアイコンの生成、 favicon 追加等の機能も備えています。 `gatsby-plugin-offline` と併用することが推奨されています。 |
gatsby-plugin-mdx
| [MDX](https://mdxjs.com/) を利用するためのプラグインです。 MDX は JSX の中に Markdown が書けるフォーマットです。 |
gatsby-plugin-netlify-cms
| [Netlify CMS](https://www.netlifycms.org/) を利用するためのプラグインです。パス `admin/index.html` に Netlify CMS を生成します。 |
gatsby-plugin-netlify
| Netlify に対応するためのプラグインです。デフォルトでは、 Netlify のヘッダーとリダイレクトの設定のために `_headers` と `_redirects` という 2 つのファイルを public フォルダのルートに設置します。 |
gatsby-plugin-no-sourcemaps
| ソースマップを生成しないようにするためのプラグインです。 Webpack の設定のためのほんの数行のコードからなるプラグインです。 |
gatsby-plugin-nprogress
| [Nprogress.js](http://ricostacruz.com/nprogress/) を利用するためのプラグインです。 |
gatsby-plugin-offline
| ネットワーク環境が悪い場合でもサイトがなるべく動くようにするためのプラグインです。 Service Worker を追加します。 `gatsby-plugin-manifest` と併用することが推奨されています。 |
gatsby-plugin-page-creator
| 指定されたパスの下の React コンポーネントを含むファイルからページを自動生成するためのプラグインです。 Gatsby 本体が利用しており、デフォルトでは `src/pages` 以下のファイルが対象になっています。 | gatsby-plugin-postcss
| [PostCSS](https://postcss.org/) を利用するためのプラグインです。 |
gatsby-plugin-preact
| React の軽量版である [Preact](https://preactjs.com/) を利用するためのプラグインです。 |
gatsby-plugin-preload-fonts
| パフォーマンス改善のために、ページで使われているフォントを `<link rel="preload">` で先読みするためのプラグインです。 |
gatsby-plugin-react-css-modules
| React コンポーネント内の `styleName` を `className` に変換するプラグインです。 Gatsby は CSS モジュールをデフォルトでサポートしているため、このプラグインは通常必要ありません。 |
gatsby-plugin-react-helmet
| [React Helmet](https://github.com/nfl/react-helmet) を利用するためのプラグインです。 HTML の `<head>` タグ内に `<title>` や `<meta>` 等のタグがかんたんに追加できます。 |
gatsby-plugin-remove-trailing-slashes
| パスの末尾の `/` （スラッシュ）を削除するためのプラグインです。 |
gatsby-plugin-sass
| Sass/SCSS を利用するためのプラグインです。 |
gatsby-plugin-schema-snapshot
| GraphQL のスキーマのスナップショットファイルを生成するためのプラグインです。デフォルトで `schema.gql` という名前のファイルに出力します。 |
gatsby-plugin-sharp
| 画像処理ライブラリの sharp を利用するためのプラグインです。画像をレスポンシブ化する際によく利用されます。 |
gatsby-plugin-sitemap
| マシン向けのサイトマップ（ `sitemap.xml` ）を生成するためのプラグインです。 |
gatsby-plugin-styled-components
| [`styled-components`](https://github.com/styled-components/styled-components) を利用するためのプラグインです。 |
gatsby-plugin-styled-jsx
| [`styled-jsx`](https://github.com/vercel/styled-jsx) を利用するためのプラグインです。 |
gatsby-plugin-styletron
| [Styletron](https://github.com/styletron/styletron) を利用するためのプラグインです。 |
gatsby-plugin-stylus
| [Stylus](https://www.stylus.com/) を利用するためのプラグインです。 |
gatsby-plugin-subfont
| Google fonts 等のウェブフォントの配信を最適化するためのライブラリ [Subfont](https://github.com/Munter/subfont#readme) を利用するためのプラグインです。 |
gatsby-plugin-twitter
| Twitter のツイートやタイムラインやシェアボタンをページに埋め込むためのプラグインです。 |
gatsby-plugin-typescript
| TypeScript を利用するためのプラグインです。 Gatsby 本体が利用しています。 |
gatsby-plugin-typography
| タイポグラフィー・フォント周りの設定を行うための [Typography](https://kyleamathews.github.io/typography.js/) を利用するためのプラグインです。 |
gatsby-remark-autolink-headers
| `gatsby-transformer-remark` のサブプラグインで、 Markdown 内の各見出し（ `h1` - `h6` ）にリンク付きのアイコンを付けられるプラグインです（ GitHub の README にあるようなものです）。 |
gatsby-remark-code-repls
| `gatsby-transformer-remark` のサブプラグインで、 Markdown 内でウェブ上で JS コードを試せる Codepen 等のサービスへのリンクを生成できるプラグインです。 |
gatsby-remark-copy-linked-files
| `gatsby-transformer-remark` のサブプラグインで、 Markdown 内でリンクで参照されているファイルを public フォルダにコピーするプラグインです。 |
gatsby-remark-custom-blocks
| `gatsby-transformer-remark` のサブプラグインで、 Markdown 内で使えるカスタムブロックを定義して利用できるプラグインです。 [`remark-custom-blocks`](https://github.com/zestedesavoir/zmarkdown/tree/master/packages/remark-custom-blocks) を使用します。 |
gatsby-remark-embed-snippet
| `gatsby-transformer-remark` のサブプラグインで、 Markdown 内でファイルの中身をコードスニペットとして埋め込めるプラグインです。動作には `gatsby-remark-prismjs` が必要です。 |
gatsby-remark-graphviz
| `gatsby-transformer-remark` のサブプラグインで、 Markdown 内の [Graphviz](https://www.graphviz.org/) のコードブロックを SVG 画像に変換してくれるプラグインです。しかし、このプラグインが利用する [Viz.js](https://github.com/mdaines/viz.js/) の開発が終了しています。 |
gatsby-remark-images-contentful
| `gatsby-transformer-remark` のサブプラグインで、 Contentful の Image API を使って Markdown 内の画像をレスポンシブ化するためのプラグインです。 |
gatsby-remark-images
| `gatsby-transformer-remark` のサブプラグインで、 Markdown 内の画像をレスポンシブ化するためのプラグインです。 |
gatsby-remark-katex
| `gatsby-transformer-remark` のサブプラグインで、 Markdown 内に数式を書くためのプラグインです。 |
gatsby-remark-prismjs
| `gatsby-transformer-remark` のサブプラグインで、 Markdown 内のコードブロックにシンタックスハイライトを追加できるプラグインです。シンタックスハイライト用のライブラリ [Prism](https://prismjs.com/) を使用します。 |
gatsby-remark-responsive-iframe
| `gatsby-transformer-remark` のサブプラグインで、 Markdown 内の `<iframe>` タグの縦横比を維持するためのプラグインです。 |
gatsby-remark-smartypants
| `gatsby-transformer-remark` のサブプラグインで、 Markdown 内のアルファベットの句読点をきれいな形に変換してくれるプラグインです。 |
gatsby-source-contentful
|
|
gatsby-source-drupal
|
|
gatsby-source-faker
|
|
gatsby-source-filesystem
|
|
gatsby-source-graphql
|
|
gatsby-source-hacker-news
|
|
gatsby-source-lever
|
|
gatsby-source-medium
|
|
gatsby-source-mongodb
|
|
gatsby-source-npm-package-search
|
|
gatsby-source-shopify
|
|
gatsby-source-wikipedia
|
|
gatsby-source-wordpress
|
|
gatsby-transformer-asciidoc
|
|
gatsby-transformer-csv
|
|
gatsby-transformer-documentationjs
|
|
gatsby-transformer-excel
|
|
gatsby-transformer-hjson
|
|
gatsby-transformer-javascript-frontmatter
|
|
gatsby-transformer-javascript-static-exports
|
|
gatsby-transformer-json
|
|
gatsby-transformer-pdf
|
|
gatsby-transformer-react-docgen
|
|
gatsby-transformer-remark
|
|
gatsby-transformer-screenshot
|
|
gatsby-transformer-sharp
|
|
gatsby-transformer-sqip
|
|
gatsby-transformer-toml
|
|
gatsby-transformer-xml
|
|
gatsby-transformer-yaml
|
|

## テーマ

| 名前 | 説明 |
| --- | --- |
| [`gatsby-theme-blog-core`](https://www.gatsbyjs.org/packages/gatsby-theme-blog-core) | シンプルなブログ作成用のテーマです。通常は子テーマの `gatsby-theme-blog` を使うことが想定されています。 | [`gatsby-theme-blog`](https://www.gatsbyjs.org/packages/gatsby-theme-blog) | シンプルなブログ作成用のテーマです。 `gatsby-theme-blog-core` を親テーマとして利用しています。 |
| [`gatsby-theme-notes`](https://www.gatsbyjs.org/packages/gatsby-theme-notes) | メモ集サイト用のテーマです。 |
| [`gatsby-theme-ui-preset`](https://www.gatsbyjs.org/packages/gatsby-theme-ui-preset) | 他の公式テーマが使うための Theme UI の設定だけを提供するテーマです（と公式に書かれていますが、他の公式テーマでこれを使っているものは現状無いようです）。 |
