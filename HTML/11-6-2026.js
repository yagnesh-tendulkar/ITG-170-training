


function randomFunction(){
    return Math.floor(Math.random()*20);
}
console.log(randomFunction());


console.log();
function convertToInteger(str){
    return parseInt(str);
}
console.log(convertToInteger("10"));



function checkSign(num){
    return num>0?"positive":num<0?"negative":"zero";
}

console.log(checkSign(-1));


const s=[1,1,22,3];
function editInPlCE(){
    s[0]=2;
    s[1]=4;
}
editInPlCE();
console.log(s);



console.log("\n");
console.log("balaji");

//prevent object mutation

function freezeObj(){
    const MATH_CONSTANTS={
        PI:3.14
    };
    //object.freeze(MATH_CONSTANTS);
    try{
        MATH_CONSTANTS.PI=88;
    }
    catch (ex){
        console.log(ex);
    }
    return MATH_CONSTANTS.PI;
}

const PI=freezeObj();
console.log(PI);








//arrow function
var myCont=(arr1,arr2)=>arr1.concat(arr2);
console.log(myCont([1,2],[2,3]));




//without arrow function
var magic=function(){
    return new Date();
};
console.log(magic());

console.log("\n using arrow function  \n");
var magic =()=>new Date();
console.log(magic());




//rest operator 
const sum=(function(){
    return function sum(...args){
        return args.reduce((a,b)=> a+b,0);
    };
} )();
console.log(sum(1,2,3));




//spread operator
