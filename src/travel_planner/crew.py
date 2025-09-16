from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from travel_planner.tools.search_tool import SearchTool
from travel_planner.tools.travel_tools import CalculatorTool, WeatherTool

@CrewBase
class TravelPlanner():
    """TravelPlanner crew for comprehensive travel planning"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def travel_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['travel_researcher'], # type: ignore[index]
            tools=[SearchTool(), WeatherTool()],
            verbose=True
        )

    @agent
    def itinerary_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['itinerary_planner'], # type: ignore[index]
            tools=[SearchTool(), CalculatorTool()],
            verbose=True
        )

    @agent
    def local_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['local_expert'], # type: ignore[index]
            tools=[SearchTool()],
            verbose=True
        )

    @agent
    def budget_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['budget_advisor'], # type: ignore[index]
            tools=[CalculatorTool(), SearchTool()],
            verbose=True
        )

    @task
    def destination_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['destination_research_task'], # type: ignore[index]
        )

    @task
    def itinerary_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['itinerary_planning_task'], # type: ignore[index]
        )

    @task
    def local_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config['local_insights_task'], # type: ignore[index]
        )

    @task
    def budget_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['budget_analysis_task'], # type: ignore[index]
        )

    @task
    def final_travel_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['final_travel_plan_task'], # type: ignore[index]
            output_file='travel_plan.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TravelPlanner crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
