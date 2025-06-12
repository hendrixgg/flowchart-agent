
from flowchart import FlowchartNode, execute_FlowchartNode, execute_Flowchart
from prompt_chain import FlowchartNode_to_prompt, FlowchartNode_execution_basic

import random
import string


def generate_random_string(length: int) -> str:
    """Generate a string of specified length using letters, digits, and punctuation using python 'random'."""
    assert length >= 0, "Length must be a nonnegative integer"
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    return ''.join(random.choice(characters) for _ in range(length))


def test_execute_FlowchartNode(verbose=False):
    """Test the execute_FlowchartNode function."""
    node = FlowchartNode(
        name="Test Node",
        instructions="This is a test node for the flowchart. For this test, just return the input as output and do not change it.",
        inputFormat="Input format example",
        outputFormat="Output format example"
    )

    input = generate_random_string(10)
    result = execute_FlowchartNode(node, FlowchartNode_execution_basic, input)
    if verbose:
        print("Testing execute_FlowchartNode:")
        print(f"Node:\n```\n{node}\n```")
        print(f"Input:\n```\n{input}\n```")
        print(f"Result:\n```\n{result}\n```")

    assert isinstance(result, str), "Result should be a string"
    assert len(result) > 0, "Result should not be empty"


def test_execute_Flowchart(verbose=False):
    """Test the execute_Flowchart function."""
    node1 = FlowchartNode(
        name="Node 1",
        instructions="convert the input to a single number in base 10.",
        inputFormat="a number in english wording such as 'forty two'",
        outputFormat="just a single decimal number"
    )
    node2 = FlowchartNode(
        name="Node 2",
        instructions="convert the base 10 number to an english worded representation such as 'ten thousand' or 'fifty five'.",
        inputFormat="a number is base 10",
        outputFormat="number in english wording"
    )

    flowchart = [node1, node2]
    input = "two hundred and fifty six"
    result = execute_Flowchart(flowchart, FlowchartNode_execution_basic, input)

    if verbose:
        print("Testing execute_Flowchart:")
        print(f"Flowchart:\n```\n{flowchart}\n```")
        print(f"Input:\n```\n{input}\n```")
        print(f"Result:\n```\n{result}\n```")

    assert isinstance(result, list), "Result should be a list"
    assert len(result) == len(
        flowchart), "Result length should match flowchart length"
    for res in result:
        assert isinstance(res, str), "Each result item should be a string"
        assert len(res) > 0, "Each result item should not be empty"


def main():
    """Run all tests."""
    test_execute_FlowchartNode(verbose=True)
    test_execute_Flowchart(verbose=True)
    print("-----------------")
    print("All tests passed!")


if __name__ == "__main__":
    main()
