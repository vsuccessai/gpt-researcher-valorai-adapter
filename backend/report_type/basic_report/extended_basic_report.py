from fastapi import WebSocket
import os
import sys
add_path = os.getcwd()
sys.path.insert(0, add_path)
import asyncio

#from .basic_report import BasicReport
from backend.report_type.basic_report.basic_report import BasicReport
from gpt_researcher.config.extended_config import ExtConfig
from gpt_researcher.master.extended_agent import ExtendGPTResearcher
from gpt_researcher.utils.enum import Tone


class ExtendedBasicReport(BasicReport):

    def __init__(
        self,
        query: str,
        report_type: str,
        report_source: str,
        source_urls,
        tone: Tone,
        config_path: str,
        websocket: WebSocket,
        headers=None,
        **kwargs  # Additional parameters for the ExtConfig class
    ):       
        super().__init__(
            query=query,
            report_type=report_type,
            report_source=report_source,
            source_urls=source_urls,
            tone=tone,
            config_path=config_path,
            websocket=websocket,
            headers=headers
        )
        
        # Store additional parameters in a separate attribute
        self.extra_config_params = kwargs

    async def run(self):
        """	Run the extended basic report."""

        # Initialize the extended researcher
        researcher = ExtendGPTResearcher(
            query=self.query,          
            report_type=self.report_type,
            report_source=self.report_source,
            source_urls=self.source_urls,
            tone=self.tone,
            config_path=self.config_path,
            websocket=self.websocket,
            headers=self.headers,
            **self.extra_config_params        
        )

        # Run research
        await researcher.conduct_research()

        # Generate report
        report = await researcher.write_report()
        return report

    



#test code

# init = ExtendedBasicReport(
#     query="What is the capital of France?",
#     report_type="research_report",
#     report_source="web",
#     source_urls=None,
#     tone="Objective",
#     config_path=None,
#     websocket=None,
#     headers=None,    
#     retrievers = ["google"],
#     llm_provider = 'test',
#     llm_model = 'gpt2',
#     smart_llm_model = 'gpt2',
# )
# asyncio.run(init.run())  # Run the extended basic report