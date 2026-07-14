from graph import graph
from langchain_core.messages import HumanMessage


def chat_with_ai(message):

    result = graph.invoke(
        {
            "messages":[
                HumanMessage(
                    content=message
                )
            ]
        }
    )


    return result["messages"][-1].content