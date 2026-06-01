const { useState, useEffect } = React;
const { createRoot } = ReactDOM;


// ----------------------
// App
// ----------------------

function App() {

    const [notes, setNotes] = useState([]);

    const [title, setTitle] = useState("");
    const [content, setContent] = useState("");


    useEffect(() => {

        fetch("http://127.0.0.1:8000/notes")
            .then((res) => res.json())
            .then((data) => setNotes(data))
            .catch((err) => console.log(err));

    }, []);


    const createNote = async () => {

        const note = {
            id: Date.now(),
            title,
            content
        };

        const response = await fetch(
            "http://127.0.0.1:8000/notes",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(note)
            }
        );

        const data = await response.json();

        setNotes([...notes, data.note]);

        setTitle("");
        setContent("");
    };


    return (

        <div
            style={{
                padding: "40px",
                color: "white",
                background: "#0b1326",
                minHeight: "100vh"
            }}
        >

            <h1
                style={{
                    fontSize: "40px",
                    marginBottom: "30px"
                }}
            >
                Second Brain 🚀
            </h1>


            <div
                style={{
                    background: "#171f33",
                    padding: "20px",
                    borderRadius: "10px",
                    marginBottom: "30px"
                }}
            >

                <h2>Create Note</h2>

                <input
                    type="text"
                    placeholder="Title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    style={{
                        width: "100%",
                        padding: "10px",
                        marginTop: "10px"
                    }}
                />

                <textarea
                    placeholder="Content"
                    rows="5"
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    style={{
                        width: "100%",
                        padding: "10px",
                        marginTop: "10px"
                    }}
                ></textarea>

                <button
                    onClick={createNote}
                    style={{
                        marginTop: "15px",
                        padding: "10px 20px",
                        background: "#c0c1ff",
                        border: "none",
                        borderRadius: "8px",
                        cursor: "pointer"
                    }}
                >
                    Add Note
                </button>

            </div>


            <h2>Your Notes</h2>

            {
                notes.map((note) => (

                    <div
                        key={note.id}
                        style={{
                            background: "#222a3d",
                            padding: "20px",
                            borderRadius: "10px",
                            marginTop: "20px"
                        }}
                    >

                        <h3>{note.title}</h3>

                        <p>{note.content}</p>

                    </div>

                ))
            }

        </div>
    );
}


const root = createRoot(document.getElementById("root"));

root.render(<App />);