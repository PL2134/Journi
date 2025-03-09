from typing import Any, Optional
from smolagents.tools import Tool
from smolagents.agent_types import AgentImage

class FinalAnswerTool(Tool):
    name = "final_answer"
    description = "Provides a final answer to the given problem."
    inputs = {'answer': {'type': 'any', 'description': 'The final answer to the problem'}}
    output_type = "any"

    def forward(self, answer: Any) -> Any:
        # Check if the answer is an image path
        if isinstance(answer, str) and ('/tmp/gradio/' in answer or answer.endswith(('.png', '.jpg', '.jpeg', '.webp'))):
            # Return as AgentImage for proper handling by stream_to_gradio
            return AgentImage(answer)
        
        # Return the original answer for non-image responses
        return answer

    def __init__(self, *args, **kwargs):
        super().__init__()  # This is what was missing
        self.is_initialized = False