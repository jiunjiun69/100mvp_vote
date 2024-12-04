# 自動化投票程式

## 功能簡介
此程式目前支援透過 **註冊好的 Email 與密碼** 自動登入進行投票（暫不支援 Google 或 Facebook 第三方登入）。  
只需在 `config.json` 中填入 **Email** 與 **Password**，並執行程式即可完成自動投票！  
*提示：可搭配 Windows 的排程器定時執行，實現全自動化投票。*

---

## 快速開始

### 步驟 1：下載與解壓縮
1. 從[Releases](https://github.com/jiunjiun69/100mvp_vote/releases/tag/v1.0.0) 下載 `100mvp_vote.exe`執行檔。
2. 將 **執行檔 `100mvp_vote.exe`** 與 **設定檔 `config.json`** 放置於同一目錄。

### 步驟 2：設定 `config.json`
根據您的使用情境，設定以下參數：

```json
{
    "mode": "home",  // 模式選擇: "home", "company", "manual"
    "proxy": {
        "http": "http://proxy_host:proxy_port",  // 公司模式需設定
        "https": "http://proxy_host:proxy_port",
        "username": "ad_username",  // AD 使用者名稱
        "password": "ad_password"   // AD 密碼
    },
    "chromedriver_path": "chromedriver.exe",  // 手動模式需指定，若`chromedriver.exe`與`100mvp_vote.exe`放置同一層目錄時則不需更改
    "login_method": "email",  // 登入方式: 僅支援 "email"
    "vote_count": 3,  // 每次登入的投票次數 (1 至 3 次)
    "email": "vote_email",  // 經理人網站註冊的 Email
    "password": "vote_password"  // 經理人網站註冊的密碼
}
```

### 步驟 3：執行程式
在同一目錄下執行 `100mvp_vote.exe`，程式將自動依據設定進行操作。

---

## 配置參數說明

| **參數**         | **描述**                                                                                   | **範例值**                                                                 |
|-------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `mode`            | 模式選擇：`home`、`company`、`manual`                                                    | `"home"`、`"company"`、`"manual"`                                          |
| `proxy`           | 公司模式需設定代理，包含 `http` 和 `https` 主機、`username` 和 `password`                | `"http": "http://proxy.company.com:8080"`                                  |
| `chromedriver_path` | 手動模式需指定 ChromeDriver 的執行檔路徑                                                | `"chromedriver_path": "chromedriver.exe"`                                  |
| `login_method`    | 登入方式，目前僅支援 Email                                                               | `"email"`                                                                  |
| `vote_count`      | 每次登入的投票次數，最大值為 3                                                            | `3`                                                                        |
| `email`           | 經理人網站的註冊 Email                                                                   | `"vote_email@example.com"`                                                |
| `password`        | 經理人網站的註冊密碼                                                                     | `"your_password"`                                                          |

---

## 模式說明

### 1. 家庭模式 `home` (可以連到外網)
適用於能直接連外網的情境：
- 設定 `mode` 為 `"home"`。
- 填寫您註冊經理人網站的 **Email** 和 **Password**。
- 程式將自動下載並使用適合的 ChromeDriver。

### 2. 公司模式 `company` (直接連外網會擋住)
適用於需經代理伺服器連外網的情境：
- 設定 `mode` 為 `"company"`。
- 填寫您註冊經理人網站的 **Email** 和 **Password**。
- 填寫 **代理伺服器** (`http`/`https`)、**AD 帳號** 和 **密碼**。
- 程式將透過代理下載 ChromeDriver。

### 3. 手動模式 `manual` (將瀏覽器驅動預先下載至本地運行，較穩定)
適用於希望手動管理 ChromeDriver 的情境：
1. 設定 `mode` 為 `"manual"`。
2. 填寫您註冊經理人網站的 **Email** 和 **Password**。
3. 手動下載 ChromeDriver，並將其放置在與執行檔同一目錄。
4. 填寫 `chromedriver_path` 為 ChromeDriver 的檔案名稱或完整路徑。

---

## 手動下載 ChromeDriver (手動模式 `manual`才須做此項操作)
### 步驟
1. 在 Google Chrome 瀏覽器的網址列輸入 `chrome://settings/help`，找到您的 **瀏覽器版本號(目前本儲存庫為131.0.6778)**。
2. 前往以下網站下載對應版本的 ChromeDriver (win64沒有的話就選win32，記得名稱要是chromedriver)：
   - [最新版 ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/)
   - [舊版 ChromeDriver](https://chromedriver.storage.googleapis.com/index.html) （若需要）
3. 下載後將 `chromedriver.exe` 解壓縮並放置於與 `100mvp_vote.exe` 相同的目錄(替換掉目前的 `chromedriver.exe`)。

---

## 注意事項
1. **目前限制**：僅支援使用 Email 登入。
2. **公司模式代理設定**：確保 `proxy` 配置正確，並提供合法的 AD 帳號密碼。
3. **手動模式穩定性**：手動下載 ChromeDriver 可避免版本不符問題，但需自行管理。

---

## 開發者聯絡
如需協助或有其他建議，歡迎提出 Issue 或 Pull Request。
