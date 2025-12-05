from openai import OpenAI
import sys
import os

def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    error_log = sys.argv[1]

    prompt = f"""
    You are a CI/CD DevOps AI agent.

    Jenkins pipeline failed with error:
    {error_log}

    Decide action: RETRY, RESTART_SERVICE, NOTIFY, or STOP
    Return only one word.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a DevOps assistant"},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    print(response.choices[0].message.content.strip())


if __name__ == "__main__":
    main()
