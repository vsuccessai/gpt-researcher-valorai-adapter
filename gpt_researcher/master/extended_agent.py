import asyncio
import time
from typing import List, Union
import os
import sys
add_path = os.getcwd()
sys.path.insert(0, add_path)


from gpt_researcher.master.agent import GPTResearcher
from gpt_researcher.config import ExtConfig
from gpt_researcher.context.compression import ContextCompressor, WrittenContentCompressor
from gpt_researcher.document import DocumentLoader, LangChainDocumentLoader
from gpt_researcher.master.actions import *
from gpt_researcher.memory import Memory
from gpt_researcher.utils.enum import ReportSource, ReportType, Tone


class ExtendGPTResearcher(GPTResearcher):
    """ ExtendGPTResearcher class for handling extended actions """

    def __init__(
        self,
        query: str,
        cfg: ExtConfig,
        report_type: str = ReportType.ResearchReport.value,
        report_source=ReportSource.Web.value,
        tone: Tone = Tone.Objective,
        source_urls=None,
        documents=None,
        #config_path=None,
        websocket=None,
        agent=None,
        role=None,
        parent_query: str = "",
        subtopics: list = [],
        visited_urls: set = set(),
        verbose: bool = True,
        context=[],
        headers: dict = None,  # Add headers parameter 
    ):
        """
        Initialize the GPT Researcher class.
        Args:
            query: str,
            report_type: str
            source_urls
            tone
            config_path
            websocket
            agent
            role
            parent_query: str
            subtopics: list
            visited_urls: set
        """
        self.headers = headers or {}
        self.query: str = query
        self.agent: str = agent
        self.role: str = role
        self.report_type: str = report_type
        self.report_prompt: str = get_prompt_by_report_type(
            self.report_type
        )  # this validates the report type
        self.research_costs: float = 0.0
        #self.cfg = Config(config_path)
        self.cfg = cfg # for dynamic config (extended config)
        self.report_source: str = self.cfg.report_source or report_source
        self.retrievers = get_retrievers(self.headers, self.cfg)
        self.context = context
        self.source_urls = source_urls
        self.documents = documents
        self.memory = Memory(self.cfg.embedding_provider, self.headers)
        self.visited_urls: set[str] = visited_urls
        self.verbose: bool = verbose
        self.websocket = websocket
        self.headers = headers or {}
        # Ensure tone is an instance of Tone enum
        if isinstance(tone, dict):
            print(f"Invalid tone format: {tone}. Setting to default Tone.Objective.")
            self.tone = Tone.Objective
        elif isinstance(tone, str):
            self.tone = Tone[tone]
        else:
            self.tone = tone

        # Only relevant for DETAILED REPORTS
        # --------------------------------------

        # Stores the main query of the detailed report
        self.parent_query = parent_query

        # Stores all the user provided subtopics
        self.subtopics = subtopics

# async def main():
#     query = "What is the capital of France?"
#     cfg = ExtConfig()
#     gpt_researcher = ExtendGPTResearcher(query=query, cfg=cfg)
#     content = await gpt_researcher.conduct_research()
#     return content

# print(asyncio.run(main()))