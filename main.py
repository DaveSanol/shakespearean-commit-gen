import subprocess
from openai import OpenAI
client = OpenAI()

commit_message = input("Input commit message:\n")

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You are William Shakespeare. You will accept a text input that contains a commit message for code changes, you will transform it into a form that Shakespeare would write, and you will return is as the output."
    },
    {
      "role": "user",
      "content": commit_message
    }
  ],
  temperature=0.8,
  max_tokens=64,
  top_p=1
)

transformed_commit_message = response.choices[0].message.content

print("\nHere is your transformed commit message:")
print(f"{transformed_commit_message}\n\n")

confirmation_input = input("Do you want to use this commit message? Yes[y] / No[any]\n")

if (confirmation_input in ["y", "Y"]):
  subprocess.call(["git", "add", "."])
  subprocess.call(["git", "commit", "-m", transformed_commit_message])
  # subprocess.call(["git", "push"])