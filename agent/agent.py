import os
import sys
import openai

def main():
    if len(sys.argv) < 2:
        print("NO_LOGS")
        return

    logs = sys.argv[1]
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if not openai.api_key:
        print("NO_API_KEY")
        return

    prompt = f"""
You are a DevOps AI agent.

Based on this Jenkins error log, choose ONE action only from:
RETRY / RESTART_SERVICE / NOTIFY / STOP

Error log:
{logs}

Give only 1 word.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "DevOps Expert"},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    decision = response["choices"][0]["message"]["content"].strip().upper()
    print(decision)


if __name__ == "__main__":
    main()
