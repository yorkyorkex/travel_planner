#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime
from dotenv import load_dotenv

# Add the src directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from travel_planner.crew import TravelPlanner

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def get_user_input():
    """Get travel planning inputs from user."""
    print("=== Travel Planner AI ===")
    print("讓我來幫您規劃一次完美的旅行！")
    print()
    
    destination = input("請輸入您想去的目的地 (例如: Tokyo, Japan): ").strip()
    
    while True:
        try:
            duration = int(input("請輸入旅行天數 (例如: 7): ").strip())
            break
        except ValueError:
            print("請輸入有效的數字")
    
    budget = input("請輸入您的預算 (例如: $3000 USD): ").strip()
    
    travel_style = input("旅行風格 (可選，例如: luxury, budget, adventure, cultural): ").strip()
    
    return {
        'destination': destination,
        'duration': duration,
        'budget': budget,
        'travel_style': travel_style or 'moderate',
        'current_year': str(datetime.now().year)
    }

def run():
    """
    Run the travel planning crew.
    """
    try:
        # Check if running in interactive mode or with predefined inputs
        if len(sys.argv) > 1 and sys.argv[1] == "--demo":
            # Demo mode with predefined inputs
            inputs = {
                'destination': 'Tokyo, Japan',
                'duration': 7,
                'budget': '$3000 USD',
                'travel_style': 'cultural',
                'current_year': str(datetime.now().year)
            }
            print("Running demo mode with Tokyo, Japan...")
        else:
            # Interactive mode
            inputs = get_user_input()
        
        print(f"\n正在為您規劃 {inputs['destination']} 的 {inputs['duration']} 天旅行...")
        print(f"預算: {inputs['budget']}")
        print("請稍候，AI 代理團隊正在工作中...\n")
        
        result = TravelPlanner().crew().kickoff(inputs=inputs)
        
        print("\n" + "="*50)
        print("旅行規劃完成！")
        print("詳細的旅行計劃已保存到 travel_plan.md 文件中")
        print("="*50)
        
        return result
        
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'destination': 'Tokyo, Japan',
        'duration': 7,
        'budget': '$3000 USD',
        'travel_style': 'cultural',
        'current_year': str(datetime.now().year)
    }
    try:
        TravelPlanner().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TravelPlanner().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'destination': 'Tokyo, Japan',
        'duration': 7,
        'budget': '$3000 USD',
        'travel_style': 'cultural',
        'current_year': str(datetime.now().year)
    }
    
    try:
        TravelPlanner().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()
