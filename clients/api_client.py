import time
import json
import uuid
import logging
from typing import Any, Dict, Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config.config import Config
from utils.loggers import get_logger


class APIClient:
    """
    Production-grade reusable HTTP client.

    Features:
    - Connection pooling via requests.Session
    - Retry strategy for transient failures
    - Configurable timeout
    - Centralized request handling
    - Structured logging with request tracing
    - Automatic error handling
    - Authentication support
    """

    def __init__(self):
        self.base_url: str = Config.BASE_URL.rstrip("/")
        self.timeout: int = Config.TIMEOUT

        self.logger = get_logger(__name__)

        self.session = requests.Session()

        self._set_default_headers()
        self._configure_retries()

        self.token: Optional[str] = None

    # ----------------------------
    # Setup Methods
    # ----------------------------

    def _set_default_headers(self) -> None:
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "pytest-api-client",
            "x-api-key": Config.API_KEY
        })

    def _configure_retries(self) -> None:
        retry_strategy = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE"],
            raise_on_status=False
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)

        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    # ----------------------------
    # Utility Methods
    # ----------------------------

    def _build_url(self, endpoint: str) -> str:
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def _add_auth_header(self):
        if self.token:
            self.session.headers["Authorization"] = f"Bearer {self.token}"

    # ----------------------------
    # Core Request Handler
    # ----------------------------

    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        request_id = str(uuid.uuid4())[:8]
        url = self._build_url(endpoint)

        self.logger.info(f"[{request_id}] REQUEST -> {method} {url}")

        if "json" in kwargs and kwargs["json"] is not None:
            try:
                pretty_payload = json.dumps(kwargs["json"], indent=2)
                self.logger.info(f"[{request_id}] Payload ->\n{pretty_payload}")
            except Exception:
                self.logger.info(f"[{request_id}] Payload (raw) -> {kwargs['json']}")

        start_time = time.time()

        try:
            self._add_auth_header()

            response = self.session.request(
                method=method,
                url=url,
                timeout=self.timeout,
                **kwargs
            )

            duration = round((time.time() - start_time) * 1000, 2)

            self.logger.info(
                f"[{request_id}] RESPONSE <- {response.status_code} {method} {url} | {duration} ms"
            )

            try:
                pretty_body = json.dumps(response.json(), indent=2)[:500]

                # Always log error responses
                if response.status_code >= 400:
                    self.logger.error(
                        f"[{request_id}] Error Response ->\n{pretty_body}"
                    )

                # Only log success bodies in DEBUG mode
                elif self.logger.isEnabledFor(logging.DEBUG):
                    self.logger.debug(
                        f"[{request_id}] Response Body ->\n{pretty_body}"
                    )

            except Exception:
                if response.status_code >= 400:
                    self.logger.error(
                        f"[{request_id}] Response Text -> {response.text[:500]}"
                    )
            return response

        except requests.exceptions.Timeout:
            self.logger.error(f"[{request_id}] TIMEOUT -> {method} {url}")
            raise AssertionError(f"Request timed out: {method} {url}")

        except requests.exceptions.ConnectionError:
            self.logger.error(f"[{request_id}] CONNECTION ERROR -> {method} {url}")
            raise AssertionError(f"Connection error: {method} {url}")

        except requests.exceptions.RequestException as e:
            self.logger.error(
                f"[{request_id}] REQUEST FAILED -> {method} {url} | {str(e)}"
            )
            raise AssertionError(f"Unexpected request error: {str(e)}")

    # ----------------------------
    # Public HTTP Methods
    # ----------------------------

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, payload: Optional[Dict] = None, **kwargs) -> requests.Response:
        return self._request("POST", endpoint, json=payload, **kwargs)

    def put(self, endpoint: str, payload: Optional[Dict] = None, **kwargs) -> requests.Response:
        return self._request("PUT", endpoint, json=payload, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("DELETE", endpoint, **kwargs)

    # ----------------------------
    # Authentication
    # ----------------------------

    def authenticate(self) -> str:
        """
        Fetch auth token and attach to session headers.
        """
        payload = {
            "email": Config.EMAIL,
            "password": Config.PASSWORD
        }

        response = self.post("/login", payload)

        if response.status_code != 200:
            raise AssertionError(
                f"Auth failed: {response.status_code} {response.text}"
            )

        token = response.json().get("token")

        if not token:
            raise AssertionError("Auth token not found in response")

        self.token = token 

        self.session.headers.update({
            "Authorization": f"Bearer {token}"
        })

        return token