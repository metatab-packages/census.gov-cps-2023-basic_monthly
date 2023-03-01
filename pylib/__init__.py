""" Example pylib functions"""

def openai_one_completion(prompt):
    """Call the OpenAI completions interface to re-write the extra path for a census variable
    into an English statement that can be used to describe the variable."""

    import os
    import openai

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0.2,
    )

    return response["choices"][0]["text"].strip()
