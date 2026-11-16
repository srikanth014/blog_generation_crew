from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool


web_search_tool = SerperDevTool()

@CrewBase
class BlogGenerationCrew():
    """BlogGenerationCrew crew"""

    agents: List[BaseAgent]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    tasks: List[Task]


    @agent
    def team_leader(self) -> Agent:
        return Agent(
            config = self.agents_config["team_leader"] ,
            verbose=True,
            allow_delegation=True
        )

    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config = self.agents_config["research_agent"],
            verbose=True,
            allow_delegation=False,
            tools = [web_search_tool]
            )

    
    @agent
    def blog_writing_agent(self) -> Agent:
         return Agent(
            config = self.agents_config["blog_writing_agent"],
            verbose = True,
            allow_delegation=False
         )

    @agent
    def blog_review_agent(self) -> Agent:
         return Agent(
            config = self.agents_config["blog_review_agent"],
            verbose = True,
            allow_delegation=False
         )

    @task
    def blog_writing_task(self)-> Task:
        return Task(
            config = self.tasks_config['blog_writing_task'],
            output_file="blog.md"
        )


    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = [self.research_agent(), self.blog_writing_agent(), self.blog_review_agent()],
            tasks = [self.blog_writing_task()],
            process = Process.hierarchical,
            verbose = True,
            manager_agent=self.team_leader()
        )
