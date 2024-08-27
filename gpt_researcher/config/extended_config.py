from .config import Config


class ExtConfig(Config):

    def __init__(self, config_file: str = None, **kwargs):
        super().__init__(config_file)
        self.add_custom_config(kwargs) #update the config with custom config
        
    def add_custom_config(self, custom_config: dict) -> None: 
        """Update the config with custom config."""	
        for key, value in custom_config.items():
            setattr(self, key, value)


#old but working
# class ExtendedConfig (Config):
#     """Config class for GPT Researcher."""

#     def __init__(self,
#                  retrievers: str | None = None,
#                  llm_provider: str | None = None,
#                  fast_llm_model: str | None = None,
#                  smart_llm_model: str | None = None,
#                  fast_token_limit: int | None = None,
#                  smart_token_limit: int | None = None,
#                  browse_chunk_max_length: int | None = None,
#                  summary_token_limit: int | None = None,
#                  llm_temperature: float | None = None,
#                  max_search_results_per_query: int | None = None,
#                  total_words: int | None = None,
#                  report_format: str | None = None,
#                  max_iterations: int | None = None,
#                  agent_role: str | None = None,
#                  scraper: str | None = None,
#                  config_file: str = None):
#         """Initialize the config class."""
#         self.config_file = os.path.expanduser(
#             config_file) if config_file else os.getenv('CONFIG_FILE')
#         self.retrievers = self.parse_retrievers(retrievers if retrievers else os.getenv('RETRIEVER', "tavily"))
#         self.embedding_provider = os.getenv('EMBEDDING_PROVIDER', 'openai')
#         self.similarity_threshold = int(
#             os.getenv('SIMILARITY_THRESHOLD', 0.38))
#         self.llm_provider = llm_provider if llm_provider else os.getenv(
#             'LLM_PROVIDER', "openai")
#         self.ollama_base_url = os.getenv('OLLAMA_BASE_URL', None)
#         self.fast_llm_model = fast_llm_model if fast_llm_model else os.getenv(
#             'FAST_LLM_MODEL', "gpt-3.5-turbo-16k")
#         self.smart_llm_model = smart_llm_model if smart_llm_model else os.getenv(
#             'SMART_LLM_MODEL', "gpt-4o")
#         self.llm_model = "gpt-4o-mini" 
#         self.fast_token_limit = fast_token_limit if fast_token_limit else int(
#             os.getenv('FAST_TOKEN_LIMIT', 2000))
#         self.smart_token_limit = smart_token_limit if smart_token_limit else int(
#             os.getenv('SMART_TOKEN_LIMIT', 4000))
#         self.browse_chunk_max_length = browse_chunk_max_length if browse_chunk_max_length else int(
#             os.getenv('BROWSE_CHUNK_MAX_LENGTH', 8192))
#         self.summary_token_limit = summary_token_limit if summary_token_limit else int(
#             os.getenv('SUMMARY_TOKEN_LIMIT', 700))
#         self.llm_temperature = llm_temperature if llm_temperature else float(
#             os.getenv('LLM_TEMPERATURE', 0.55))
#         self.user_agent = os.getenv('USER_AGENT', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                                     "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0")
#         self.max_search_results_per_query = max_search_results_per_query if max_search_results_per_query else int(
#             os.getenv('MAX_SEARCH_RESULTS_PER_QUERY', 5))
#         self.memory_backend = os.getenv('MEMORY_BACKEND', "local")
#         self.total_words = total_words if total_words else int(
#             os.getenv('TOTAL_WORDS', 800))
#         self.report_format = report_format if report_format else os.getenv(
#             'REPORT_FORMAT', "APA")
#         self.max_iterations = max_iterations if max_iterations else int(
#             os.getenv('MAX_ITERATIONS', 3))
#         self.agent_role = agent_role if agent_role else os.getenv(
#             'AGENT_ROLE', None)
#         self.scraper = scraper if scraper else os.getenv("SCRAPER", "bs")
#         self.max_subtopics = os.getenv("MAX_SUBTOPICS", 3)
#         self.report_source = os.getenv("REPORT_SOURCE", None)
#         self.doc_path = os.getenv("DOC_PATH", "")
#         self.llm_kwargs = {}

#         # The last load to update the config
#         self.load_config_file()
#         if not hasattr(self, "llm_kwargs"):
#             self.llm_kwargs = {}

#         if self.doc_path:
#             self.validate_doc_path()



