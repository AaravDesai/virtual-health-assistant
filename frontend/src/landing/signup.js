import React, { useState } from 'react';
import { basic_call } from '../api_call';

function Signup() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

    const handleSubmit = async(e) => {
        e.preventDefault();
        if (!username || !password) {
            alert('Please enter both username and password.');
            return;
        }
        const config = {
            method: 'get',
            url: 'http://localhost:5000/signup',
            params: {
                username: username,
                password: password,
                confirmPassword:confirmPassword
            },
            headers: {
                'Content-Type': 'application/json',
            }
        }
        console.log(config)
        const res = await basic_call(config)
        console.log(res)
    }

    return (
        <div>
            <form onSubmit={handleSubmit} className="Login">
                <label className="form-label">
                    Username:
                    <input
                        type="text"
                        name="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
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
                        onChange={(e) => setPassword(e.target.value)}
                        className="input-box"
                    />
                </label>
                <br />
                <label className="form-label">
                    Confirm Password:
                    <input
                        type="password"
                        name="password"
                        value={confirmPassword}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                        className="input-box"
                    />
                </label>
                <br />
                <button type="submit" className="submit-button">
                    Submit
                </button>
            </form>
        </div>
    );
}

export default Signup;
