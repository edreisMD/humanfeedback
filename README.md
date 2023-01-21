# 🍬 HumanFeedback
👨Helping Humans Teach AIs 🤖 

# What is this?
A new set of applications are centered around AI API calls (like GPT3). Data from the user-AI interaction can be evaluated, (re)labeled and then used to improve the model (through finetuning or RLHF). But just storing the results in a unstructured manner doesn't make the data very useful. There is a need for a simple and standardized pipeline to go through these steps. 

This library aims to help AI apps to easily incorporate Human Feedback and improve their models.

This library is inspired on LangChain work and is aimed to work together with it.

# What can this help with?
- Store all the inputs/outputs of a  by simply calling a python library
- Extract metrics of unlabeled data
- Rank the most relevant examples to be labeled
- Export a table of examples to be annotated
- Finetune GPT3 with the annotated data

