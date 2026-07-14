from typing import TypedDict

from langgraph.graph import StateGraph, END
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    ToolMessage
)

from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

from tools import (
    log_interaction,
    edit_interaction,
    get_interaction,
    list_interactions,
    summarize_interactions
)


load_dotenv()


class AgentState(TypedDict):
    messages: list



llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)


tools = [
    log_interaction,
    edit_interaction,
    get_interaction,
    list_interactions,
    summarize_interactions
]


llm_with_tools = llm.bind_tools(tools)



def chatbot(state: AgentState):

    system_prompt = SystemMessage(
        content="""
You are an AI CRM assistant for Healthcare Professionals.

Your tasks:
1. Answer CRM related questions.
2. If user asks to save/log doctor interaction,
   use log_interaction tool.

Example:

User:
Log my meeting with Dr Kumar about diabetes medicine.

Use tool:
log_interaction(
details="Meeting with Dr Kumar about diabetes medicine"
)
"""
    )


    response = llm_with_tools.invoke(
        [
            system_prompt
        ] + state["messages"]
    )


    return {
        "messages":[response]
    }



def tool_node(state: AgentState):

    last_message = state["messages"][-1]

    results = []


    for tool_call in last_message.tool_calls:

        if tool_call["name"] == "log_interaction":

            result = log_interaction.invoke(
                tool_call["args"]
            )

            results.append(
                ToolMessage(
                    content=result,
                    tool_call_id=tool_call["id"]
                )
            )
        if tool_call["name"] == "edit_interaction":

            result = edit_interaction.invoke(
                tool_call["args"]
            )

            results.append(
                ToolMessage(
                    content=result,
                    tool_call_id=tool_call["id"]
                )
            )
        if tool_call["name"] == "get_interaction":
    
            result = get_interaction.invoke(
                tool_call["args"]
            )

            results.append(
                ToolMessage(
                    content=result,
                    tool_call_id=tool_call["id"]
                )
            )
        if tool_call["name"] == "list_interactions":

            result = list_interactions.invoke({})

            results.append(
                ToolMessage(
                    content=result,
                    tool_call_id=tool_call["id"]
                )
            )


        if tool_call["name"] == "summarize_interactions":

            result = summarize_interactions.invoke({})

            results.append(
                ToolMessage(
                    content=result,
                    tool_call_id=tool_call["id"]
                )
            )


    return {
        "messages": results
    }




def should_continue(state):

    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return END



graph_builder = StateGraph(AgentState)


graph_builder.add_node(
    "chatbot",
    chatbot
)


graph_builder.add_node(
    "tools",
    tool_node
)


graph_builder.set_entry_point(
    "chatbot"
)


graph_builder.add_conditional_edges(
    "chatbot",
    should_continue,
    {
        "tools":"tools",
        END:END
    }
)


graph_builder.add_edge(
    "tools",
    END
)


graph = graph_builder.compile()