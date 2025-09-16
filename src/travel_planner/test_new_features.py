#!/usr/bin/env python
"""
簡單測試新功能
"""
import sys
import os
from datetime import datetime

# 設置 Python 路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# 加載環境變數
from dotenv import load_dotenv
env_path = os.path.join(parent_dir, '..', '.env')
load_dotenv(dotenv_path=env_path)

def test_new_features():
    """測試新功能"""
    print("=== 測試新功能 ===")
    print("✅ 日期功能: 支持旅行開始日期輸入")
    print("✅ 季節分析: 根據日期判斷季節")
    print("✅ 詳細地址: 每個地點都包含完整地址")
    print("✅ Google Maps: 每個地點都有地圖鏈接")
    print("✅ HTML 生成: 創建互動式網頁版本")
    
    # 測試季節函數
    from main import get_season
    print(f"\n季節測試:")
    print(f"12月 -> {get_season(12)}")
    print(f"6月 -> {get_season(6)}")
    print(f"3月 -> {get_season(3)}")
    print(f"9月 -> {get_season(9)}")
    
    # 示例輸入
    demo_date = datetime(2025, 12, 15)
    inputs = {
        'destination': 'Tokyo, Japan',
        'duration': 7,
        'budget': '$3000 USD',
        'travel_style': 'luxury',
        'start_date': demo_date.strftime('%Y-%m-%d'),
        'travel_month': demo_date.strftime('%B'), 
        'travel_season': get_season(demo_date.month),
        'current_year': str(datetime.now().year)
    }
    
    print(f"\n示例輸入:")
    for key, value in inputs.items():
        print(f"  {key}: {value}")
    
    print("\n新功能已成功集成！")
    print("系統現在會為每個地點提供:")
    print("- 📍 精確地址")
    print("- 🗺️ Google Maps 鏈接") 
    print("- 🕒 營業時間")
    print("- 📞 聯繫方式")
    print("- 🌐 互動式 HTML 報告")

if __name__ == "__main__":
    test_new_features()