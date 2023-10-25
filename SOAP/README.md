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
> 可選的 SOAP Header 元素包含關於應用專用的訊息(例：認證、支付...等)
例子
```
<?xml version="1.0"?>
<soap:Envelope
xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

<soap:Header>
  <m:Trans xmlns:m="http://www.w3schools.com/transaction/"
  soap:mustUnderstand="1">234
  </m:Trans>
</soap:Header>
...
...
</soap:Envelope>
```
從以上 SOAP 命名空間中可知有定義了三種屬性，分別如下 :

### mustUnderstand 属性
> 提供安全標籤給接收者，當 Header 元素的某個子元素添加了 mustUnderstand="1", 代表已提供處理頭部的接收者安全標籤

語法
```
soap:mustUnderstand="0|1"
```

例子
```
<?xml version="1.0"?>
<soap:Envelope
xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

<soap:Header>
  <m:Trans xmlns:m="http://www.w3schools.com/transaction/"
  soap:mustUnderstand="1">234
  </m:Trans>
</soap:Header>
...
...
</soap:Envelope>
```

### actor 属性
> 1. 此屬性可於將Header 元素尋址到一個特定端點
> 2. SOAP 消息可發送至某個接收者，中途可能會經過不同的端點且並非傳送到最終端點，它也有可能尋址到特定的端點中

語法
```
soap:actor="URI"
```

例子
```
<?xml version="1.0"?>
<soap:Envelope
xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

<soap:Header>
  <m:Trans xmlns:m="http://www.w3schools.com/transaction/"
  soap:actor="http://www.w3schools.com/appml/">234
  </m:Trans>
</soap:Header>
...
...
</soap:Envelope>
```


### encodingStyle 属性
> 主要用於定義在文檔中使用的數據類型，可出現在任何 SOAP 元素並應用於元素的內容或是所有的子元素上。

語法
```
soap:encodingStyle="URI"
```


## SOAP Body 元素
> 包含傳送到最終端點的 SOAP 消息

例子
```
<?xml version="1.0"?>
<soap:Envelope
xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

<soap:Body>
  <m:GetPrice xmlns:m="http://www.w3schools.com/prices">
    <m:Item>Apples</m:Item>
  </m:GetPrice>
</soap:Body>

</soap:Envelope>
```


## SOAP Fault 元素
> 用於存留 SOAP 消息的錯誤資訊和狀態訊息 





有以下規則
- 必須是 Body 元素的子元素
- 一條 SOAP 消息中，Fault 元素只能出現一次
- 以下為 Fault 元素所擁有的子元素：
  
  | 子元素 | 描述 |
  | ----- | ---- |
  | `<faultcode>`	| 提供識別故障的代碼 |
  | `<faultstring>` | 提供故障敘述 |
  | `<faultactor>` | 提供是誰引發故障的訊息 |
  | `<detail>` | 提供涉及到 body 元素的應用程式錯誤資訊 |

- 定義 faultcode 值必須用於描述錯誤時的 faultcode 元素中：
  | 錯誤 | 描述 |
  | ---- | --- |
  | VersionMismatch |  |
  | MustUnderstand |  |
  | Client |  |
  | Server |  |



 ## Reference

[runoob-SOAP 教程](https://www.runoob.com/soap/soap-tutorial.html)