from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

def generate_article(topic):
    message_content = f"""
        Write a detailed news article about {topic}. 
        Assume you are a New York Times reporter who just heard of the news. 
        Format the output as follows: 
        - Title: write the title 
        - Content: write the content
        Make your output easy to parse into my database.
        Make the articles be at least 500 words.
        """

    completion = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": message_content.strip()},
            {"role": "user", "content": topic}
        ]
    )
    return completion.choices[0].message.content

def save_article(topic, article_content):
    filename = topic.replace(' ', '_').lower() + '.txt'
    with open("result.txt", 'a') as file:
        file.write(article_content)
        file.write("\n************************\n")

def main():
    topics = [
        "September 11th attacks",
        "Obama's election as President",
        "Ruth Bader Ginsburg's death"
    ]

    for topic in topics:
        article_content = generate_article(topic)
        save_article(topic, article_content)
        print(f"Article on '{topic}' saved to file.")

if __name__ == '__main__':
    main()

