# Travel Planner AI - User Guide

This is an intelligent travel planning system based on CrewAI, using multiple AI agents to help you plan the perfect trip.

## Key Features

- **Travel Researcher**: Research destination information, weather, transportation, etc.
- **Itinerary Planner**: Create detailed daily schedules
- **Local Expert**: Provide insider tips and hidden gems
- **Budget Advisor**: Analyze travel costs and money-saving tips

## Installation and Setup

### 1. Install Dependencies
```bash
pip install crewai crewai-tools requests python-dotenv
```

### 2. Configure Environment Variables
Ensure your `.env` file contains the necessary API keys:
```
MODEL=gpt-4o-mini
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

### 3. Run the System

#### Interactive Mode
```bash
cd src/travel_planner
python main.py
```

#### Demo Mode (with preset Tokyo trip)
```bash
cd src/travel_planner
python main.py --demo
```

#### Test Mode
```bash
cd src/travel_planner
python test_demo.py
```

## How to Use

1. When you run the program, the system will ask for:
   - Destination (e.g., Tokyo, Japan)
   - Trip duration (e.g., 7)
   - Budget (e.g., $3000 USD)
   - Travel style (optional: luxury, budget, adventure, cultural)

2. The AI agent team will work sequentially:
   - Research destination information
   - Plan itinerary
   - Provide local recommendations
   - Analyze budget
   - Generate final travel plan

3. Results will be saved in the `travel_plan.md` file

## System Architecture

- **Agents**:
  - `travel_researcher`: Uses search and weather tools
  - `itinerary_planner`: Uses search and calculator tools
  - `local_expert`: Uses search tools
  - `budget_advisor`: Uses calculator and search tools

- **Tools**:
  - `SearchTool`: Uses Serper API to search for latest information
  - `WeatherTool`: Get weather information
  - `CalculatorTool`: Perform budget calculations

- **Tasks**:
  1. Destination research
  2. Itinerary planning
  3. Local recommendations
  4. Budget analysis
  5. Final plan integration

## Customization

You can customize the system by modifying these files:
- `config/agents.yaml`: Modify agent roles and backgrounds
- `config/tasks.yaml`: Adjust task descriptions and expected outputs
- `tools/`: Add new tool functionality

## Important Notes

- Ensure stable internet connection as external APIs are required
- Search result accuracy depends on Serper API search quality
- Budget estimates are for reference only; actual costs may vary

## Troubleshooting

If you encounter issues:
1. Check if API keys are correctly configured
2. Verify internet connection
3. Review terminal output for error messages
4. Ensure all dependencies are properly installed

## Example Output

The system generates a comprehensive travel guide including:
- Executive summary
- Day-by-day detailed itinerary
- Budget breakdown and spending guidelines
- Important local information and cultural tips
- Emergency contacts
- Packing recommendations
- Pre-trip checklist
- Alternative plans for different weather conditions