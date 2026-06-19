type UserFormProps = {
  username: string;
  email: string;
  setUsername: React.Dispatch<React.SetStateAction<string>>;
  setEmail: React.Dispatch<React.SetStateAction<string>>;
  handleSave: () => void;
  editId: number | null;
};

function UserForm({
  username,
  email,
  setUsername,
  setEmail,
  handleSave,
  editId,
}: UserFormProps) {
  return (
    <div>
      <h2>
        {editId ? "Update User" : "Create User"}
      </h2>

      <input
        type="text"
        placeholder="Enter Username"
        value={username}
        onChange={(e) =>
          setUsername(e.target.value)
        }
      />

      <br />
      <br />

      <input
        type="email"
        placeholder="Enter Email"
        value={email}
        onChange={(e) =>
          setEmail(e.target.value)
        }
      />

      <br />
      <br />

      <button onClick={handleSave}>
        {editId ? "Update" : "Save"}
      </button>
    </div>
  );
}

export default UserForm;