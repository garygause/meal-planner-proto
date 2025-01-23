import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai_api_key = os.environ["OPENAI_API_KEY"]

from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

llm = OpenAI()

prompt_template = PromptTemplate.from_template(
    """
    Generate a meal plan following these dietary restrictions: {dietary_restrictions}. 
    Use these preferred ingredients:  {preferred_ingredients}.  
    The preferred cuisine is {preferred_cuisine}.
    """
)


def generate_meal_plan(dietary_restrictions, preferred_cuisine, preferred_ingredients):
    llm_prompt = prompt_template.format(
        dietary_restrictions=dietary_restrictions,
        preferred_cuisine=preferred_cuisine,
        preferred_ingredients=preferred_ingredients,
    )
    response = llm.invoke(llm_prompt)
    return response


def main():
    print("Welcome to the Meal Planner Prototype!")
    print("Please enter your dietary restrictions, separated by commas:")
    dietary_restrictions = input()
    print("Please enter your preferred cuisine, separated by commas:")
    preferred_cuisine = input()
    print("Please enter your preferred ingredients, separated by commas:")
    preferred_ingredients = input()

    print("Generating meal plan...")
    meal_plan = generate_meal_plan(
        dietary_restrictions, preferred_cuisine, preferred_ingredients
    )
    print("Meal plan generated!")
    print("Here is your meal plan:")
    print(meal_plan)


if __name__ == "__main__":
    main()
