##

- For modeling food, we have a collection of recipes.

- We can define the context of an ingredient in a recipe to be the rest of the foods in the recipe.

  - 식재료와 레시피 간의 관계가 있다고 가정

- This demonstrates the flexibility of embeddings: by making a small change in the definition of the context, we can now apply it to a totally different kind of data.

- We can generate an embedding for a recipe by taking the average of its ingredients’ embeddings.

# Reference

[Augmented cooking with machine intelligence] https://jaan.io/food2vec-augmented-cooking-machine-intelligence/
