function UserList({ users, deleteUser, editUser, setCurrentView }) {
    return (
      <>
      <div className="top">

        <button onClick={() => setCurrentView("home")} className="btn-primary">Back</button>
        <h2>All Users</h2>
  
        </div>

        <table className="table">
            <thead>
                <tr>
                <th style={{ border: "1px solid black", padding: "10px" }}>ID</th>
                <th style={{ border: "1px solid black", padding: "10px" }}>Name</th>
                <th style={{ border: "1px solid black", padding: "10px" }}>Username</th>
                <th style={{ border: "1px solid black", padding: "10px" }}>Email</th>
                <th style={{ border: "1px solid black", padding: "10px" }}>Phone</th>
                <th style={{ border: "1px solid black", padding: "10px" }}>Website</th>
                <th style={{ border: "1px solid black", padding: "10px" }}>Actions</th>
                </tr>
            </thead>

            <tbody>
                {!users || users.length === 0 ? (
                <tr>
                    <td colSpan={7} style={{ textAlign: "center", padding: "10px" }}>
                    No Users Available
                    </td>
                </tr>
                ) : (
                users.map((user) => (
                    <tr key={user.id}>
                    <td style={{ border: "1px solid black", padding: "10px" }}>
                        {user.id}
                    </td>
                    <td style={{ border: "1px solid black", padding: "10px" }}>
                        {user.name}
                    </td>
                    <td style={{ border: "1px solid black", padding: "10px" }}>
                        {user.username}
                    </td>
                    <td style={{ border: "1px solid black", padding: "10px" }}>
                        {user.email}
                    </td>
                    <td style={{ border: "1px solid black", padding: "10px" }}>
                        {user.phone}
                    </td>
                    <td style={{ border: "1px solid black", padding: "10px" }}>
                        {user.website}
                    </td>
                    <td style={{ border: "1px solid black", padding: "10px" }}>
                    <div className="action-buttons">
                    <button className="btn-primary" onClick={() => editUser(user)}>
                        Edit
                    </button>

                    <button className="btn-danger" onClick={() => deleteUser(user.id)}>
                        Delete
                    </button>
                    </div>
                    </td>
                    </tr>
                ))
                )}
            </tbody>
</table>
      </>
    );
  }
  
  export default UserList;