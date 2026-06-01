product={'name':'laptop','price':53000,'quantity':10}
print(product.__getitem__('price')*product.get('quantity'))