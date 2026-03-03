"""
OpenAI standard format LLM backend.
Can be used independently - still works even if llm_local.py is deleted.
"""
import sys
import time
import threading

import config
from exceptions import ContextLengthExceededError

# Lock to ensure only one thread prints stream output at a time.
# When multiple threads run concurrently, only the one holding
# the lock will print tokens; others accumulate silently.
_stream_print_lock = threading.Lock()


class OpenAIBackend:
    """OpenAI standard format API backend."""

    def __init__(self):
        from locales import get_locale
        ui = get_locale().UI

        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError(ui["openai_need_package"])

        if not config.OPENAI_API_KEY:
            raise ValueError(ui["openai_no_key"])

        self.client = OpenAI(
            api_key=config.OPENAI_API_KEY,
            base_url=config.OPENAI_BASE_URL,
        )
        print(ui["openai_initialized"].format(model=config.OPENAI_MODEL, url=config.OPENAI_BASE_URL))

    def chat(self, system_prompt: str, messages: list[dict], **kwargs) -> str | None:
        """
        Call the OpenAI standard format API with retry logic.

        Args:
            system_prompt: System prompt text.
            messages: Message list, [{"role": "user"/"assistant", "content": "..."}].
            **kwargs: Extra params (can override config generation params).

        Returns:
            Model response text, or None on failure.
        """
        from locales import get_locale
        ui = get_locale().UI

        for attempt in range(1, config.MAX_RETRIES + 1):
            try:
                return self._call(system_prompt, messages, **kwargs)
            except ContextLengthExceededError:
                # Context length exceeded — no retry, re-raise immediately
                raise
            except Exception as e:
                # Check if the OpenAI SDK BadRequestError contains a token-limit message
                err_msg = str(e)
                try:
                    ContextLengthExceededError.check_and_raise(err_msg)
                except ContextLengthExceededError:
                    raise
                print(ui["openai_attempt_failed"].format(n=attempt, error=e))
                if attempt < config.MAX_RETRIES:
                    wait = config.RETRY_DELAY * attempt
                    print(ui["openai_retry_wait"].format(wait=wait))
                    time.sleep(wait)
                else:
                    print(ui["openai_max_retries"].format(max=config.MAX_RETRIES))
                    return None

    def _call(self, system_prompt: str, messages: list[dict], **kwargs) -> str:
        """Execute a single API call (supports both stream and non-stream modes)."""
        full_messages = []
        if system_prompt:
            full_messages.append({"role": "system", "content": system_prompt})
        full_messages.extend(messages)

        stream_enabled = kwargs.get("stream", config.STREAM_MODE)

        if stream_enabled:
            return self._call_stream(full_messages, **kwargs)
        else:
            response = self.client.chat.completions.create(
                model=kwargs.get("model", config.OPENAI_MODEL),
                messages=full_messages,
                temperature=kwargs.get("temperature", config.TEMPERATURE),
                top_p=kwargs.get("top_p", config.TOP_P),
                max_tokens=kwargs.get("max_tokens", config.MAX_OUTPUT_TOKENS),
            )
            return response.choices[0].message.content

    def _call_stream(self, full_messages: list[dict], **kwargs) -> str:
        """Execute a streaming API call, printing tokens in real-time.

        When multiple threads call this concurrently, only the thread
        that acquires _stream_print_lock will print tokens to stdout;
        other threads accumulate content silently.
        """
        # Non-blocking acquire: only one thread wins the right to print
        can_print = _stream_print_lock.acquire(blocking=False)

        try:
            stream = self.client.chat.completions.create(
                model=kwargs.get("model", config.OPENAI_MODEL),
                messages=full_messages,
                temperature=kwargs.get("temperature", config.TEMPERATURE),
                top_p=kwargs.get("top_p", config.TOP_P),
                max_tokens=kwargs.get("max_tokens", config.MAX_OUTPUT_TOKENS),
                stream=True,
            )

            full_content = ""
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    content_piece = chunk.choices[0].delta.content
                    full_content += content_piece
                    # Only the thread holding the lock prints
                    if can_print:
                        print(content_piece, end="", flush=True)

            # Newline after stream ends
            if full_content and can_print:
                print()

            if not full_content:
                raise RuntimeError("Empty response from streaming API")

            return full_content
        finally:
            if can_print:
                _stream_print_lock.release()
