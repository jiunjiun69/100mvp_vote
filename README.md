# 自動化投票程式

## 目前僅先支援使用註冊好的email + password的方式自動登入 (暫時不支援使用第三方google、facebook方式自動登入)

### 只需要在 `config.json` 中填入註冊好的`email`以及`password`再執行程式就可以了(懶惰的話可以使用Windows的工作排程器定時跑)

#### `config.json`中的參數解釋:
 - login_method : 可選 "google", "facebook", "email" (目前僅先支援email)
 - vote_count : 每次登入要投票的次數(最大3、最小1，可使用3直接投好投滿)
 - email : 請輸入您的 email
 - password : 請輸入您的 password
