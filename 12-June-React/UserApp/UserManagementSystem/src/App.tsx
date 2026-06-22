import { useEffect, useState } from "react";
import Home from "./components/Home";
import UserForm from "./components/UserForm";
import UserList from "./components/UserList";

function App() {
  const [currentView, setCurrentView] = useState("home");
  const [users, setUsers] = useState([]);
  const [editingUser, setEditingUser] = useState(null);

  // Fetch API users when "Show All Users" is clicked
  // const fetchUsers = async () => {
  //   try {
  //     const res = await fetch("https://jsonplaceholder.typicode.com/users");
  //     const data = await res.json();
  //     setUsers(data);
  //   } catch (error) {
  //     console.error("Error fetching users:", error);
  //   }
  // };

  const fetchUsers = async () => {
    try {
      const res = await fetch(
        "https://jsonplaceholder.typicode.com/users"
      );
      const data = await res.json();
      setUsers(data);
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };
  
  useEffect(() => {
    fetchUsers();
  }, []);
  // Delete user
  const deleteUser = (id) => {
    if (window.confirm("Are you sure you want to delete this user?")) {
      setUsers(users.filter((user) => user.id !== id));
    }
  };

  // Edit user
  const editUser = (user) => {
    setEditingUser(user);
    setCurrentView("addUser"); // Show form
  };

  // Update user
  const updateUser = (updatedUser) => {
    setUsers(
      users.map((u) => (u.id === updatedUser.id ? updatedUser : u))
    );
    setEditingUser(null);
    setCurrentView("showUsers");
  };

  // Add new user
  const addUser = (newUser) => {
    setUsers([...users, newUser]);
    setCurrentView("showUsers");
  };

  return (
    <>
      {currentView === "home" && (
        <Home
          setCurrentView={setCurrentView}
          fetchUsers={fetchUsers}
        />
      )}

      {currentView === "addUser" && (
        <UserForm
          addUser={addUser}
          updateUser={updateUser}
          editingUser={editingUser}
          setCurrentView={setCurrentView}
        />
      )}

      {currentView === "showUsers" && (
        <UserList
          users={users}
          deleteUser={deleteUser}
          editUser={editUser}
          setCurrentView={setCurrentView}
        />
      )}
    </>
  );
}

export default App;