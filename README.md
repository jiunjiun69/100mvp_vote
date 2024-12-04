# 自動化投票程式

## 目前僅先支援使用註冊好的email + password的方式自動登入 (暫時不支援使用第三方google、facebook方式自動登入)

### 只需要在 `config.json` 中填入註冊好的`email`以及`password`再執行程式就可以了(懶惰的話可以使用Windows的工作排程器定時跑)

#### `config.json`中的參數解釋:
 - mode : 可選值: "home", "company", "manual" (在公司外面可以連外網使用"home"，在公司內部請使用"company" + 設定proxy 或是 "manual" + 下載驅動)
 - proxy : mode 選擇為"company"時才須設定，將"proxy"中的"http"及"https"替換為公司proxy主機；"proxy"中的"username"替換為AD帳號，"password"替換為AD密碼
 - chromedriver_path : mode 選擇為"manual"時才須設定，Chrome瀏覽器驅動目錄，基本上將瀏覽器驅動與執行檔放置同一目錄下就不用修改 (建議維持原樣)
 - login_method : 可選 "google", "facebook", "email" (目前僅先支援email)
 - vote_count : 每次登入要投票的次數(最大3、最小1，可使用3直接投好投滿)
 - email : 請輸入您註冊經理人網站的 email
 - password : 請輸入您註冊經理人網站的 password


需先將 `100mvp_vote.rar` 壓縮檔解壓縮出執行檔 `100mvp_vote.exe`，將 `100mvp_vote.exe` 其與 `config.json` 放置至同一層目錄中，並在 `config.json` 中設定好自己的`email`以及`password`就可以執行了

---

## mode 切換注意事項:
1. ["mode": "home"] 如果在家使用的話(可以連到外網)，僅需將mode設定為home，再設定email與password為註冊經理人網站的郵件與密碼就可以執行了
2. ["mode": "company"] 如果在公司使用的話(連線外網會擋住)，因為程式中會需要連外網抓取瀏覽器驅動程式，因此會需要設定proxy連出去外網，需將mode設定為company，並將proxy中的proxy主機、port號與ad帳號密碼設置完成才能連線出去，再設定email與password為註冊經理人網站的郵件與密碼就可以執行了
3. ["mode": "manual"] 如果想要直接執行本地瀏覽器驅動(將瀏覽器驅動預先下載至本地運行，較穩定)，就不需要設定proxy了，不過需要先去下載瀏覽器驅動程式，將其 `chromedriver.exe` 執行檔放置至與 `100mvp_vote.exe` 自動投票執行檔同一層的目錄中，再設定email與password為註冊經理人網站的郵件與密碼就可以執行了
   - 瀏覽器驅動下載流程(目前以Google Chrome為主)
      1. 在Google Chrome瀏覽器網址列輸入 `chrome://settings/help` ，找到目前的版本號(目前本儲存庫為131.0.6778)
      2. 前往官方網站下載瀏覽器驅動程式: `https://googlechromelabs.github.io/chrome-for-testing/` (如果瀏覽器版本過舊，可以到此網址去找: `https://chromedriver.storage.googleapis.com/index.html`)
      3. 下載 win64 或 win32 的 chromedriver ，將其解壓縮後的 `chromedriver.exe` 執行檔放置至與 `100mvp_vote.exe` 自動投票執行檔同一層的目錄中就完成了
