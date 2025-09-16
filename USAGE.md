# Travel Planner AI - 使用指南

這是一個基於 CrewAI 的智能旅行規劃系統，使用多個 AI 代理來幫助您規劃完美的旅行。

## 功能特色

- **旅行研究員**: 研究目的地信息、天氣、交通等
- **行程規劃師**: 制定詳細的日程安排
- **當地專家**: 提供內部消息和隱藏景點
- **預算顧問**: 分析旅行成本和省錢技巧

## 安裝和運行

### 1. 安裝依賴
```bash
pip install crewai crewai-tools requests python-dotenv
```

### 2. 配置環境變量
確保 `.env` 文件包含必要的 API 密鑰：
```
MODEL=gpt-4o-mini
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

### 3. 運行系統

#### 互動模式
```bash
cd src
python -m travel_planner.main
```

#### 演示模式 (使用預設的東京旅行)
```bash
cd src
python -m travel_planner.main --demo
```

## 使用方法

1. 運行程序後，系統會詢問：
   - 目的地 (例如: Tokyo, Japan)
   - 旅行天數 (例如: 7)
   - 預算 (例如: $3000 USD)
   - 旅行風格 (可選: luxury, budget, adventure, cultural)

2. AI 代理團隊會依序工作：
   - 研究目的地信息
   - 規劃行程
   - 提供當地建議
   - 分析預算
   - 生成最終旅行計劃

3. 結果會保存在 `travel_plan.md` 文件中

## 系統架構

- **Agents (代理)**:
  - `travel_researcher`: 使用搜索和天氣工具
  - `itinerary_planner`: 使用搜索和計算器工具
  - `local_expert`: 使用搜索工具
  - `budget_advisor`: 使用計算器和搜索工具

- **Tools (工具)**:
  - `SearchTool`: 使用 Serper API 搜索最新信息
  - `WeatherTool`: 獲取天氣信息
  - `CalculatorTool`: 進行預算計算

- **Tasks (任務)**:
  1. 目的地研究
  2. 行程規劃
  3. 當地建議
  4. 預算分析
  5. 最終計劃整合

## 自定義

您可以通過修改以下文件來自定義系統：
- `config/agents.yaml`: 修改代理的角色和背景
- `config/tasks.yaml`: 調整任務描述和期望輸出
- `tools/`: 添加新的工具功能

## 注意事項

- 確保網絡連接正常，因為需要訪問外部 API
- 搜索結果的準確性取決於 Serper API 的搜索質量
- 預算估算僅供參考，實際費用可能有所不同

## 故障排除

如果遇到問題：
1. 檢查 API 密鑰是否正確設置
2. 確認網絡連接
3. 查看終端輸出的錯誤信息
4. 確保所有依賴都已正確安裝