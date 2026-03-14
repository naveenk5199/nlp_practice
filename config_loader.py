import yaml

class ConfigLoader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)

    def get_openai_api_key(self):
        return self.config.get('openai', {}).get('api_key')

    def get_embeddings_settings(self):
        return self.config.get('embeddings', {})

    def get_faiss_indexing_settings(self):
        return self.config.get('faiss_indexing', {})

    def get_pdf_chunking_settings(self):
        return self.config.get('pdf_chunking', {})

    def get_file_paths(self):
        return self.config.get('file_paths', {})
