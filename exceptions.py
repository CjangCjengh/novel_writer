"""
Custom exception types for the novel_writer project.
"""

import re


class ContextLengthExceededError(RuntimeError):
    """Raised when the request exceeds the model's maximum context length.
    Both OpenAI and custom API error formats are detected.
    """

    def __init__(self, message: str = "Context length exceeded",
                 input_tokens: int | None = None,
                 max_tokens: int | None = None):
        super().__init__(message)
        self.input_tokens = input_tokens
        self.max_tokens = max_tokens

    @staticmethod
    def check_and_raise(error_message: str):
        """Check if the error message indicates a context length exceeded error.
        If so, raise ContextLengthExceededError.

        Compatible formats:
        1. OpenAI standard format:
           "This model's maximum context length is 40964 tokens. However, your request
            has 42685 input tokens."
        2. Other common formats:
           "maximum context length" / "context_length_exceeded" / "token limit" /
           "input too long" / "request too large" / "max_tokens" / "context window"
        """
        msg_lower = error_message.lower()

        # Detect common context-length-exceeded keywords
        context_length_patterns = [
            "maximum context length",
            "context_length_exceeded",
            "context length exceeded",
            "token limit exceeded",
            "input too long",
            "request too large",
            "max_tokens",
            "context window",
            "reduce the length",
            "input_tokens",
            "too many tokens",
            "exceeds the model",
            "prompt is too long",
        ]

        is_context_error = any(p in msg_lower for p in context_length_patterns)
        if not is_context_error:
            return  # Not a token limit error, skip

        # Try to extract numeric values from the OpenAI standard error message
        input_tokens = None
        max_tokens = None

        # "maximum context length is 40964 tokens"
        max_match = re.search(r'maximum context length is (\d+)', error_message)
        if max_match:
            max_tokens = int(max_match.group(1))

        # "your request has 42685 input tokens" or "value=42685"
        # or OpenAI format: "your messages resulted in 130000 tokens"
        input_match = re.search(r'has (\d+) (?:input )?tokens', error_message)
        if not input_match:
            input_match = re.search(r'resulted in (\d+) tokens', error_message)
        if not input_match:
            input_match = re.search(r'value=(\d+)', error_message)
        if input_match:
            input_tokens = int(input_match.group(1))

        raise ContextLengthExceededError(
            message=error_message,
            input_tokens=input_tokens,
            max_tokens=max_tokens,
        )
