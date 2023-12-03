# Internet

## 何謂網路？

- 透過網路介面裝置及傳輸媒介將兩部以上電腦透過一定的方式連接起來，使其能共享資源（比如檔案、程式或是週邊裝置...等） ，互相傳送訊息

## 何謂 ＷＷＷ ？

- 全球資訊網（World Wide Web）是一個透過網際網路訪問的，由許多互相連結的超文字組成的資訊系統
- 全球資訊網並不等於網際網路，全球資訊網只是網際網路所能提供的服務之一

## 何謂 HTTP?

- 超文本傳輸協定（英語：HyperText Transfer Protocol，縮寫：HTTP）是一種用於分佈式、協作式和超媒體訊息系統的應用層協定
- 是全球資訊網的基礎，用於透過超文字連結載入網頁
- HTTP 在應用層協定中，用於在聯網裝置之間傳輸資訊，並在網路通訊協定堆疊的其他層上執行。
- 典型流程涉及用戶端機器向伺服器發出請求，然後伺服器傳送回應訊息。

### HTTP 請求中包含什麼內容？

典型的 HTTP 請求包含以下內容：

#### 1. HTTP 版本類型

#### 2. 一個 URL

#### 3. 一個 HTTP 方法

> 表示 HTTP 請求期待被查詢的伺服器執行的動作, 種最常見的 HTTP 方法是「GET」和「POST」
>
> > GET : 請求期望返傳回資訊（通常以網站的形式）\
> > POST : 請求通常表示用戶端正在向 Web 伺服器提交資訊（例如表單資訊，如提交的使用者名稱和密碼）

#### 4. HTTP 請求標頭

> HTTP 標頭包含存儲在索引鍵/值組中的文字訊息，並且它們包含在每個 HTTP 請求中。這些標頭可傳達核心資訊，如用戶端正在使用什麼瀏覽器以及正在請求什麼資料。

#### 5. 選用的 HTTP 主體

> 請求的主體部分包含請求正在傳輸的資訊的「正文」。HTTP 請求的主體包含提交到網頁伺服器的任何資訊，例如使用者名稱和密碼，或輸入到表單中的任何其他資料。

### HTTP 回應中包含什麼內容？

典型的 HTTP 回應包含以下內容：

#### 1. 一個 HTTP 狀態代碼

> 狀態代碼分為以下 5 個區塊：
>
> > 1xx 資訊內容\
> > 2xx 成功\
> > 3xx 重新導向\
> > 4xx 用戶端錯誤\
> > 5xx 伺服器錯誤\
> > 「xx」是指 00 到 99 之間的不同數字。

#### 2. HTTP 回應標頭

> 與 HTTP 請求非常相似，HTTP 回應也帶有標頭，用於傳達重要的資訊，例如在回應主體中傳送的資料的語言和格式。

#### 3. 選用的 HTTP 主體

> 對「GET」請求的成功 HTTP 回應通常有一個主體，其中包含請求的資訊。在大多數 Web 請求中，這是 HTML 資料，Web 瀏覽器會將其轉譯為網頁。

## 何謂 HTTPS?

- 超文本傳輸安全協定（HyperText Transfer Protocol Secure） 是 HTTP 的安全版本
- HTTP 是用於在 Web 瀏覽器和網站之間傳送資料的主要通訊協定, HTTPS 經過加密，以提高資料傳輸的安全性
- HTML, CSS 及 JavaScript 為傳輸文件的三大要素

## 何謂 DNS？

- 網路名稱系統 (Domain Name Servers), 它是轉換 IP 與 URL 的服務
- 瀏覽器會在取得網站之前，他會去看 DNS 來尋找託管網站的伺服器
- 瀏覽器會向伺服器傳送 http 請求．伺服器就會傳送 200 OK，並開始傳遞給瀏覽器資料封包
- 瀏覽器會將資料封包整合成完整的網站

## 何謂瀏覽器？

- 網頁瀏覽器有兩個主要功能
- 1. 排版引擎(Layout engine)主要將網頁的 HTML 和其他資源和其他資源轉換為用戶設備上和其他資源轉換為用戶設備上的交互式視覺表示
- 2. JavaScript 引擎是專門處理 Javascript 程式碼的虛擬機器

## Reference

[網路基本概要](http://www.greatbooks.com.tw/backend/news/test_pdf/580.pdf)

[全球資訊網定義](https://zh.wikipedia.org/zh-tw/%E4%B8%87%E7%BB%B4%E7%BD%91)

[超文本傳輸協定](https://zh.wikipedia.org/wiki/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE)

[Cloudflare - 什麼是 HTTP？](https://www.cloudflare.com/zh-tw/learning/ddos/glossary/hypertext-transfer-protocol-http/)

[超文本傳輸安全協定](https://zh.wikipedia.org/zh-tw/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%AE%89%E5%85%A8%E5%8D%8F%E8%AE%AE)

[Cloudflare - 什麼是 HTTPS？](https://www.cloudflare.com/zh-tw/learning/ssl/what-is-https/)
