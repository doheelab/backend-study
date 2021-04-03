## USE

```
USE DB명 (DB 선택)
```

## LIKE

```sql
SELECT *
FROM custormers
WHERE last_name like 'b%'
```

```sql
`%b%`
'a__b' : 빈칸은 아무 문자 허용
```

## REGEXP

정규표현식

```sql
SELECT *
FROM custormers
WHERE last_name REGEXP 'field'
```

```sql
`field`: 포함 확인
'^field': 시작점
'field$': 끝점
'field|mac|rose': logical or
`[gim]e`: `ge` or `ie` or `me`
`[a-h]`e : a부터 e까지
```

## IS NULL

빈 값 확인

```sql
SELECT *
FROM customers
WHERE phone is NOT NULL
```

## ORDER_BY

정렬하기

```sql
SELECT *
FROM customers
ORDER BY state DESC, first_name
```

## LIMIT 6,3

6부터 시작하여 3개만 보여주기

## INNER JOIN

```sql
SELECT *
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
```

```sql
SELECT order_id, oi.product_id
FROM order_items oi
JOIN products p
ON oi.customer_id = p.customer_id
```

--

## Row 삽입

- single row

```sql
INSERT INTO customers (
  first_name,
  last_name,
  birth_date,
  address,
  city,
  state
)
VALUES(
  'JOHN',
  'SMITH',
  '1990-01-01',
  'address',
  'city',
  'CA',
)
```

- multiple rows

```sql
INSERT INTO shippers
VALUES ('shipper1'), ('shipper2'), ('shipper3')
```

- creating a copy of a table

```sql
INSERT INTO orders_archived
SELECT *
FROM orders
WHERE order_date < '2019-01-01'
```

---

## Update a Single Row

```sql
UPDATE invoices
SET
  payment_total = DEFAULT,
  payment_date = '2019-03-01'
WHERE invoice_id = 1
```

## Delete rows

```sql
DELETE FROM invoices
WHERE client_id = (
  SELECT *
  FROM clients
  WHERE name = 'Myworks'
)
```

---

## 제약조건

`PK` - Primary key, 중복이나 빈값(NULL)이 들어올 수 없음

`NN` - Not Null(빈값) 못들어옴

`UQ` - Unique, 중복 값을 넣을 수 없음

`B` - 데이터를 이진 문자열로 저장함(010101 같은)

`UN` - Unsigned data type (- 범위 삭제)
INT, DOUBLE 등의 경우, UN을 사용해 주면 -값 +값 이던 범위가 값은 없어지고 +값만 2배로 늘어남

`ZF` - Zero Filled 컬럼 크기보다 작은 값을 넣었을 경우 0으로 채운 뒤 삽입시킴

`AI` - Insert 시마다 값 1씩 늘어남

`G` - 다른 열을 기반으로 한 수식으로 생성된 값

`Default/Expression` - 기본값, 기본값에 수식 설정

---

## 테이블 , 데이터 삭제

테이블 삭제는 DROP 테이블명

데이터 삭제는 TRUNCATE 테이블명

---

## 기본키(PRIMARY KEY)

- 테이블 생성시

```sql
CREATE TABLE table_name (
    column1 int(11) PRIMARY KEY
)
```

```sql
CREATE TABLE table_name (
    column1 int(11),
    column2 int(11),
    PRIMARY KEY (column1, column2)
)
```

- 추가

```sql
ALTER TABLE table_name ADD PRIMARY KEY (column1, column2);
```

- 삭제

```sql
ALTER TABLE table_name DROP PRIMARY KEY
```

## 유니크키(UNIQUE KEY)

- 테이블 생성시

```sql
CREATE TABLE table_name (
    column1 int(11),
    column2 int(11),
    UNIQUE KEY `unique_index` (column1, column2)
)
```

- 추가

```sql
ALTER TABLE table_name
ADD UNIQUE `unique_index` (column1, column2);
```

- 삭제

```sql
ALTER TABLE table_name
DROP INDEX `unique_index`
```

## 참고자료

[1] https://wakestand.tistory.com/451
