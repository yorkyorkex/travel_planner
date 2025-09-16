#!/usr/bin/env python
"""
簡單的旅行規劃系統測試
"""
import os
import sys
import warnings
from datetime import datetime
from dotenv import load_dotenv

# 設置 Python 路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# 加載環境變數
env_path = os.path.join(parent_dir, '..', '.env')
load_dotenv(dotenv_path=env_path)

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def test_environment():
    """測試環境設置"""
    print("=== 環境測試 ===")
    print(f"Python 版本: {sys.version}")
    print(f"當前目錄: {current_dir}")
    print(f"父目錄: {parent_dir}")
    print(f"環境文件路徑: {env_path}")
    print(f"環境文件存在: {os.path.exists(env_path)}")
    
    # 檢查環境變數
    openai_key = os.getenv("OPENAI_API_KEY")
    serper_key = os.getenv("SERPER_API_KEY")
    
    print(f"OpenAI API Key: {'設置完成' if openai_key else '未設置'}")
    print(f"Serper API Key: {'設置完成' if serper_key else '未設置'}")
    
    return openai_key and serper_key

def test_imports():
    """測試模組導入"""
    print("\n=== 模組導入測試 ===")
    try:
        from travel_planner.crew import TravelPlanner
        print("✓ TravelPlanner 導入成功")
        return True
    except ImportError as e:
        print(f"✗ TravelPlanner 導入失敗: {e}")
        return False

def simple_demo():
    """簡單演示"""
    print("\n=== 旅行規劃演示 ===")
    print("目的地: 東京, 日本")
    print("天數: 7 天")
    print("預算: $3000 USD")
    print("風格: 文化之旅")
    
    if not test_environment():
        print("環境設置不完整，無法繼續")
        return
    
    if not test_imports():
        print("模組導入失敗，無法繼續")
        return
    
    try:
        from travel_planner.crew import TravelPlanner
        
        inputs = {
            'destination': 'Tokyo, Japan',
            'duration': 7,
            'budget': '$3000 USD',
            'travel_style': 'cultural',
            'current_year': str(datetime.now().year)
        }
        
        print("\n正在啟動 AI 代理團隊...")
        travel_planner = TravelPlanner()
        crew = travel_planner.crew()
        
        print("開始執行旅行規劃...")
        result = crew.kickoff(inputs=inputs)
        
        print("\n" + "="*50)
        print("旅行規劃完成！")
        print("="*50)
        
    except Exception as e:
        print(f"執行過程中出現錯誤: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    simple_demo()