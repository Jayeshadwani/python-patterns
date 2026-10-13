# Day 4, Problem 7 (overall #34): `merge`: inner, left, and anti-join

**Fact:** `merge` matches rows of two tables on a key. The `how` argument decides what happens to rows that find no match: `inner` drops them, `left` keeps the left ones and fills the right side with `NaN`.
**Gap from Problem 6:** all earlier answers came from one table. Here two tables must be lined up first.
**Gap to Problem 8:** matching is easy when keys are unique. When a key repeats, one row matches several rows, and the result grows.

## Where this shows up
Joining orders to customers, events to users, predictions to labels. The "who has no match" question (customers who never ordered, orders with an unknown customer) is the anti-join, and pandas has no `how="anti"`, so you build it.

## Task
`customers` has columns `customer_id, name`. `orders` has `order_id, customer_id, amount`. Write four functions in `main.py`. Every result is sorted by `customer_id` (then `order_id` where it exists, missing last) and has its index reset to `0..n-1`.

1. `inner_join(customers, orders)`: customers that have orders, one row per order. Columns: `customer_id, name, order_id, amount`.
2. `left_join(customers, orders)`: every customer; customers without orders have `NaN` in `order_id` and `amount`. Same columns.
3. `customers_without_orders(customers, orders)`: the customer rows (columns `customer_id, name`) that have no order at all.
4. `orders_with_unknown_customer(customers, orders)`: the order rows (columns `order_id, customer_id, amount`) whose `customer_id` is not in `customers`.

## Examples
```python
customers = pd.DataFrame({"customer_id": [1, 2], "name": ["Ana", "Ben"]})
orders = pd.DataFrame({"order_id": [101, 102], "customer_id": [1, 9], "amount": [50.0, 20.0]})
customers_without_orders(customers, orders)["name"].tolist()          # ['Ben']
orders_with_unknown_customer(customers, orders)["order_id"].tolist()  # [102]
```

## Rules
- Do not modify the inputs.
- A customer whose order has a missing `amount` **has** an order. Do not decide "no order" by looking for `NaN` in a value column.
- Say in 2-3 sentences how you build an anti-join, before you code.

## Think first
1. After `merge(how="left")`, which column is safe to test for "no match", and which one is not?
2. What does `merge(..., indicator=True)` add, and how could it help here?

## Run
```
cd 34_merge_joins
python main.py
python -m pytest -q
```

## Commit
```
git add python_programs/34_merge_joins
git commit -m "day04-p07: merge_joins"
```
