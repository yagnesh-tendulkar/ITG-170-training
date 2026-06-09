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
