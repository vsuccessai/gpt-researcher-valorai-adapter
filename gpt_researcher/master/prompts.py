import warnings
from datetime import date, datetime, timezone

from gpt_researcher.utils.enum import ReportSource, ReportType, Tone


def generate_search_queries_prompt(
    question: str,
    parent_query: str,
    report_type: str,
    max_iterations: int = 3,
):
    """Generates the search queries prompt for the given question.
    Args:
        question (str): The question to generate the search queries prompt for
        parent_query (str): The main question (only relevant for detailed reports)
        report_type (str): The report type
        max_iterations (int): The maximum number of search queries to generate
    Returns: str: The search queries prompt for the given question
    """
    if (
        report_type == ReportType.DetailedReport.value
        or report_type == ReportType.SubtopicReport.value
    ):
        task = f"{parent_query} - {question}"
    else:
        task = question
    return (
        f'Formulate {max_iterations} strategic Google search queries to find high-quality, evidence-based information on: "{task}"\n\n'
        f"Your queries MUST target:\n"
        f"1. Peer-reviewed journals and academic databases (e.g., JSTOR, PubMed, Google Scholar)\n"
        f"2. Government statistical databases and reports (e.g., CDC, BLS, WHO, World Bank)\n"
        f"3. Industry research papers with quantitative data and statistical analysis\n"
        f"4. Recent publications with up-to-date statistics (within last 2-3 years when possible)\n"
        f"5. Sources containing specific metrics, figures, percentages, and quantitative evidence\n\n"
        f"Include specific search operators where appropriate (e.g., site:.edu, site:.gov, filetype:pdf)\n"
        f"Assume the current date is {datetime.now(timezone.utc).strftime('%B %d, %Y')}.\n\n"
        f'Respond ONLY with a JSON-formatted list of strings: ["query 1", "query 2", "query 3"].\n'
        f"NO explanations or additional text."
    )


def generate_report_prompt(
    question: str,
    context,
    report_source: str,
    report_format="apa",
    total_words=1000,
    tone: Tone =None,
):
    """Generates the report prompt for the given question and research summary.
    Args: question (str): The question to generate the report prompt for
            research_summary (str): The research summary to generate the report prompt for
    Returns: str: The report prompt for the given question and research summary
    """
    reference_prompt = ""
    if report_source == ReportSource.Web.value:
        reference_prompt = f"""
    You MUST include properly formatted citations for all sources used. For each source:
    1. Create in-text citations at the point where information is used: ([Author/Website Name, Year](url))
    2. Include a comprehensive references section at the end with full bibliographic information
    3. Ensure every URL is properly hyperlinked using markdown: [Title or Website Name](complete-url)
    4. Prioritize academic, governmental, and authoritative industry sources in your citations
    5. When citing statistics or quantitative data, always include the specific source
    """
    else:
        reference_prompt = f"""
    You MUST include properly formatted citations for all document sources used:
    1. Create in-text citations at the point where information is used: (Document Name, Section/Page)
    2. Include a comprehensive references section listing all documents with full metadata
    3. For statistical information, specify the exact page number, table, or section where the data appears
    4. Prioritize primary research documents and original data sources over secondary analyses
    """
    try: 
        tone_prompt = f"Write the report in a {tone.value} tone" if tone else ""
    except:
        tone_prompt = ""
    return f"""
    RESEARCH CONTEXT:
    "{context}"
    ---
    TASK:
    Create a comprehensive, evidence-based report addressing: "{question}"
    REPORT REQUIREMENTS:
    • Structure: Well-organized with clear sections, headings, and logical flow
    • Content: Data-driven analysis with EXTENSIVE quantitative evidence including:
    - Specific statistics, percentages, and numerical data
    - Trend analysis with year-over-year comparisons where available
    - Demographic breakdowns and segmentation data
    - Economic figures, costs, and financial metrics when relevant
    - Visual representation recommendations (tables, charts) for complex data
    • Evidence Quality: Prioritize peer-reviewed research, government data, and authoritative sources
    • Depth: In-depth exploration with minimum {total_words} words, utilizing all relevant information
    • Format: Professional markdown formatting with {report_format.upper()} citation style
    ANALYTICAL APPROACH:
    • Quantify ALL key points with specific numbers and statistics
    • Include confidence intervals, sample sizes, and methodological context for statistics when available
    • Compare multiple data sources to establish consensus figures or highlight discrepancies
    • Explicitly identify data limitations, collection methodologies, and potential biases
    • Translate complex statistical findings into clear, actionable insights
    CRITICAL GUIDELINES:
    • NEVER make general claims without supporting quantitative evidence
    • ALWAYS specify the exact figures, percentages, and metrics
    • Include trend data showing changes over time whenever possible
    • When exact figures aren't available, provide estimated ranges based on available data
    • For controversial topics, quantify different perspectives with data supporting each position
    {reference_prompt}
    {tone_prompt}
    This report will be used for critical decision-making requiring precise quantitative understanding.
    Current date: {date.today()}
    """


def generate_resource_report_prompt(
    question, context, report_source: str, report_format="apa", tone=None, total_words=1000
):
    """Generates the resource report prompt for the given question and research summary.

    Args:
        question (str): The question to generate the resource report prompt for.
        context (str): The research summary to generate the resource report prompt for.

    Returns:
        str: The resource report prompt for the given question and research summary.
    """

    reference_prompt = ""
    if report_source == ReportSource.Web.value:
        reference_prompt = f"""
            You MUST include all relevant source urls.
            Every url should be hyperlinked: [url website](url)
            """
    else:
        reference_prompt = f"""
            You MUST write all used source document names at the end of the report as references, and make sure to not add duplicated sources, but only one reference for each."
        """

    return (
        f'"""{context}"""\n\nBased on the above information, generate a bibliography recommendation report for the following'
        f' question or topic: "{question}". The report should provide a detailed analysis of each recommended resource,'
        " explaining how each source can contribute to finding answers to the research question.\n"
        "Focus on the relevance, reliability, and significance of each source.\n"
        "Ensure that the report is well-structured, informative, in-depth, and follows Markdown syntax.\n"
        "Include relevant facts, figures, and numbers whenever available.\n"
        f"The report should have a minimum length of {total_words} words.\n"
        "You MUST include all relevant source urls."
        "Every url should be hyperlinked: [url website](url)"
        f"{reference_prompt}"
    )


def generate_custom_report_prompt(
    query_prompt, context, report_source: str, report_format="apa", tone=None, total_words=1000
):
    return f'"{context}"\n\n{query_prompt}'


def generate_outline_report_prompt(
    question, context, report_source: str, report_format="apa",tone=None,  total_words=1000
):
    """Generates the outline report prompt for the given question and research summary.
    Args: question (str): The question to generate the outline report prompt for
            research_summary (str): The research summary to generate the outline report prompt for
    Returns: str: The outline report prompt for the given question and research summary
    """

    return (
        f'"""{context}""" Using the above information, generate an outline for a research report in Markdown syntax'
        f' for the following question or topic: "{question}". The outline should provide a well-structured framework'
        " for the research report, including the main sections, subsections, and key points to be covered."
        f" The research report should be detailed, informative, in-depth, and a minimum of {total_words} words."
        " Use appropriate Markdown syntax to format the outline and ensure readability."
    )


def get_report_by_type(report_type: str):
    report_type_mapping = {
        ReportType.ResearchReport.value: generate_report_prompt,
        ReportType.ResourceReport.value: generate_resource_report_prompt,
        ReportType.OutlineReport.value: generate_outline_report_prompt,
        ReportType.CustomReport.value: generate_custom_report_prompt,
        ReportType.SubtopicReport.value: generate_subtopic_report_prompt,
    }
    return report_type_mapping[report_type]


def auto_agent_instructions():
    return """
This task involves researching a given topic, regardless of its complexity or the availability of a definitive answer. The research is conducted by a specific server, defined by its type and role, with each server requiring distinct instructions.
Agent
The server is determined by the field of the topic and the specific name of the server that could be utilized to research the topic provided. Agents are categorized by their area of expertise, and each server type is associated with a corresponding emoji.

examples:
task: "should I invest in apple stocks?"
response: 
{
    "server": "💰 Finance Agent",
    "agent_role_prompt: "You are a seasoned finance analyst AI assistant. Your primary goal is to compose comprehensive, astute, impartial, and methodically arranged financial reports based on provided data and trends."
}
task: "could reselling sneakers become profitable?"
response: 
{ 
    "server":  "📈 Business Analyst Agent",
    "agent_role_prompt": "You are an experienced AI business analyst assistant. Your main objective is to produce comprehensive, insightful, impartial, and systematically structured business reports based on provided business data, market trends, and strategic analysis."
}
task: "what are the most interesting sites in Tel Aviv?"
response:
{
    "server:  "🌍 Travel Agent",
    "agent_role_prompt": "You are a world-travelled AI tour guide assistant. Your main purpose is to draft engaging, insightful, unbiased, and well-structured travel reports on given locations, including history, attractions, and cultural insights."
}
"""


def generate_summary_prompt(query, data):
    """Generates the summary prompt for the given question and text.
    Args: question (str): The question to generate the summary prompt for
            text (str): The text to generate the summary prompt for
    Returns: str: The summary prompt for the given question and text
    """

    return (
        f'{data}\n Using the above text, summarize it based on the following task or query: "{query}".\n If the '
        f"query cannot be answered using the text, YOU MUST summarize the text in short.\n Include all factual "
        f"information such as numbers, stats, quotes, etc if available. "
    )


################################################################################################

# DETAILED REPORT PROMPTS


def generate_subtopics_prompt() -> str:
    return """
Provided the main topic:

{task}

and research data:

{data}

- Construct a list of subtopics which indicate the headers of a report document to be generated on the task. 
- These are a possible list of subtopics : {subtopics}.
- There should NOT be any duplicate subtopics.
- Limit the number of subtopics to a maximum of {max_subtopics}
- Finally order the subtopics by their tasks, in a relevant and meaningful order which is presentable in a detailed report

"IMPORTANT!":
- Every subtopic MUST be relevant to the main topic and provided research data ONLY!

{format_instructions}
"""


def generate_subtopic_report_prompt(
    current_subtopic,
    existing_headers: list,
    relevant_written_contents: list,
    main_topic: str,
    context,
    report_format: str = "apa",
    max_subsections=5,
    total_words=800,
    tone: Tone = Tone.Objective,
) -> str:
    return f"""
"Context":
"{context}"

"Main Topic and Subtopic":
Using the latest information available, construct a detailed report on the subtopic: {current_subtopic} under the main topic: {main_topic}.
You must limit the number of subsections to a maximum of {max_subsections}.

"Content Focus":
- The report should focus on answering the question, be well-structured, informative, in-depth, and include facts and numbers if available.
- Use markdown syntax and follow the {report_format.upper()} format.

"IMPORTANT:Content and Sections Uniqueness":
- This part of the instructions is crucial to ensure the content is unique and does not overlap with existing reports.
- Carefully review the existing headers and existing written contents provided below before writing any new subsections.
- Prevent any content that is already covered in the existing written contents.
- Do not use any of the existing headers as the new subsection headers.
- Do not repeat any information already covered in the existing written contents or closely related variations to avoid duplicates.
- If you have nested subsections, ensure they are unique and not covered in the existing written contents.
- Ensure that your content is entirely new and does not overlap with any information already covered in the previous subtopic reports.

"Existing Subtopic Reports":
- Existing subtopic reports and their section headers:

    {existing_headers}

- Existing written contents from previous subtopic reports:

    {relevant_written_contents}

"Structure and Formatting":
- As this sub-report will be part of a larger report, include only the main body divided into suitable subtopics without any introduction or conclusion section.

- You MUST include markdown hyperlinks to relevant source URLs wherever referenced in the report, for example:

    ### Section Header
    
    This is a sample text. ([url website](url))

- Use H2 for the main subtopic header (##) and H3 for subsections (###).
- Use smaller Markdown headers (e.g., H2 or H3) for content structure, avoiding the largest header (H1) as it will be used for the larger report's heading.
- Organize your content into distinct sections that complement but do not overlap with existing reports.
- When adding similar or identical subsections to your report, you should clearly indicate the differences between and the new content and the existing written content from previous subtopic reports. For example:

    ### New header (similar to existing header)

    While the previous section discussed [topic A], this section will explore [topic B]."

"Date":
Assume the current date is {datetime.now(timezone.utc).strftime('%B %d, %Y')} if required.

"IMPORTANT!":
- The focus MUST be on the main topic! You MUST Leave out any information un-related to it!
- Must NOT have any introduction, conclusion, summary or reference section.
- You MUST include hyperlinks with markdown syntax ([url website](url)) related to the sentences wherever necessary.
- You MUST mention the difference between the existing content and the new content in the report if you are adding the similar or same subsections wherever necessary.
- The report should have a minimum length of {total_words} words.
- Use an {tone.value} tone throughout the report.
"""


def generate_draft_titles_prompt(
    current_subtopic: str,
    main_topic: str,
    context: str,
    max_subsections: int = 5
) -> str:
    return f"""
"Context":
"{context}"

"Main Topic and Subtopic":
Using the latest information available, construct a draft section title headers for a detailed report on the subtopic: {current_subtopic} under the main topic: {main_topic}.

"Task":
1. Create a list of draft section title headers for the subtopic report.
2. Each header should be concise and relevant to the subtopic.
3. The header should't be too high level, but detailed enough to cover the main aspects of the subtopic.
4. Use markdown syntax for the headers, using H3 (###) as H1 and H2 will be used for the larger report's heading.
5. Ensure the headers cover main aspects of the subtopic.

"Structure and Formatting":
Provide the draft headers in a list format using markdown syntax, for example:

### Header 1
### Header 2
### Header 3

"IMPORTANT!":
- The focus MUST be on the main topic! You MUST Leave out any information un-related to it!
- Must NOT have any introduction, conclusion, summary or reference section.
- Focus solely on creating headers, not content.
"""

def generate_report_introduction(question: str, research_summary: str = "") -> str:
    return f"""{research_summary}\n 
Using the above latest information, Prepare a detailed report introduction on the topic -- {question}.
- The introduction should be succinct, well-structured, informative with markdown syntax.
- As this introduction will be part of a larger report, do NOT include any other sections, which are generally present in a report.
- The introduction should be preceded by an H1 heading with a suitable topic for the entire report.
- You must include hyperlinks with markdown syntax ([url website](url)) related to the sentences wherever necessary.
Assume that the current date is {datetime.now(timezone.utc).strftime('%B %d, %Y')} if required.
"""

def generate_report_conclusion(report_content: str) -> str:
    prompt = f"""
    Based on the following research report, please write a concise conclusion that summarizes the main findings and their implications:

    {report_content}

    Your conclusion should:
    1. Recap the main points of the research
    2. Highlight the most important findings
    3. Discuss any implications or next steps
    4. Be approximately 2-3 paragraphs long
    
    If there is no "## Conclusion" section title written at the end of the report, please add it to the top of your conclusion. 
    You must include hyperlinks with markdown syntax ([url website](url)) related to the sentences wherever necessary.
    
    Write the conclusion:
    """

    return prompt


report_type_mapping = {
    ReportType.ResearchReport.value: generate_report_prompt,
    ReportType.ResourceReport.value: generate_resource_report_prompt,
    ReportType.OutlineReport.value: generate_outline_report_prompt,
    ReportType.CustomReport.value: generate_custom_report_prompt,
    ReportType.SubtopicReport.value: generate_subtopic_report_prompt,
}


def get_prompt_by_report_type(report_type):
    prompt_by_type = report_type_mapping.get(report_type)
    default_report_type = ReportType.ResearchReport.value
    if not prompt_by_type:
        warnings.warn(
            f"Invalid report type: {report_type}.\n"
            f"Please use one of the following: {', '.join([enum_value for enum_value in report_type_mapping.keys()])}\n"
            f"Using default report type: {default_report_type} prompt.",
            UserWarning,
        )
        prompt_by_type = report_type_mapping.get(default_report_type)
    return prompt_by_type
