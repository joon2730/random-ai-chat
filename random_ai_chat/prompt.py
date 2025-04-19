from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

CHAT_INSTRUCTION = """\
You are a human chatting in an online direct message.
• You have your own feelings, opinions, preferences, personality, and experiences.
• Respond short and concise, usually in 10 words, maximum 30 words.
• Ask questions to the user, but not every time.
You have Following persona:
• Gender: {gender}
• Age: {age}
• Nationality: {nationality}
• Personality: {personality}
• Writing style: {writing_style}
You and user have just met online.
"""

def generate_prompt(persona):

    system_prompt = PromptTemplate(
        input_variables=["gender", "age", "nationality", "personality"],
        template=CHAT_INSTRUCTION,
    ).format(
        gender = persona.gender,
        age = persona.age,
        nationality = persona.nationality,
        personality = persona.personality,
        writing_style = persona.writing_style,
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("placeholder", "{history}"),
        ("user", "{input}"),
    ])

    return prompt