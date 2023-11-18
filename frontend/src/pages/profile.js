import { useEffect, useState } from "react";
import { basic_call } from "../api_call";

function Profile() {
    const [userData, setuserData] = useState({})

    useEffect(() => {
        const fetchUserData = async (cookieValue) => {
            const config = {
                method: 'get',
                url: 'http://localhost:5000/fetchdata',
                params: {
                    cookie: cookieValue
                },
                headers: {
                    'Content-Type': 'application/json',
                }
            }
            const data = (await basic_call(config)).data
            setuserData(data)
        }
        const cookies = document.cookie.split('; ')
        const myCookie = cookies.find(cookie => cookie.startsWith('auth='))
        const cookieValue = myCookie && myCookie.split('=')[1]

        fetchUserData(cookieValue)
    }, [])

    const handleSubmit = () => {

    }

    return (
        <div className="Profile">
            <form onSubmit={handleSubmit} className="Login">
                <label className="form-label">
                    Gender:
                    <select
                        type="password"
                        name="password"
                        className="input-box"
                    >
                        <option value=""></option>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                    </select>
                </label>
                <br />
                <label className="form-label">
                    Age:
                    <input
                        type="number"
                        className="input-box"
                    />
                </label>
                <label className="form-label">
                    Height:
                    <input
                        type="number"
                        className="input-box"
                    /> feet
                    <input
                        type="number"
                        className="input-box"
                    /> inches
                </label>
                <br />
                <label className="form-label">
                    Fitness Goals:
                    <select
                        type="password"
                        name="password"
                        className="input-box"
                    >
                        <option value=""></option>
                        <option value="Muscle Gain">Muscle Gain</option>
                        <option value="Build Strength">Build Strength</option>
                        <option value="Improve Cardio/Endurance">Improve Cardio/Endurance</option>
                        <option value="Lose Weight">Lose Weight</option>
                    </select>
                </label>
                <br />
                <label className="form-label">
                    Experience:
                    <select
                        type="password"
                        name="password"
                        className="input-box"
                    >
                        <option value=""></option>
                        <option value="beginner">{"Beginner ( < 6 months)"}</option>
                        <option value="intermediate">{"Intermediate (6 months ~ 1.5 years)"}</option>
                        <option value="advanced">{"Advanced ( > 1.5 years)"}</option>
                    </select>
                </label>
                <br />
                <label className="form-label">
                    Dietary restrictions:
                    <select
                        className="input-box"
                    >
                        <option value="n/a">None</option>
                        <option value="Vegetarian">Vegetarian</option>
                        <option value="Vegan">Vegan</option>
                        <option value="Pescetarian">Pescetarian</option>
                    </select>
                </label>
                <br />
                <button type="submit" className="submit-button">
                    Submit
                </button>
            </form>
        </div>
    );
}

export default Profile;
