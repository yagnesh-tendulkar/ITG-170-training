import { useState, useEffect } from "react";

function UserForm({ addUser, updateUser, editingUser, setCurrentView }) {
  const [formData, setFormData] = useState({
    id: "",
    name: "",
    username: "",
    email: "",
    phone: "",
    website: "",
  });

  useEffect(() => {
    if (editingUser) {
      setFormData(editingUser);
    }
  }, [editingUser]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (editingUser) {
      updateUser(formData);
    } else {
      addUser({ ...formData, id: Date.now() });
    }
  };

  return (
    <>
      <div className="card">
      <h3>{editingUser ? "Edit User" : "Add User"}</h3>

      <form onSubmit={handleSubmit}>
  <table className="form-table">
    <tbody>
      {editingUser && (
        <tr>
          <td>
            <label>ID</label>
          </td>
          <td>
            <input value={formData.id} disabled />
          </td>
        </tr>
      )}

      <tr>
        <td>
          <label>Name</label>
        </td>
        <td>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </td>
      </tr>

      <tr>
        <td>
          <label>Username</label>
        </td>
        <td>
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
          />
        </td>
      </tr>

      <tr>
        <td>
          <label>Email</label>
        </td>
        <td>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </td>
      </tr>

      <tr>
        <td>
          <label>Phone</label>
        </td>
        <td>
          <input
            type="text"
            name="phone"
            value={formData.phone}
            onChange={handleChange}
            required
          />
        </td>
      </tr>

      <tr>
        <td>
          <label>Website</label>
        </td>
        <td>
          <input
            type="text"
            name="website"
            value={formData.website}
            onChange={handleChange}
          />
        </td>
      </tr>

      <tr>
        <td></td>
        <td>
          <div className="form-buttons">
            <button className="btn-primary" type="submit">
              {editingUser ? "Update User" : "Add User"}
            </button>

            <button
              className="btn-secondary"
              type="button"
              onClick={() => setCurrentView("showUsers")}
            >
              Cancel
            </button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</form>
      </div>
    </>
  );
}

export default UserForm;