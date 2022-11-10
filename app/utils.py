
def calculate_price(order_list:[str], promo_saga: str) -> float:
    
    order_list = [item.lower() for item in order_list]
    promo_saga = promo_saga.lower()
    discount =  0

    other_items = [item for item in order_list if promo_saga not in item]
    promo_saga_items = [item for item in order_list if promo_saga in item]
    
    # Add 20 to total for every item not BTF = Total Not BTF
    total_other_price = 20 * len(other_items)
    # Compute 15 x number of BTF DVDs = Total BTF
    total_saga_price = 15 * len(promo_saga_items)

    distinct_saga_items = [item.split()[-1] for item in promo_saga_items]
    distinct_saga_items = list(set(distinct_saga_items))
    print(distinct_saga_items)

    if len(distinct_saga_items) == 3:
        # if 3 different apply 20% discount to Total BTF
        discount = 0.2
    elif len(distinct_saga_items) == 2:
        # if 2 different apply 10% discount to Total BTF
        discount = 0.1

    final_price = total_other_price + (total_saga_price * (1 - discount))
    # print(final_price)
    return round(final_price, 2)