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
