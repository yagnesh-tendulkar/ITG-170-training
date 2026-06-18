const localForecast={
    today :{min:22,max:34},
    tomorrow:{min:34,max:90}
};
function getMaxOfTomorrow(forercast){
    const {tomorrow:{max:temp}}=localForecast;
    return temp;
}
console.log(getMaxOfTomorrow(localForecast));
