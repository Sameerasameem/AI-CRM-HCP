from typing import TypedDict, Annotated

from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from langchain_core.messages import SystemMessage

from agent import llm
from tools import tools


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


llm_with_tools = llm.bind_tools(tools)


def chatbot(state: AgentState):

    system_prompt = SystemMessage(
        content="""
You are an AI CRM Assistant.

Whenever the user wants to:
- log an interaction
- search interactions
- generate summary
- recommend next action

ALWAYS use the available tool.

Do not ask unnecessary questions.
"""
    )

    response = llm_with_tools.invoke(
        [system_prompt] + state["messages"]
    )

    return {"messages": [response]}


builder = StateGraph(AgentState)

builder.add_node("chatbot", chatbot)
builder.add_node("tools", ToolNode(tools))

builder.set_entry_point("chatbot")

builder.add_conditional_edges(
    "chatbot",
    tools_condition
)

builder.add_edge(
    "tools",
    "chatbot"
)

graph = builder.compile()