# flowchart-agent

## Flowchart Schema

```
data FlowchartTask = Task
    { inputFormat :: String
    , instructions :: String
    , outputFormat :: String
    }
```


```
data TaskResult = TaskResult
    { resultValue :: a
    , executionDetails :: Dict
    }
```

Potential Improvements or Modifications:
- there could be two stages to the creation of a flowchart, definition of natural language tasks and possibly some pure code tasks, conversion of natural language tasks into functions that take in any input and always produce the output of type TaskResult.
- each flowchart "task" could be a coroutine that takes a single input to run instead of just a task description object. this would allow for asynchronous execution of a directed acyclic graph of tasks


## example output from test.py

Testing FlowchartNode_llm_execution:
```json
{
  "node": {
    "name": "Test Task",
    "instructions": "This is a test node for the flowchart. For this test, just return the input as output and do not change it.",
    "inputFormat": "some string input",
    "outputFormat": "the same format as the input"
  },
  "input": "1dk)G\"]7~c",
  "result": {
    "value": "The output for the \"Test Task\" node with the input \"1dk)G\"]7~c\" is: 1dk)G\"]7~c",
    "executionDetails": {
      "promptMessages": [
        {
          "content": "You are a helpful assistant.",
          "additional_kwargs": {},
          "response_metadata": {},
          "type": "system",
          "name": null,
          "id": null
        },
        {
          "content": "Produce the output for the following flowchart node using the provided inputs:\nNode Name: Test Task\nInstructions: This is a test node for the flowchart. For this test, just return the input as output and do not change it.\nInput Format: some string input\nOutput Format: the same format as the input\nInput: 1dk)G\"]7~c",
          "additional_kwargs": {},
          "response_metadata": {},
          "type": "human",
          "name": null,
          "id": null,
          "example": false
        }
      ],
      "response": {
        "content": "The output for the \"Test Task\" node with the input \"1dk)G\"]7~c\" is: 1dk)G\"]7~c",
        "additional_kwargs": {
          "refusal": null
        },
        "response_metadata": {
          "token_usage": {
            "completion_tokens": 33,
            "prompt_tokens": 94,
            "total_tokens": 127,
            "completion_tokens_details": {
              "accepted_prediction_tokens": 0,
              "audio_tokens": 0,
              "reasoning_tokens": 0,
              "rejected_prediction_tokens": 0
            },
            "prompt_tokens_details": {
              "audio_tokens": 0,
              "cached_tokens": 0
            }
          },
          "model_name": "gpt-3.5-turbo-0125",
          "system_fingerprint": null,
          "id": "chatcmpl-Bi6A02uEHz5w2CMuGcEqoCnHcKAXN",
          "service_tier": "default",
          "finish_reason": "stop",
          "logprobs": null
        },
        "type": "ai",
        "name": null,
        "id": "run--b2ac3a70-8e78-451e-889e-9322996d736d-0",
        "example": false,
        "tool_calls": [],
        "invalid_tool_calls": [],
        "usage_metadata": {
          "input_tokens": 94,
          "output_tokens": 33,
          "total_tokens": 127,
          "input_token_details": {
            "audio": 0,
            "cache_read": 0
          },
          "output_token_details": {
            "audio": 0,
            "reasoning": 0
          }
        }
      }
    }
  }
}
```

Testing execute_Flowchart:
```json
{
  "flowchart": [
    {
      "name": "Task 1",
      "instructions": "convert the input to a single number in base 10.",
      "inputFormat": "a number in english wording such as 'forty two'",
      "outputFormat": "just a single decimal number"
    },
    {
      "name": "Task 2",
      "instructions": "convert the base 10 number to an english worded representation such as 'ten thousand' or 'fifty five'.",
      "inputFormat": "a number is base 10",
      "outputFormat": "number in english wording"
    }
  ],
  "input": "two hundred and fifty six",
  "result": [
    {
      "value": "two hundred and fifty six",
      "executionDetails": {
        "initial_input": "two hundred and fifty six"
      }
    },
    {
      "value": "To convert the input \"two hundred and fifty six\" to a single number in base 10, you would write it as 256.",
      "executionDetails": {
        "promptMessages": [
          {
            "content": "You are a helpful assistant.",
            "additional_kwargs": {},
            "response_metadata": {},
            "type": "system",
            "name": null,
            "id": null
          },
          {
            "content": "Produce the output for the following flowchart node using the provided inputs:\nNode Name: Task 1\nInstructions: convert the input to a single number in base 10.\nInput Format: a number in english wording such as 'forty two'\nOutput Format: just a single decimal number\nInput: two hundred and fifty six",
            "additional_kwargs": {},
            "response_metadata": {},
            "type": "human",
            "name": null,
            "id": null,
            "example": false
          }
        ],
        "response": {
          "content": "To convert the input \"two hundred and fifty six\" to a single number in base 10, you would write it as 256.",
          "additional_kwargs": {
            "refusal": null
          },
          "response_metadata": {
            "token_usage": {
              "completion_tokens": 28,
              "prompt_tokens": 84,
              "total_tokens": 112,
              "completion_tokens_details": {
                "accepted_prediction_tokens": 0,
                "audio_tokens": 0,
                "reasoning_tokens": 0,
                "rejected_prediction_tokens": 0
              },
              "prompt_tokens_details": {
                "audio_tokens": 0,
                "cached_tokens": 0
              }
            },
            "model_name": "gpt-3.5-turbo-0125",
            "system_fingerprint": null,
            "id": "chatcmpl-Bi6A1P3acM4fbFeix53reizrp4pRU",
            "service_tier": "default",
            "finish_reason": "stop",
            "logprobs": null
          },
          "type": "ai",
          "name": null,
          "id": "run--9b9ca350-13e7-4644-8809-ae94409f3650-0",
          "example": false,
          "tool_calls": [],
          "invalid_tool_calls": [],
          "usage_metadata": {
            "input_tokens": 84,
            "output_tokens": 28,
            "total_tokens": 112,
            "input_token_details": {
              "audio": 0,
              "cache_read": 0
            },
            "output_token_details": {
              "audio": 0,
              "reasoning": 0
            }
          }
        }
      }
    },
    {
      "value": "The output for Task 2 based on the provided input \"two hundred and fifty six\" would be: 256 in English wording is \"two hundred fifty-six\".",
      "executionDetails": {
        "promptMessages": [
          {
            "content": "You are a helpful assistant.",
            "additional_kwargs": {},
            "response_metadata": {},
            "type": "system",
            "name": null,
            "id": null
          },
          {
            "content": "Produce the output for the following flowchart node using the provided inputs:\nNode Name: Task 2\nInstructions: convert the base 10 number to an english worded representation such as 'ten thousand' or 'fifty five'.\nInput Format: a number is base 10\nOutput Format: number in english wording\nInput: To convert the input \"two hundred and fifty six\" to a single number in base 10, you would write it as 256.",
            "additional_kwargs": {},
            "response_metadata": {},
            "type": "human",
            "name": null,
            "id": null,
            "example": false
          }
        ],
        "response": {
          "content": "The output for Task 2 based on the provided input \"two hundred and fifty six\" would be: 256 in English wording is \"two hundred fifty-six\".",
          "additional_kwargs": {
            "refusal": null
          },
          "response_metadata": {
            "token_usage": {
              "completion_tokens": 33,
              "prompt_tokens": 113,
              "total_tokens": 146,
              "completion_tokens_details": {
                "accepted_prediction_tokens": 0,
                "audio_tokens": 0,
                "reasoning_tokens": 0,
                "rejected_prediction_tokens": 0
              },
              "prompt_tokens_details": {
                "audio_tokens": 0,
                "cached_tokens": 0
              }
            },
            "model_name": "gpt-3.5-turbo-0125",
            "system_fingerprint": null,
            "id": "chatcmpl-Bi6A3Mjl9F5hbZv27Fejkkw8ZDKSD",
            "service_tier": "default",
            "finish_reason": "stop",
            "logprobs": null
          },
          "type": "ai",
          "name": null,
          "id": "run--a0421ca9-be19-46cf-ae09-6d552064085d-0",
          "example": false,
          "tool_calls": [],
          "invalid_tool_calls": [],
          "usage_metadata": {
            "input_tokens": 113,
            "output_tokens": 33,
            "total_tokens": 146,
            "input_token_details": {
              "audio": 0,
              "cache_read": 0
            },
            "output_token_details": {
              "audio": 0,
              "reasoning": 0
            }
          }
        }
      }
    }
  ]
}
```