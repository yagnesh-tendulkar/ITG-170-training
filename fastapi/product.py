from fastapi import APIRouter
router=APIRouter()
products=[]
@router.get("/")
def get_products():
    return products
@router.post("/")
def add_products(name :str,price:int):
    products.append({"name":name,"price":price})
    return {"Message" : "Product added"}
@router.put("/{index}")
def update_product(index:int , name:str,price:int):
    if index>0 or index>=len(products):
        return {"Invalid index"}
    products[index]={"name":name,"price":price}
    return {"Product updated"}