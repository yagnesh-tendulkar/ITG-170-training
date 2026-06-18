//js objects
var myObj={
    gift:"pony",
    pet:"kitten",
    bed:"sleigh"
};
function checkObj(checkProp){
    if (myObj.hasOwnProperty(checkProp)){
        return myObj[checkProp];

    }
    else{
        return "NOt found";
    }
}

console.log(myObj.car);
