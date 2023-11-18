import React, { useState } from 'react';
import './login.css';

function Login() {
  const [credentials, setCredentials] = useState({ username: '', password: '' });
  const { username, password } = credentials;

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCredentials({ ...credentials, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!username || !password) {
      alert('Please enter both username and password.');
      return;
    }

    if (username === 'example' && password === 'password') {
      alert('Login successful!');
    } else {
      alert('Invalid username or password. Please try again.');
    }
  };

  return (
    <>
      <form onSubmit={handleSubmit} className="Login">
        <label className="form-label">
          Username:
          <input
            type="text"
            name="username"
            value={username}
            onChange={handleChange}
            className="input-box"
          />
        </label>
        <br />
        <label className="form-label">
          Password:
          <input
            type="password"
            name="password"
            value={password}
            onChange={handleChange}
            className="input-box"
          />
        </label>
        <br />
        <button type="submit" className="submit-button">
          Submit
        </button>
      </form>
    </>
  );
}

export default Login;
