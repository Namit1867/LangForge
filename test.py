from langchain.tools import BaseTool
import requests

class WikipediaSearchTool(BaseTool):
    def __init__(self, language='en'):
        self.api_url = f"https://{language}.wikipedia.org/w/api.php"
        self.language = language

    def search(self, query, limit=5):
        params = {
            'action': 'query',
            'list': 'search',
            'srsearch': query,
            'format': 'json',
            'srlimit': limit
        }
        response = requests.get(self.api_url, params=params)
        response.raise_for_status()
        return response.json()

    def get_page_content(self, page_id):
        params = {
            'action': 'query',
            'pageids': page_id,
            'prop': 'extracts',
            'explaintext': True,
            'format': 'json'
        }
        response = requests.get(self.api_url, params=params)
        response.raise_for_status()
        return response.json()

    def get_recent_changes(self, limit=5):
        params = {
            'action': 'query',
            'list': 'recentchanges',
            'rclimit': limit,
            'format': 'json'
        }
        response = requests.get(self.api_url, params=params)
        response.raise_for_status()
        return response.json()

    def _run(self, query):
        search_results = self.search(query)
        if not search_results['query']['search']:
            return "No results found."

        page_id = search_results['query']['search'][0]['pageid']
        page_content = self.get_page_content(page_id)
        page_extract = page_content['query']['pages'][str(page_id)]['extract']
        
        return page_extract

# Example usage:
tool = WikipediaSearchTool()
print(tool.api_url)
# print(tool.run("Python programming language"))