import datetime
from typing import Dict, List


from .websocket_manager import WebSocketManager
from backend.report_type import DetailedReport, ExtendedBasicReport
from gpt_researcher.utils.enum import ReportType, Tone
from multi_agents.main import run_research_task
from gpt_researcher.master.actions import stream_output  # Import stream_output

class ExtendedWebSocketManager(WebSocketManager):
    """Manage websockets"""

    async def start_streaming(self, task, report_type, report_source, source_urls, tone, websocket, headers=None, **extra_config_params):
        """Start streaming the output."""
        tone = Tone[tone]
        report = await extended_run_agent(task, report_type, report_source, source_urls, tone, websocket, headers, **extra_config_params)
        return report

async def extended_run_agent(task, report_type, report_source, source_urls, tone: Tone, websocket, headers=None, **extra_config_params):
    """Run the agent."""
    # measure time
    start_time = datetime.datetime.now()
    # add customized JSON config file path here
    config_path = ""
    # Instead of running the agent directly run it through the different report type classes
    if report_type == "multi_agents":
        report = await run_research_task(query=task, websocket=websocket, stream_output=stream_output, tone=tone, headers=headers)
        report = report.get("report", "")
    elif report_type == ReportType.DetailedReport.value:
        researcher = DetailedReport(
            query=task,
            report_type=report_type,
            report_source=report_source,
            source_urls=source_urls,
            tone=tone,
            config_path=config_path,
            websocket=websocket,
            headers=headers
        )
        report = await researcher.run()
    else:
        researcher = ExtendedBasicReport(
            query=task,
            report_type=report_type,
            report_source=report_source,
            source_urls=source_urls,
            tone=tone,
            config_path=config_path,
            websocket=websocket,
            headers=headers,
            **extra_config_params  # Pass additional parameters to the ExtendedBasicReport class
        )
        report = await researcher.run()

    # measure time
    end_time = datetime.datetime.now()
    await websocket.send_json(
        {"type": "logs", "output": f"\nTotal run time: {end_time - start_time}\n"}
    )

    return report