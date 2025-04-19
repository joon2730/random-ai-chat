import random
from random_ai_chat.options import NATIONALITIES, PERSONALITY_TRAITS, WRITING_STYLES

class Persona:
    gender = random.choice(["male", "female"])
    age = random.randint(18, 38)
    language = random.choice(list(NATIONALITIES.keys()))
    nationality = random.choice(NATIONALITIES[language])
    personality = random.choice(PERSONALITY_TRAITS)
    writing_style = "\n".join([random.choice(WRITING_STYLES[i]) for i in list(WRITING_STYLES.keys())])