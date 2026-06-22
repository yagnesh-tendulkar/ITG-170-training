import styled from "styled-components";

const Button = styled.button`
  width: 200px;
  color: white;
  background-color: #000033;
  padding: 10px;
  border-radius: 5px;
  font-weight: 900;
  cursor: pointer;

  &:hover {
    background-color: #000066;
  }
`;

function Home({ setCurrentView, fetchUsers }) {
  return (
    <div className="hero">
      <h1>Welcome to User Management System</h1>

        <div className="button-group">
        <button className="btn-primary" onClick={() => setCurrentView("addUser")}>
            Add User
        </button>

        <button className="btn-secondary" onClick={() => {
            fetchUsers();
            setCurrentView("showUsers");
        }}>
            Show All Users
        </button>
        </div>
    </ div >
  );
}

export default Home;