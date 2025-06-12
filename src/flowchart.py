from typing import List, Callable, Any


class FlowchartNode:
    def __init__(self, name, instructions, inputFormat=None, outputFormat=None):
        self.name = name
        self.instructions = instructions
        self.inputFormat = inputFormat
        self.outputFormat = outputFormat

    def __repr__(self):
        return f"FlowchartNode(name={self.name.__repr__()}, instructions={self.instructions.__repr__()}, inputFormat={self.inputFormat.__repr__()}, outputFormat={self.outputFormat.__repr__()})"


# This is a linear flowchart structure, the nodes are connected in a sequence.
Flowchart = List[FlowchartNode]


def execute_FlowchartNode(node: FlowchartNode, function: Callable[[FlowchartNode], Any], input) -> str:
    """
    Execute a FlowchartNode and return the output.
    This function simulates the execution of a flowchart node.
    """
    assert isinstance(
        node, FlowchartNode), "node must be a FlowchartNode instance"

    # Here we would normally call an LLM or some processing function
    # For this example, we will just return a placeholder output
    return function(node, input)


def execute_Flowchart(flowchart: Flowchart, function: Callable[[FlowchartNode], Any], input) -> List[str]:
    """
    Execute a Flowchart and return the output.
    This function simulates the execution of a flowchart.
    """
    assert isinstance(
        flowchart, list), "flowchart must be a list of FlowchartNode instances"

    outputs = [input]
    for node in flowchart:
        outputs.append(execute_FlowchartNode(node, function, outputs[-1]))

    return outputs[1:]  # Return all outputs except the initial input
