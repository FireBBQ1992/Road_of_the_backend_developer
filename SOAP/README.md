# SOAP
> 基於 XML 的簡易協議，用於 HTTP 上的訊息交換\
> 簡單來說， SAP 是用於訪問網路服務 (Webservice) 的協議

## 預備知識
- XML
- XML 空間命名 

## 何謂 SOAP ?
- 基於 XML
- 獨立於語言
- 獨立於平台
- 簡單且可擴展
- 准許繞過防火牆
- 是一種 *通訊協議*，一種簡易對象的訪問協議
- 應用於程式之間的通訊
- 是一種發消息的格式

## 為何要使用 SOAP ?
> SOAP 提供了一種標準的方法，可讓以下動作相互通訊：
> > - 不同的操作系統 
> > - 不同的技術
> > - 編程語法的應用

## 結構
 > 一則 SOAP 消息就是一個普通的 XML 文檔，須包含以下元素：
 > > - Envelope ：讓 XML 文檔識別為一則 SOAP 消息
 > > - Header : 頭部訊息
 > > - Body : 一些調用或響應訊息
 > > - Fault : 提供有關處理發生的錯誤資訊

 ## 規則
 - 需使用 XML 進行編碼
 -  SOAP 消息<font color=#008000>必須</font>使用 Envelope 命名空間
 -  SOAP 消息<font color=#008000>必須</font>使用 Encoding 命名空間
 -  SOAP 消息<font color=#FF0000>不能</font>包含 DTD 引用
 -  SOAP 消息<font color=#FF0000>不能</font>包含 XML 處理指令

 ### 基本結構
 ```
<?xml version="1.0"?>
<soap:Envelope
xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

<soap:Header>
...
</soap:Header>

<soap:Body>
...
  <soap:Fault>
  ...
  </soap:Fault>
</soap:Body>

</soap:Envelope>
 ```


## SOAP Envelope 元素
> 主要為 SOAP 的 <font color=#00FFFF> 根元素 </font>

例子：
```
<?xml version="1.0"?>
<soap:Envelope
xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">
  ...
  Message information goes here
  ...
</soap:Envelope>
```
### xmlns: SOAP 的命名空間
> SOAP 訊息必須擁有一個與命名空間 "http://www.w3.org/2001/12/soap-envelope" 相關聯的一個 ? Envelope 元素。
如果使用了不同的命名空間，應用程式會發生錯誤，並拋棄此訊息。

### encodingStyle 屬性
> encodingStyle 應用於定義在文檔中使用的數據類型，此屬性可出現在任何SOAP 元素中，應用到元素的內容及元素的所有子元素上

語法
```
soap:encodingStyle="Test for encodingStyle element"
```


## SOAP Header 元素



## SOAP Body 元素

## SOAP Fault 元素



 ## Reference

[runoob-SOAP 教程](https://www.runoob.com/soap/soap-tutorial.html)