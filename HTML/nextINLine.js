function nextItem(ar,item){
    ar.push(item);
    return ar;
}

var ar=[1,3,4,45];
console.log("Before adding:"+JSON.stringify(ar));
console.log(nextItem(ar,10));
console.log(ar.unshift(11));//returns updated length
console.log("After adding:"+JSON.stringify(ar));
