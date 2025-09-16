from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests
import json


class CalculatorToolInput(BaseModel):
    """Input schema for CalculatorTool."""
    operation: str = Field(..., description="Mathematical operation or calculation to perform, e.g., '100 * 7 + 50' for calculating trip costs")


class CalculatorTool(BaseTool):
    name: str = "Calculator"
    description: str = (
        "A tool to perform mathematical calculations for travel budgeting, cost estimation, "
        "currency conversion, and other numerical operations needed for travel planning."
    )
    args_schema: Type[BaseModel] = CalculatorToolInput

    def _run(self, operation: str) -> str:
        """Perform mathematical calculations safely."""
        try:
            # Remove any potentially dangerous characters
            allowed_chars = "0123456789+-*/.() "
            cleaned_operation = ''.join(c for c in operation if c in allowed_chars)
            
            # Evaluate the mathematical expression safely
            result = eval(cleaned_operation)
            return f"Calculation: {operation} = {result}"
            
        except Exception as e:
            return f"Error in calculation: {str(e)}"


class WeatherToolInput(BaseModel):
    """Input schema for WeatherTool."""
    location: str = Field(..., description="Location to get weather information for")
    query_type: str = Field(default="current", description="Type of weather query: 'current', 'forecast', or 'climate'")


class WeatherTool(BaseTool):
    name: str = "Weather Information"
    description: str = (
        "A tool to get weather information for travel destinations, including current conditions, "
        "forecasts, and general climate information to help with travel planning."
    )
    args_schema: Type[BaseModel] = WeatherToolInput

    def _run(self, location: str, query_type: str = "current") -> str:
        """Get weather information using search."""
        try:
            from .search_tool import SearchTool
            search_tool = SearchTool()
            
            if query_type == "current":
                query = f"current weather in {location}"
            elif query_type == "forecast":
                query = f"weather forecast {location} next 7 days"
            else:
                query = f"climate and weather patterns {location} best time to visit"
            
            return search_tool._run(query)
            
        except Exception as e:
            return f"Error getting weather information: {str(e)}"