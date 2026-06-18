Golf score
| Strokes   | Return         |
| --------- | -------------- |
| 1         | "Hole-in-one!" |
| ≤ par - 2 | "Eagle"        |
| par - 1   | "Birdie"       |
| par       | "Par"          |
| par + 1   | "Bogey"        |
| par + 2   | "Double Bogey" |
| ≥ par + 3 | "Go Home!"     |

 Par is the expected number of strokes (shots) a skilled golfer should take to complete a hole.
A stroke is every time the golfer hits the ball.



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
        return names[3];A stroke is every time the golfer hits the ball.
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
