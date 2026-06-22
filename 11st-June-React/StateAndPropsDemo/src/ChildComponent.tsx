import { useState } from "react";

function ChildComponent({ name: initialName }) {
    const [name, setName] = useState(initialName || "");

    function handleChange(event) {
        const newName = event.target.value;
        setName(newName);
        console.log(`${newName} is changed`);
    }

    return (
        <>
            <input
                type="text"
                placeholder="eg: John"
                onChange={handleChange}
                value={name}
            />
        </>
    );
}

export default ChildComponent;