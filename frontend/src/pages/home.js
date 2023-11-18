import { useEffect, useState } from "react";
import { basic_call } from "../api_call";

function Home() {
    const [userData,setuserData] = useState({})

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

    return (
        <div className="Home">
            home
        </div>
    );
}

export default Home;
