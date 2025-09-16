from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests
import os


class SearchToolInput(BaseModel):
    """Input schema for SearchTool."""
    query: str = Field(..., description="The search query to find information about travel destinations, attractions, restaurants, etc.")


class SearchTool(BaseTool):
    name: str = "Search Tool"
    description: str = (
        "A tool to search for current information about travel destinations, attractions, restaurants, "
        "weather conditions, and other travel-related topics using Serper API."
    )
    args_schema: Type[BaseModel] = SearchToolInput

    def _run(self, query: str) -> str:
        """Search for information using Serper API."""
        try:
            api_key = os.getenv("SERPER_API_KEY")
            if not api_key:
                return "Error: SERPER_API_KEY not found in environment variables."
            
            url = "https://google.serper.dev/search"
            payload = {
                "q": query,
                "num": 10
            }
            headers = {
                "X-API-KEY": api_key,
                "Content-Type": "application/json"
            }
            
            response = requests.post(url, json=payload, headers=headers)
            
            if response.status_code == 200:
                results = response.json()
                
                # Format the search results
                formatted_results = []
                
                # Add organic results
                if "organic" in results:
                    for result in results["organic"][:8]:  # Limit to top 8 results
                        formatted_results.append(f"**{result.get('title', 'No Title')}**\n{result.get('snippet', 'No description available')}\nSource: {result.get('link', 'No link')}\n")
                
                # Add knowledge graph info if available
                if "knowledgeGraph" in results:
                    kg = results["knowledgeGraph"]
                    if "description" in kg:
                        formatted_results.insert(0, f"**Knowledge Graph Info:**\n{kg['description']}\n")
                
                return "\n".join(formatted_results) if formatted_results else "No relevant information found."
            
            else:
                return f"Error: Search request failed with status code {response.status_code}"
                
        except Exception as e:
            return f"Error performing search: {str(e)}"