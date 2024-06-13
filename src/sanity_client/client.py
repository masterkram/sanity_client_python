import requests

from src.sanity_client.exceptions import *


class SanityClient:
    project_id: str
    dataset: str
    token: str
    use_cdn: bool

    def __init__(
        self, project_id: str, dataset: str, token: str = None, use_cdn: bool = True
    ) -> None:
        self.project_id = project_id
        self.dataset = dataset
        self.token = token
        self.use_cdn = use_cdn

    def _build_host(self) -> str:
        return f"{self.project_id}.{'apicdn' if self.use_cdn else 'api'}.sanity.io"

    def _build_path(self) -> str:
        return f"/v1/data/query/{self.dataset}"

    def _parse_response(self, response: requests.Response):
        if response.status_code == 200:
            responseJson = response.json()
            return responseJson["result"]
        if response.status_code == 400:
            raise BadRequestException(response.text)
        if response.status_code in [401, 403]:
            raise UnauthorizedException(response.text)

        raise Exception(
            f"Error occured while communicating with the server {response.status_code}"
        )

    def fetch(self, query: str, params: dict = {}):
        query_parameters = {"query": query}
        url = f"https://{self._build_host()}{self._build_path()}"
        response: requests.Response = requests.get(url=url, params=query_parameters)
        return self._parse_response(response)
