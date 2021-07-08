# allegro 추천 시스템

- 6th largest e-commerce in EU (1st in Poland)

- ~15 million transactions monthly

- ~20 million accounts

- ~110 million offers

# Recommender System

- Collaborative-filtering (CF)

  - item-to-item

  - user-to-item

- Content-Based (CB)

  - Description

  - Meta-data

  - Images

## Which is better?

- In general, CF are better

- Not always can be applied

  - Cold-start scenarios

  - Data sparsity

# General framework

## Main components

- Training data preparation (ETL)

- Representation learning module (embedding)

- NN search in latent space

- Serving

# Training data preparation

- Collaborative filtering

  - Sequences of visited product ids from user sessions

  - Purchases or carts

- Content-based recommendations

  - Product title with concatenated category path

  - Product images

# Representation learning

- prod2vec: user sessions' product IDs -> Skipgram (word embedding)

  - word2vec implicitly decomposes the item-to-item interaction matrix

  - resilient to data sparsity

  - 100D embeddings, 2D t-SNE (11:57)

- Textual content

  - Word embeddings trained using fastText (product titles)

  - Products represented as a weight averages of title words

- Product images

  - We use Inception v3, pretrained on ImageNet, fine-tuned on Allegro's products

# Nearest Neightbor search

- Naive approach is expensive

- We need some approximation

- We want high precision but we are willing to compromise on recall

- False negatives are not a problem

## Approximate NN search

- Searching in almost constant time

- Random hyperplane projections (SimHash or LSH)

- Two popular libraries

  - Annoy

  - FAISS: has a two-stage searching strategy

    - Vectors are clustered into relatively small number (e.g. 1000) of partitions

    - Each cluster is represented by a centroid

    - During search, a small number (e.g. 5) of cells closest to the query product is selected

    - Exact search within those cells

- In case of content-based embeddings we use separate indices for each top category of product

- Filtering out too close neighbors

  - Both too close to the source and too close to each other

  - How far is too far (from source)? : experiment

- Eagerly precomputing neighbors for all the products

# Re-ranking

- Leaning-to-rank re-ranking is common in search engines

- A LambdaMART reranking improved allegro's search results by 9% (NDCG)

- We experiment with learning-to-rank algorithms to improve quality of recommendations

# Hybrid recommenders

- For majority of products we are unble to server CF recommendations

  - Item cold-start

  - Data sparsity

- We can recommend products based on content similarity. But is there a better way?

## Our approach

- Find the NN in "content" space narrowed to "popular" items

- Serve CF-based recommendations for the neighbor

## meta-prod2vec

- In classic prod2vec we simply use product ids as words

  - id1 id2 ... idN

- In meta-prod2vec we interleave ids and meta-data

  - id1 meta1 id2 meta2 ... idN metaN

  - We also need to increase window size

- Improves quality of product representations

- We obtain metadata embeddings

  - Both product embeddings and metadata embeddings are in the same vector space

# User-to-item recommendations

- Item-to-item recommendations are crucial for Allegro

  - Offer pages - most visited part of the system

  - The aim is to shorten the Path-to-Purchase

- However, on the main page we need user-to-item recommendations

  - No explicit product context

  - The aim is to inspire users to make new purchases

- Also in e-mail campaigns we need user-to-items recommendations

## Approach

- Learn latent representation of the user

  - Obtained from a user-to-item interaction matrix

  - Impossible to retrain user representation in real-time

  - Good for e-mailing campaigns

- User representation is an aggregation of representation of visited products

  - Requires online NN search

  - Challenge : latency under heavy traffic

- No user representation

  - Interleaved item-to-item recommendations of visited items

  - Easy to implement, fast to serve at runtime

  - Challenge: how to mix recommendations?

# Hyperparameter tuning

- "Hyperparameter Matter" : How to tune word2vec in a recommender system?

- We hold-out some number of train sessions

  - We predict the last item in the session based on the penultimate item.

- Metric = MRR@25

- Do-It-Yourself hyperopt library

# References

https://www.youtube.com/watch?v=muXTMnfPU0k&t=211s
