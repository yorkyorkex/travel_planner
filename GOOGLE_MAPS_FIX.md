# Google Maps URL 修正指南

## 問題分析
當前 AI 生成的 Google Maps 網址格式不正確，無法正常連接。

## 正確的 Google Maps URL 格式

### 1. 搜索 URL 格式 (推薦)
```
https://www.google.com/maps/search/?api=1&query=LOCATION_NAME+FULL_ADDRESS
```

**示例:**
- Tokyo Skytree: `https://www.google.com/maps/search/?api=1&query=Tokyo+Skytree+1-1-2+Oshiage+Sumida+City+Tokyo+Japan`
- Senso-ji Temple: `https://www.google.com/maps/search/?api=1&query=Senso-ji+Temple+2-3-1+Asakusa+Taito+City+Tokyo+Japan`

### 2. 地點 URL 格式
```
https://www.google.com/maps/place/LOCATION_NAME/@LATITUDE,LONGITUDE,ZOOM
```

### 3. 方向 URL 格式
```
https://www.google.com/maps/dir/ORIGIN/DESTINATION
```

## 修正方法

### 方法 1: 更新任務描述
在 `tasks.yaml` 中指定確切的 URL 格式：

```yaml
Google Maps URL must follow this exact format:
https://www.google.com/maps/search/?api=1&query=[Location+Name]+[Full+Address]
Example: https://www.google.com/maps/search/?api=1&query=Tokyo+Skytree+1-1-2+Oshiage+Sumida+City+Tokyo+Japan

Rules:
- Replace all spaces with + signs
- Include full location name and address
- Use the complete address in English
- No special characters like commas in the query
```

### 方法 2: 創建 URL 驗證工具
可以創建一個專門的工具來生成和驗證 Google Maps URL。

### 方法 3: 使用更具體的搜索指令
告訴 AI：
```
For each location, provide Google Maps URL in this EXACT format:
https://www.google.com/maps/search/?api=1&query=Tokyo+Skytree+1-1-2+Oshiage+Sumida+City+Tokyo+131-0045+Japan

Replace:
- All spaces with +
- Remove commas from the query parameter
- Include full English address
```

## 測試 URL

可以複製以下 URL 測試是否正常工作：

1. **Tokyo Skytree**: https://www.google.com/maps/search/?api=1&query=Tokyo+Skytree+1-1-2+Oshiage+Sumida+City+Tokyo+Japan

2. **Senso-ji Temple**: https://www.google.com/maps/search/?api=1&query=Senso-ji+Temple+2-3-1+Asakusa+Taito+City+Tokyo+Japan

3. **Meiji Shrine**: https://www.google.com/maps/search/?api=1&query=Meiji+Shrine+1-1+Kamizono-cho+Shibuya+City+Tokyo+Japan

## 實施建議

1. **立即修正**: 更新 `tasks.yaml` 中的 URL 格式指令
2. **測試驗證**: 運行系統並檢查生成的 URL 是否可以正常開啟
3. **HTML 修正**: 確保 HTML 生成器也使用正確的 URL 格式

這樣修正後，所有生成的 Google Maps 鏈接都應該能正常工作！