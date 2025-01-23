import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai_api_key = os.environ["OPENAI_API_KEY"]

from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

llm = OpenAI()

prompt_template = PromptTemplate.from_template(
    """
    Generate a meal plan for one day include breakfast, lunch, and dinner.
    Follow these dietary restrictions: {dietary_restrictions}. 
    The preferred cuisine is {preferred_cuisine}.
    Return full recipes for each meal, including ingredients and instructions.
    Finally, generate a shopping list that includes all ingredients and quantities used in the recipes.
    """
)


def generate_meal_plan(dietary_restrictions, preferred_cuisine):
    llm_prompt = prompt_template.format(
        dietary_restrictions=dietary_restrictions, preferred_cuisine=preferred_cuisine
    )
    response = llm.invoke(llm_prompt)
    return response


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
