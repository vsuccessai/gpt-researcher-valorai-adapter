from .config import Config


class ExtConfig(Config):

    def __init__(self, config_file: str = None, **kwargs):
        super().__init__(config_file)
        self.add_custom_config(kwargs) #update the config with custom config
        #print("Extended config", self.__dict__)

    @property
    def retrievers(self):
        return self._retrievers
    
    @retrievers.setter
    def retrievers(self, retrievers: str | list[str]):
        if isinstance(retrievers, str):
            self._retrievers = self.parse_retrievers(retrievers)
        else:
            self._retrievers = retrievers        
        
    def add_custom_config(self, custom_config: dict) -> None: 
        """Update the config with custom config."""	
        for key, value in custom_config.items():
            setattr(self, key, value)