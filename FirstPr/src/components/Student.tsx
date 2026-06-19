type StudentProps = {
    name : string;
    rollno : number;
    course : string;
};
function Student({name,course,rollno}: StudentProps){
    return (
        <div>
            <h1>{name}</h1>
            <h2>{course}</h2>
            <p> {rollno} </p>
        </div>
    );
}
export default Student;


