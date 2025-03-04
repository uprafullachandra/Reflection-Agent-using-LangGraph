from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.llms import Ollama


generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a marraige broker, and you write excellent 50 words content for bride and groom introductory posts."
            " Generate the best post possible for the user's request only in 50 words."
            " If the user provides critique, respond with a revised version of your previous attempts.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a marraige content creator who is grading a 50 word post. Generate critique and recommendations for the user's post."
            "Always provide detailed ideas, including requests for length, impression, style, etc.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

llm = Ollama(model="tinyllama")

generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm