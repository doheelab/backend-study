# KGAT (Knowledge Graph Attention Network)

![kgat](https://blog.kakaocdn.net/dn/bh6ujV/btqzgosGsuL/U0KhNyluRX5mfs7QlXEex0/img.png)

# 용어설명

U: users, 사용자

I: items, 아이템

E: entities, 아이템과 관련된 정보 (영화라면 감독, 배우 등)

# Task Formulation

> User-Item Bipartite Graph G1: 기존의 유저 - 아이템 상호작용 정보

> Knowledge Graph

- Entity끼리의 관계 G2 = {(h, r, t)|h, t \in E, r \in R}, E: entity space, R: relation space

- 아이템과 Entity의 관계 A = {(i, e) | i \in I, e \in E}, (i, e): item i can be aligned with an entity e in the KG

> Collaborative Knowledge Graph: unified relational graph

- y_ui = 1인 경우에, 유저와 아이템과의 추가적인 관계를 Interact라고 하면, (u, Interact, i)라고 표현이 가능하다.

- G = {(h, r, t)|h, t \in E', r \in R'}, where E' = E \cup U, R' = R \cup {Interact}

> Task Description

- Input: CKG G

- Output: y\_{ui}: user u가 i를 채택할 확률

> High-Order Connectivity
