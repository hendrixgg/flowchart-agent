from typing import List, Callable, Any, Tuple, Dict


class FlowchartTask:
    def __init__(self, name, instructions, inputFormat, outputFormat):
        self.name = name
        self.instructions = instructions
        self.inputFormat = inputFormat
        self.outputFormat = outputFormat

    def __repr__(self):
        return f"FlowchartNode(name={self.name.__repr__()}, instructions={self.instructions.__repr__()}, inputFormat={self.inputFormat.__repr__()}, outputFormat={self.outputFormat.__repr__()})"


class FlowchartTaskResult:
    def __init__(self, value: Any, executionDetails: Dict):
        self.value = value
        self.executionDetails = executionDetails

    def __repr__(self):
        return f"FlowchartNodeOutput(value={self.value.__repr__()}, executionDetails={self.executionDetails.__repr__()})"


# This is a linear flowchart structure, the nodes are connected in a sequence.
Flowchart = List[FlowchartTask]


def execute_Flowchart(flowchart: Flowchart, function: Callable[[FlowchartTask, FlowchartTaskResult], Any], input: Any) -> List[FlowchartTaskResult]:
    """
    Execute a Flowchart and return the output.
    This function .
    """
    assert isinstance(
        flowchart, list), "flowchart must be a list of FlowchartNode instances"

    results = [FlowchartTaskResult(value=input, executionDetails={
                                   "initial_input": input})]
    for node in flowchart:
        results.append(function(node, results[-1].value))

    return results  # return all outputs, including the initial input as the first element
