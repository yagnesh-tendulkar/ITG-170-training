import React from "react";

function Student(props) {
  return (
    <div>
      <h3>Student Details</h3>
      <p>Name: {props.name}</p>
      <p>Course: {props.course}</p>
    </div>
  );
}

export default Student;
