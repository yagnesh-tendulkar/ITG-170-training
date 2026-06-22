import ChildComponent from "./ChildComponent";

function ParentComponent({name})
{
    return( 
    <>
        <h2>Parent Component</h2>
        <ChildComponent name={name} />

    </>);
}

export default ParentComponent;