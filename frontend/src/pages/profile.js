import { useEffect, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { basic_call } from "../api_call";
import Header from "../components/header";
import backButton from "../backButton.png"
import "./profile.css"

function Profile() {
    const [cookie, setCookie] = useState()
    const [loading, setLoading] = useState(false)

    const genderRef = useRef()
    const ageRef = useRef()
    const heightFeetRef = useRef()
    const heightInchesRef = useRef()
    const fitnessGoalRef = useRef()
    const experienceRef = useRef()
    const dietaryRestrictions = useRef()
    const weightRef = useRef()
    const includeSupplementsRef = useRef()
    const numDaysRef = useRef()
    const navigate = useNavigate()

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
            if (data.needsAction) {
                console.log("true")
            }
            else {
                console.log(data)
                ageRef.current.value = parseInt(data.age)
                numDaysRef.current.value = parseInt(data.numDays)
                weightRef.current.value = parseInt(data.weight)
                genderRef.current.value = data.gender
                fitnessGoalRef.current.value = data.fitnessGoal
                dietaryRestrictions.current.value = data.dietaryRestriction
                experienceRef.current.value = data.experience
                includeSupplementsRef.current.checked = data.includeSupplements==="true"
                const heightData = data.height.split(" ")
                heightFeetRef.current.value = parseInt(heightData[0])
                heightInchesRef.current.value = parseInt(heightData[2])
            }
        }
        const cookies = document.cookie.split('; ')
        const myCookie = cookies.find(cookie => cookie.startsWith('auth='))
        const cookieValue = myCookie && myCookie.split('=')[1]
        setCookie(cookieValue)
        fetchUserData(cookieValue)
    }, [])

    const handleSubmit = async (e) => {
        e.preventDefault()
        const newDataObject = {
            "cookie": cookie,
            "age": ageRef.current.value,
            "dietaryRestriction": dietaryRestrictions.current.value,
            "experience": experienceRef.current.value,
            "fitnessGoal": fitnessGoalRef.current.value,
            "gender": genderRef.current.value,
            "height": `${heightFeetRef.current.value} feet ${heightInchesRef.current.value} inches`,
            "needsAction": false,
            "weight": weightRef.current.value,
            "includeSupplements": includeSupplementsRef.current.checked,
            "numDays": numDaysRef.current.value
        }
        const config = {
            method: 'get',
            url: 'http://localhost:5000/updatedata',
            params: newDataObject,
            headers: {
                'Content-Type': 'application/json',
            }
        }
        setLoading("Saving user data")
        await basic_call(config)
        setLoading("Creating new suggestions")
        const config2 = {
            method: 'get',
            url: 'http://localhost:5000/initializeUserRec',
            params: {
                cookie:cookie
            },
            headers: {
                'Content-Type': 'application/json',
            }
        }
        await basic_call(config2)
        setLoading(false)
    }

    return (
        <div className="Profile">
            <Header />
            <img src={backButton} onClick={()=>navigate("/home")}/>
            <form onSubmit={handleSubmit} className="profile-content">
                <div className="profile-content-fields">
                    <div className="profile-content-fields-type1">
                        <label className="form-label">
                            <h1>Gender</h1>
                            <select
                                ref={genderRef}
                                className="input-box"
                            >
                                <option value=""></option>
                                <option value="male">Male</option>
                                <option value="female">Female</option>
                            </select>
                        </label>
                        <label className="form-label">
                            <h1>Weight</h1>
                            <input
                                ref={weightRef}
                                type="number"
                                className="input-box"
                            />
                        </label>
                    </div>
                    <div className="profile-content-fields-type1">
                        <label className="form-label">
                            <h1>Age</h1>
                            <input
                                ref={ageRef}
                                type="number"
                                className="input-box"
                            />
                        </label>
                        <label className="form-label">
                            <h1>Height</h1>
                            <input
                                ref={heightFeetRef}
                                type="number"
                                className="input-box"
                            /> feet
                            <input
                                ref={heightInchesRef}
                                type="number"
                                className="input-box"
                            /> inches
                        </label>
                    </div>
                    <div className="profile-content-fields-type1">
                        <label className="form-label">
                            <h1>Fitness Goals</h1>
                            <select
                                ref={fitnessGoalRef}
                                className="input-box"
                            >
                                <option value=""></option>
                                <option value="muscle gain">Muscle Gain</option>
                                <option value="build strength">Build Strength</option>
                                <option value="improve cardio/endurance">Improve Cardio/Endurance</option>
                                <option value="lose weight">Lose Weight</option>
                            </select>
                        </label>
                        <label className="form-label">
                            <h1>Include Supplements?</h1>
                            <input
                                ref={includeSupplementsRef}
                                type="checkbox"
                                className="input-box"
                            />
                        </label>
                    </div>
                    <div className="profile-content-fields-type1">
                        <label className="form-label">
                            <h1>Experience</h1>
                            <select
                                ref={experienceRef}
                                className="input-box"
                            >
                                <option value=""></option>
                                <option value="beginner">{"Beginner ( < 6 months)"}</option>
                                <option value="intermediate">{"Intermediate (6 months ~ 1.5 years)"}</option>
                                <option value="advanced">{"Advanced ( > 1.5 years)"}</option>
                            </select>
                        </label>
                        <label className="form-label">
                            <h1>Dietary restrictions</h1>
                            <select
                                ref={dietaryRestrictions}
                                className="input-box"
                            >
                                <option value="n/a">None</option>
                                <option value="vegetarian">Vegetarian</option>
                                <option value="vegan">Vegan</option>
                                <option value="pescetarian">Pescetarian</option>
                            </select>
                        </label>
                    </div>
                    <label className="form-label">
                        <h1>How many days do you want to exercise?</h1>
                        <input
                            ref={numDaysRef}
                            type="number"
                            className="input-box"
                        />
                    </label>
                </div>
                <button type="submit" className="submit-button">
                    Submit
                </button>
            </form>
            {loading && (
                <div className="profile-loading">
                    <div className="profile-loading-box">
                        {loading}
                        <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                    </div>                    
                </div>
            )}
        </div>
    );
}

export default Profile;
