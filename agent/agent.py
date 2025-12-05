from openai import OpenAI
import sys
import os

def main():

    error_log = sys.argv[1]

    # If API key missing, fallback (POC safety)
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        if "connection refused" in error_log.lower():
            print("RESTART_SERVICE")
        else:
            print("NOTIFY")
        return

    try:
        client = OpenAI(api_key=api_key)

        prompt = f"""
        You are a CI/CD DevOps AI agent.

        Jenkins pipeline failed with error:
        {error_log}

        Decide action: RETRY, RESTART_SERVICE, NOTIFY, or STOP
        Return only ONE WORD.
        """

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        decision = response.output_text.strip()
        print(decision)

    except Exception as e:
        # Fail-safe for quota / internet / API issues
        if "connection refused" in error_log.lower():
            print("RESTART_SERVICE")
        else:
            print("NOTIFY")


if __name__ == "__main__":
    main()
