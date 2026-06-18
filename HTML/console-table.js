console.table([1,2,3]);

console.error("error message");

console.log("Message");


for (const item of ['a', 'b', 'c']) console.log(item);


[1,2,3].forEach(num=>console.log(num));


let str = "JavaScript";
console.log(str.charAt(3));
console.log(str.includes("Script"));
console.log(str.startsWith("Java"));
console.log(str.endsWith("pt"));
console.log(str.replace("Java","Type"));
console.log(str.split(" "));
console.log(str.toUpperCase());



const arr = [1, 2, 3];
console.table(arr);
console.log("///// push//////adds at end of array,with value mentioned in ()")
console.log(arr.push(4));
console.table(arr);
console.log("----pop---removes last index element")
console.log(arr.pop());
console.table(arr);
console.log("=====shift removes first element and returns")
console.log(arr.shift());
console.table(arr);
console.log("----unshift---adds at first index and returns the length")
console.log(arr.unshift("balaji"));
console.table(arr);
console.log("====includes---checks whether it is present or not and returns true/false");
console.log(arr.includes(2));
console.table(arr);

console.log("find-returns value that satisfies  the cond:"+arr.find(num => num > 1));
console.log("filter-works similar to find,retuens element in array that meets the condition in call back funciton:"+arr.filter(num => num > 1));
console.log("map:Calls a defined callback function on each element of an array, and returns an array that contains the results.\n"+arr.map(num => num * 2));
console.log("reduce-"+arr.reduce((acc, cur) => acc + cur, 0));


console.log("\n \n");
const now = new Date();
console.log(now.getFullYear());
let res=now.getMonth()+1; // 1-12
console.log(res);
console.log(now.toISOString());
