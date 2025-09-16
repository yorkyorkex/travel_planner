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
    print("Let me help you plan the perfect trip!")
    print()
    
    destination = input("Enter your desired destination (e.g., Tokyo, Japan): ").strip()
    
    while True:
        try:
            duration = int(input("Enter trip duration in days (e.g., 7): ").strip())
            break
        except ValueError:
            print("Please enter a valid number")
    
    budget = input("Enter your budget (e.g., $3000 USD): ").strip()
    
    travel_style = input("Travel style (optional, e.g., luxury, budget, adventure, cultural): ").strip()
    
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
        
        print(f"\nPlanning your {inputs['duration']}-day trip to {inputs['destination']}...")
        print(f"Budget: {inputs['budget']}")
        print("Please wait, our AI agent team is working...\n")
        
        result = TravelPlanner().crew().kickoff(inputs=inputs)
        
        print("\n" + "="*50)
        print("Travel Planning Complete!")
        print("Detailed travel plan has been saved to travel_plan.md")
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
