"""
LLM Client - Unified interface layer.
Auto-detects available backends (OpenAI / local stream-server).
Even if one backend file is deleted, the other still works.
"""
import config


class LLMClient:
    """
    Unified LLM client.
    Delegates to the appropriate backend based on api_mode.
    """

    def __init__(self, api_mode: str = None):
        self.api_mode = api_mode or config.API_MODE
        self._backend = None
        self._init_backend()

    def _init_backend(self):
        """Initialize the appropriate backend."""
        from locales import get_locale
        ui = get_locale().UI

        if self.api_mode == "openai":
            try:
                from llm_openai import OpenAIBackend
                self._backend = OpenAIBackend()
            except ImportError as e:
                raise ImportError(ui["cannot_load_openai"].format(error=e))
        elif self.api_mode == "local":
            try:
                from llm_local import LocalBackend
                self._backend = LocalBackend()
            except ImportError as e:
                raise ImportError(ui["cannot_load_local"].format(error=e))
        else:
            raise ValueError(ui["unsupported_api_mode"].format(mode=self.api_mode))

    def chat(self, system_prompt: str, messages: list[dict], **kwargs) -> str | None:
        """
        Unified chat interface, delegating to the concrete backend.

        Args:
            system_prompt: System prompt text.
            messages: Message list, format [{"role": "user"/"assistant", "content": "..."}].
            **kwargs: Extra parameters (can override config defaults).

        Returns:
            Model response text, or None on failure.
        """
        return self._backend.chat(system_prompt, messages, **kwargs)


def get_available_backends() -> list[str]:
    """Detect which backends are currently available."""
    available = []
    try:
        import llm_openai  # noqa: F401
        available.append("openai")
    except ImportError:
        pass
    try:
        import llm_local  # noqa: F401
        available.append("local")
    except ImportError:
        pass
    return available


# Global singleton
_client: LLMClient | None = None


def get_client(api_mode: str = None) -> LLMClient:
    """Get or create the global LLM client singleton."""
    global _client
    if _client is None or (api_mode and api_mode != _client.api_mode):
        _client = LLMClient(api_mode)
    return _client
