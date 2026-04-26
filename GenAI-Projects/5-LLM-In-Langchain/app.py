from llm_factory import get_llm

def main():
    print("Langchain LLM component Demo 🧠")

    llm = get_llm()

    prompt = "Explain the concept of Langchain in simple terms."
    response = llm.invoke(prompt)
    print(f"Sending prompt to {type(llm).__name__}... \n ")
    print(f"Model Response: \n")
    print(response.content)

if __name__ == "__main__":
    main()