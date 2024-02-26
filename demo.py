# client = OpenAI(api_key="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")
import os
os.environ['OPENAI_API_KEY'] = "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"
from langchain_openai import ChatOpenAI

# We will set streaming=True so that we can stream tokens
# See the streaming section for more information on this.
model = ChatOpenAI(temperature=0, streaming=True)




# Import things that are needed generically
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool


@tool
def search(query: str) -> str:
    """Look up things online."""
    return "LangChain"


from langchain.tools.render import format_tool_to_openai_function
from langchain_core.utils.function_calling import convert_to_openai_function


tools = [search]
functions = [convert_to_openai_function(t) for t in tools]
model = model.bind_functions(functions)
