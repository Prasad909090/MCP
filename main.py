import os
import openai


openai.api_key = os.getenv("GROQ_API_KEY")  # Or use OpenAI key

def parse_prompt_with_groq(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or groq-compatible model like "mixtral-8x7b-32768"
        messages=[
            {"role": "system", "content": "You convert natural instructions into actionable commands or file paths."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=100
    )
    return response['choices'][0]['message']['content'].strip()





def main():
    print("Hello from first-mcp!")


if __name__ == "__main__":
    main()
