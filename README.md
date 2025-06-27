# 最 Min 捷快速 - 短網址產生器

一個輕量級的短網址服務平台，支援短碼自訂、密碼保護、頁面標題擷取等功能，並透過 Google Analytics 串接流量追蹤，已部署至 Render 雲端平台，可立即使用！

---

## 線上體驗

掃描 QR Code
<img src="https://min-url-shortener.onrender.com/MinQRCode" alt="Moordule-QRcode" width="400"/>

專案網址 :[https://min-url-shortener.onrender.com](https://min-url-shortener.onrender.com)
https://min-url-shortener.onrender.com/MinQRCode

---

## 專案特色

- 可自動或手動產生短網址
- 可設定密碼保護
- 可自動擷取原始網址標題作為備註
- 串接 Google Analytics 即時流量追蹤
- Render 雲端部署，隨時可用

---

## 使用技術

- 前端：HTML, Tailwind CSS, DaisyUI, Alpine.js
- 後端：Python, Django
- 資料庫：PostgreSQL
- 追蹤工具：Google Analytics
- 雲端部署：Render（Web + PostgreSQL）

### 前端資源採用 CDN 的說明

本專案為輕量級應用，考量以下因素，前端框架（如 Tailwind CSS、DaisyUI、Alpine.js、FontAwesome）皆透過 CDN 引入：

- 縮短開發與部署流程：免去配置 static 資料夾與 collectstatic
- 適合無需客製化樣式的中小型專案
- 降低雲端儲存空間使用與部署體積
- 部署 Render 等平台時更簡便，無需處理靜態檔案伺服設定

---

## 本地開發步驟

```bash
git clone https://github.com/qwer79790922/url-shortener.git
cd url-shortener

# 建立虛擬環境
python -m venv .venv
source .venv/bin/activate

# 安裝依賴套件
pip install -r requirements.txt

# 建立 .env 檔案（可參考 .env.example）
# 並執行資料遷移
python manage.py migrate

# 啟動伺服器
python manage.py runserver
```

---

## 開發者

- Min（謝旻澔）[GitHub](https://github.com/qWer79790922)
