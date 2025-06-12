from flowchart import FlowchartNode

from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

llm = init_chat_model(
    "gpt-3.5-turbo",
    model_provider="openai",
    temperature=0)


def FlowchartNode_to_prompt(node: FlowchartNode, input) -> str:
    """
    Convert a FlowchartNode to a prompt string.
    """
    assert isinstance(
        node, FlowchartNode), "node must be a FlowchartNode instance"

    return f"""Produce the output for the following flowchart node using the provided inputs:
Node Name: {node.name}
Instructionis: {node.instructions}
input Format: {node.inputFormat}
Output Format: {node.outputFormat}
Input: {input}"""


def FlowchartNode_execution_steps(node: FlowchartNode, input: str):
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=FlowchartNode_to_prompt(node, input)),
    ]
    response = llm.invoke(messages)
    messages.append(AIMessage(content=response.content))
    return messages


def FlowchartNode_execution_basic(node: FlowchartNode, input: str) -> str:
    """
    Execute a FlowchartNode and return the output.
    This function simulates the execution of a flowchart node using a basic LLM call.
    """
    assert isinstance(
        node, FlowchartNode), "node must be a FlowchartNode instance"

    return FlowchartNode_execution_steps(node, input)[-1].content
