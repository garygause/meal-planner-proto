# Meal Planner Proto

This is an example project I have written using LangChain and OpenAI to create a meal planner prototype.

This example demonstrates a basic chat-based interaction with the OpenAI API using LangChain.

## Stack

langchain, openai, python, poetry

## Usage

1. Clone the repository:

```bash
git clone https://github.com/garygause/meal-planner-proto.git
```

2. Install dependencies:

```bash
cd meal-planner-proto
pyenv local 3.11.4
poetry install
```

3. Add api keys:

```bash
cp .env.example .env
```

Edit .env to include your api keys. At a minimum, OPENAI_API_KEY.

4. Run the code:

```bash
poetry shell
python meal_planner_proto/main.py
```

## Example output

```bash
> python meal_planner_proto/main.py
Welcome to the Meal Planner Prototype!
Please enter your dietary restrictions, separated by commas:
heart healthy
Please enter your preferred cuisine, separated by commas:
vegetarian
Generating meal plan...
Meal plan generated!
Here is your meal plan:

Here’s a heart-healthy vegetarian meal plan for one day, including breakfast, lunch, and dinner, along with recipes and a shopping list.

### Meal Plan

#### Breakfast: Avocado Toast with Tomato and Spinach

**Ingredients:**
- 2 slices whole grain bread
- 1 ripe avocado
- 1 medium tomato, sliced
- 1 cup fresh spinach leaves
- 1 tablespoon lemon juice
- Salt and pepper to taste
- 1 tablespoon olive oil
- Optional: red pepper flakes for seasoning

**Instructions:**
1. Toast the whole grain bread slices until golden brown.
2. In a small bowl, mash the avocado and mix in the lemon juice, salt, and pepper.
3. Spread the mashed avocado on the toasted bread.
4. Top with sliced tomatoes and fresh spinach leaves.
5. Drizzle with olive oil and sprinkle with red pepper flakes if desired.

#### Lunch: Quinoa Salad with Chickpeas and Roasted Vegetables

**Ingredients:**
- 1 cup cooked quinoa
- 1 can (15 oz) chickpeas, rinsed and drained
- 1 red bell pepper, diced
- 1 zucchini, diced
- 1 small red onion, diced
- 2 tablespoons olive oil
- 1 teaspoon garlic powder
- 1 teaspoon cumin
- Salt and pepper to taste
- 1 tablespoon balsamic vinegar
- ¼ cup fresh parsley, chopped

**Instructions:**
1. Preheat the oven to 400°F (200°C).
2. Toss the diced bell pepper, zucchini, and red onion in a bowl with olive oil, garlic powder, cumin, salt, and pepper. Spread onto a baking sheet and roast for 20-25 minutes, until tender.
3. In a large bowl, combine the cooked quinoa, chickpeas, and roasted vegetables.
4. Drizzle with balsamic vinegar and toss to combine. Garnish with fresh parsley.

#### Dinner: Lentil and Sweet Potato Stew

**Ingredients:**
- 1 tablespoon olive oil
- 1 onion, chopped
- 2 cloves garlic, minced
- 2 carrots, diced
- 1 red bell pepper, diced
- 1 medium sweet potato, peeled and diced
- 1 teaspoon ground cumin
- 1 teaspoon smoked paprika
- 1 can (14 oz) diced tomatoes
- 4 cups vegetable broth
- 1 cup green or brown lentils, rinsed
- Salt and pepper to taste
- Fresh parsley for garnish (optional)

**Instructions:**
1. In a large pot, heat olive oil over medium heat. Add onion and garlic; sauté until fragrant.
2. Add carrots, bell pepper, and sweet potato. Cook for about 5 minutes until they begin to soften.
3. Stir in cumin and smoked paprika. Cook for another minute.
4. Add diced tomatoes, vegetable broth, and lentils. Bring to a boil, then reduce heat and simmer for about 30 minutes or until lentils and vegetables are tender.
5. Season with salt and pepper. Serve hot, garnished with fresh parsley if desired.

### Shopping List

#### Produce
- 1 ripe avocado ($1.50)
- 1 medium tomato ($0.50)
- 1 cup fresh spinach ($1.00)
- 1 red bell pepper ($0.75)
- 1 zucchini ($0.75)
- 1 small red onion ($0.50)
- 2 carrots ($0.50)
- 1 medium sweet potato ($0.75)
- 1 onion ($0.50)
- 2 cloves garlic ($0.25)
- Fresh parsley ($1.00)
- 1 lemon (for juice) ($0.50)

#### Canned Goods
- 1 can (15 oz) chickpeas ($1.00)
- 1 can (14 oz) diced tomatoes ($1.00)

#### Grains
- 1 loaf whole grain bread ($3.00)
- 1 cup quinoa ($1.50)

#### Spices/Oils
- Olive oil (16 oz bottle) - $4.00 (you will only use 1-2 tbsp)
- Garlic powder ($2.00, to taste)
- Ground cumin ($2.00)
- Smoked paprika ($2.00)
- Salt and pepper (to taste)

#### Estimated Total Cost: $23.00

Feel free to adjust quantities based on individual dietary needs or preferences. Enjoy your heart-healthy meals!
```

## Credits

Based on lessons learned from the [2025 Bootcamp: Generative AI, LLM Apps, AI Agents, Cursor AI](https://www.udemy.com/course/bootcamp-generative-artificial-intelligence-and-llm-app-development) course by Julio Colomer.
