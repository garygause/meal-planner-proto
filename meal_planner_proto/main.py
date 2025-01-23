import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai_api_key = os.environ["OPENAI_API_KEY"]

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")


chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an Nutritionist expert on meal planning."),
        ("human", "Hello, Nutritionist, can you please help me with meal planning?"),
        ("ai", "Sure!"),
        (
            "human",
            """
            Generate a meal plan for one day include breakfast, lunch, and dinner.
            Follow these dietary restrictions: {dietary_restrictions}. 
            The preferred cuisine is {preferred_cuisine}.
            Return full recipes for each meal, including ingredients and instructions.
            Finally, generate an efficient shopping list that includes all ingredients used in the recipes and estimated cost.
            """,
        ),
    ]
)


def generate_meal_plan(dietary_restrictions, preferred_cuisine):
    messages = chat_template.format_messages(
        dietary_restrictions=dietary_restrictions, preferred_cuisine=preferred_cuisine
    )
    response = llm.invoke(messages)
    return response.content


def main():
    print("Welcome to the Meal Planner Prototype!")
    print("Please enter your dietary restrictions, separated by commas:")
    dietary_restrictions = input()
    print("Please enter your preferred cuisine, separated by commas:")
    preferred_cuisine = input()

    print("Generating meal plan...")
    meal_plan = generate_meal_plan(dietary_restrictions, preferred_cuisine)
    print("Meal plan generated!")
    print("Here is your meal plan:")
    print(meal_plan)


if __name__ == "__main__":
    main()
