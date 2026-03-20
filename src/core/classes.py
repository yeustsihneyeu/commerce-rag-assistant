from string import Formatter
from typing import Any, Literal

from pydantic import BaseModel, model_validator


class Prompt(BaseModel):
    model_type: Literal["foundation", "ollama"]
    model_name: str
    prompt_text: str
    version: str
    variables: dict[str, Any]

    @staticmethod
    def _extract_variables(prompt_text: str) -> set[str]:
        return {
            field_name
            for _, field_name, _, _ in Formatter().parse(prompt_text)
            if field_name
        }

    @model_validator(mode="after")
    def validate_prompt_variables(self) -> "Prompt":
        required_variables = self._extract_variables(self.prompt_text)
        missing_variables = required_variables - set(self.variables)

        if missing_variables:
            missing = ", ".join(sorted(missing_variables))
            raise ValueError(f"Prompt variables missing for placeholders: {missing}")

        return self

    def render(self, **kwargs) -> str:
        context = {**self.variables, **kwargs}
        required_variables = self._extract_variables(self.prompt_text)
        missing_variables = required_variables - set(context)

        if missing_variables:
            missing = ", ".join(sorted(missing_variables))
            raise ValueError(f"Missing render variables for prompt: {missing}")

        return self.prompt_text.format(**context)
