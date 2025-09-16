#!/usr/bin/env python
"""
Simple Travel Planning System Test
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
    """Test environment setup"""
    print("=== Environment Test ===")
    print(f"Python version: {sys.version}")
    print(f"Current directory: {current_dir}")
    print(f"Parent directory: {parent_dir}")
    print(f"Environment file path: {env_path}")
    print(f"Environment file exists: {os.path.exists(env_path)}")
    
    # Check environment variables
    openai_key = os.getenv("OPENAI_API_KEY")
    serper_key = os.getenv("SERPER_API_KEY")
    
    print(f"OpenAI API Key: {'Configured' if openai_key else 'Not configured'}")
    print(f"Serper API Key: {'Configured' if serper_key else 'Not configured'}")
    
    return openai_key and serper_key

def test_imports():
    """Test module imports"""
    print("\n=== Module Import Test ===")
    try:
        from travel_planner.crew import TravelPlanner
        print("✓ TravelPlanner imported successfully")
        return True
    except ImportError as e:
        print(f"✗ TravelPlanner import failed: {e}")
        return False

def simple_demo():
    """Simple demonstration"""
    print("\n=== Travel Planning Demo ===")
    print("Destination: Tokyo, Japan")
    print("Duration: 7 days")
    print("Budget: $3000 USD")
    print("Style: Cultural tour")
    
    if not test_environment():
        print("Environment setup incomplete, cannot continue")
        return
    
    if not test_imports():
        print("Module import failed, cannot continue")
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
        
        print("\nStarting AI agent team...")
        travel_planner = TravelPlanner()
        crew = travel_planner.crew()
        
        print("Beginning travel planning execution...")
        result = crew.kickoff(inputs=inputs)
        
        print("\n" + "="*50)
        print("Travel planning complete!")
        print("="*50)
        
    except Exception as e:
        print(f"Error occurred during execution: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    simple_demo()