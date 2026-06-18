// var outerwear="T-shirt";
// //global
// function myScope(num){
//     //local scope 
//     var outerwear;
//     return outerwear;
// }

// console.log(outerwear);
// console.log(myScope(3));



//adding items into an array using JSON.stringify

// function nextItem(ar,item){
//     ar.push(item);
//     return ar;
// }

// var ar=[1,3,4,45];
// console.log("Before adding:"+JSON.stringify(ar));
// console.log(nextItem(ar,10));
// console.log(ar.unshift(11));//returns updated length
// console.log("After adding:"+JSON.stringify(ar));



// function welcomeToBooleans(){
//     return false;
// }

// console.log(welcomeToBooleans());






// //if conditions
// function trueOrfalse(isItTrue){
//     if (isItTrue){
//         return "Yes,it is true";
//     }
//     else
//     {
//         return "No,it is false";
//     }
// }

// console.log(trueOrfalse(0));
// //var isItTrue=false;
// console.log();

// console.log();
// console.log();

// //== ===
// function test(val1, val2) {
//     if (val1 === val2) {
//         return "Strictly equal (same value and same datatype)";
//     } 
//     else if (val1 == val2) {
//         return "Equal (same value but datatype may differ)";
//     } 
//     else {
//         return "Not equal";
//     }
// }

// console.log(test("12", "12"));


// fucntion testStrict(val1,val2){
//     if()
// }


//if else 
//conditions
// num5-return "tiny"
// num<10-return "smaller"
// num<15-return "Medium"
// num <20 return "Large"
// num>=20-return "Huge"



function conditions(value)
{
    if (value<5){
        return "Tiny";
    }
    else if (value<10){
        return "Small";
    }
    else if (value<15){
        return "Medium";
    }
    else if (value<20){
        return "Large";
    }
    else if(value>=20){
        return "Huge";
    }
    else{
        return "BYEBYE..";
    }
}
console.log(conditions(22));




console.log();



var names=["Hole-in-one!","Eagle","Birdie","Par","Bogey","Double Bogey","Go-Home"];
console.log(names.length)
function golfscore(strokes,par)
{
    if(strokes==1){
        //return "Hole-in-one!";
        return names[0];
    }
    else if (strokes<=par-2){
        //return "Eagle";
        return names[1];
    }
    else if (strokes=par-1){
        //return "Birdie";
        return names[2];
    }
    else if (strokes==par){
        //return "Par";
        return names[3];//A stroke is every time the golfer hits the ball.
    }
    else if (strokes=par+1){
        //return "Bogey";
        return names[4];
    }
    else if (strokes=par+2){
        //return "Double Bogey";
        return names[5];
    }
    else if (strokes>= par+3){
        //return "Go HOme!";
        return names[6];
    }
    else{
        return "GAME CANCELLED";
    }
}

console.log(golfscore(100,4));






function conf(val){
    var u=(val.toUpperCase());
switch(u){
    case 'A':
        return  "alphabet A";
    case 'B':
         return "alphabet B";
    default:
        return "default";

}
}
console.log(conf("A1"));



