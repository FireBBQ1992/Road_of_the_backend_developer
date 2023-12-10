# HTML

## 何謂 HTML ?

- HTML（HyperText Markup Language，超文本標記語言）是網頁的基石。它表述並定義網頁的內容。
- 「超文本」（HyperText）是指從某個網頁連到其他網頁的連結，不管它連結到站內或站外。藉由撰寫與上載網頁到網際網路中，我們就積極參與了全球資訊網（World Wide Web) 這個資訊系統。
- HTML 使用「標記」（markup）來詮釋文字、圖像、或是其他能在瀏覽器裡面顯示的內容。
- 一個 HTML 標籤包含：

  - 起始標籤(opening tag)：它包含了元素的名字，夾在一對  <、> (brackets)之間。它指明元素從何開始生效。
  - 結束標籤(closing tag)：結束標籤和起始標籤長得差不多，只不過它在名字前面還多加了一條斜線 (forward slash) 。它表示元素結束的地方。忘記加上結束標籤是初學者常犯的錯誤，這將導致奇怪的結果。
  - 內容(content):  元素的內容。
  - 元素(element):  以上三者加起來就是元素。通常我們會說標籤是 HTML element。

## 巢狀元素 Nesting elements

- 你可以把元素放進另一個元素裡面 — 這叫做巢套(nesting)。例如，p tag 內部可放入 strong tag。
  小心注意， 這些元素必須要正確地開啟與關閉，它們與其他元素的內外關係要相當明確。若沒有正確的語法，可能導致網頁瀏覽器將無法解讀，只能盡可能地猜測我們的意思，因此我們很有可能會得到一個不如預期的結果。所以，別這樣做！！

## HTML 常用標籤

### 標題

\<h1> 到 \<h6> 標籤用於定義 HTML 標題

### 段落

\<p> 標籤定義了一個段落。 瀏覽器會自動在每個 \<p> 元素之前和之後添加一個空行

### 超連結

- \<a> 標籤(anchor tag)用於在網頁上創建超鏈接, 此超鏈接用於將網頁鏈接到其他網頁或同一網頁的某些部分。 它用於提供 absolute linking 或 relative linking 作為其“href” (hyptertext reference)值
- \<a>標籤可以設定 target 屬性，來決定新頁面是否會開啟新的瀏覽器分頁
- \<base>標籤來定義所有\<a>標籤的 target。

### 圖片

\<img> 標籤用於在 HTML 頁面中嵌入圖像。src 是圖片來源，alt 是圖片無法顯示時使用的替代文字。

### 列表

- \<ul> 代表無序列表 (unordered list)
- \<ol>代表有序列表 (ordered list)

## 絕對路徑與相對路徑

- 絕對路徑使用完整的 URL 當作連結對象。當我們需要連結到不在我們伺服器內的資源時，就需要使用絕對路徑。
- 相對路徑可以連結到相對於目前文件的檔案。”.”代表目前 html 文件所在資料夾位置，”..” 代表上層的資料夾位置。
- 若使用”/”，則可從 root directory 向下連結。

## Reference

[2023 網頁全端開發](https://www.udemy.com/course/wilson-full-stack-web-development/)
