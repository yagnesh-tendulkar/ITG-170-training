type User = {
  id: number;
  username: string;
  email: string;
};

type UserListProps = {
  users: User[];
  handleEdit: (user: User) => void;
  handleDelete: (id: number) => void;
};

function UserList({
  users,
  handleEdit,
  handleDelete,
}: UserListProps) {
  return (
    <div>
      <h2>User List</h2>

      {users.map((user) => (
        <div
          key={user.id}
          style={{
            border: "1px solid black",
            padding: "10px",
            marginTop: "10px",
            borderRadius: "8px",
          }}
        >
          <h3>{user.username}</h3>

          <p>{user.email}</p>

          <button
            onClick={() => handleEdit(user)}
          >
            Edit
          </button>

          <button
            onClick={() =>
              handleDelete(user.id)
            }
            style={{ marginLeft: "10px" }}
          >
            Delete
          </button>
        </div>
      ))}
    </div>
  );
}

export default UserList;