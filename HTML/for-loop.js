//interate within an arrray using for loop
var ourArr = [1,2,23,3,34,0];

let len = ourArr.length;

for (let i = 0; i < len; i++) {
    ourArr.push(i);
}

console.log(ourArr);
var tiotal=0;
for (let j=0;j<ourArr.length;j++)
{
    tiotal+=ourArr[j];
}
console.log("total:"+tiotal);
