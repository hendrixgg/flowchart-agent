from flowchart import FlowchartTask, FlowchartTaskResult

from typing import Dict, Any
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

llm = init_chat_model(
    "gpt-3.5-turbo",
    model_provider="openai",
    temperature=0)


def FlowchartNode_to_prompt(node: FlowchartTask, input: str) -> str:
    """
    Convert a FlowchartNode to a prompt string.
    """
    assert isinstance(
        node, FlowchartTask), "node must be a FlowchartNode instance"

    return f"""Produce the output for the following flowchart node using the provided inputs:
Node Name: {node.name}
Instructions: {node.instructions}
Input Format: {node.inputFormat}
Output Format: {node.outputFormat}
Input: {input}"""


def FlowchartNode_llm_execution(node: FlowchartTask, input: str) -> FlowchartTaskResult:
    """
    Execute a FlowchartNode and return the output.
    This function simulates the execution of a flowchart node using a basic LLM call.

    currently, the audit is just the prompt and the response from the LLM.
    """
    assert isinstance(
        node, FlowchartTask), "node must be a FlowchartNode instance"
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=FlowchartNode_to_prompt(node, input)),
    ]
    response = llm.invoke(messages)
    return FlowchartTaskResult(value=response.content, executionDetails={"promptMessages": messages, "response": response})
