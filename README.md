# flowchart-agent

## example output from test.py

Testing execute_FlowchartNode:
Node:
```
FlowchartNode(name='Test Node', instructions='This is a test node for the flowchart. For this test, just return the input as output and do not change it.', inputFormat='Input format example', outputFormat='Output format example')
```
Input:
```
Hl};.w-d$7
```
Result:
```
Node Name: Test Node
Instruction: This is a test node for the flowchart. For this test, just return the input as output and do not change it.
Input: Hl};.w-d$7

Output: Hl};.w-d$7

Input Format: Input format example
Output Format: Output format example
```
Testing execute_Flowchart:
Flowchart:
```
[FlowchartNode(name='Node 1', instructions='convert the input to a single number in base 10.', inputFormat="a number in english wording such as 'forty two'", outputFormat='just a single decimal number'), FlowchartNode(name='Node 2', instructions="convert the base 10 number to an english worded representation such as 'ten thousand' or 'fifty five'.", inputFormat='a number is base 10', outputFormat='number in english wording')]
```
Input:
```
two hundred and fifty six
```
Result:
```
['To convert the input "two hundred and fifty six" to a single number in base 10, we need to convert each word to its numerical representation and then sum them up.\n\ntwo hundred and fifty six = 2 * 100 + 50 + 6 = 200 + 50 + 6 = 256\n\nTherefore, the output for Node 1 is: 256', 'The output for Node 2 is: two hundred and fifty six']
```
-----------------
All tests passed!
