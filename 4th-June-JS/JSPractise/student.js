class Student
{
    constructor(id,name,age,marks)
    {
        this.id=id;
        this.name=name;
        this.age=age;
        this.marks=marks;
    }

    study()
    {
        console.log(`Name: ${this.name},
Age: ${this.age},
Id: ${this.id},
Marks: ${marks}`)
    }
}

marks={
    "maths":89,
    "science":85,
    "english":80
}

let student= new Student(101,"Santosh",23,marks)

student.study();