import { useEffect, useState, useRef } from "react";
import { basic_call } from "../api_call";

import submitButton from "../submit.png"

function General() {
    const [userData, setuserData] = useState({})
    const [cookie, setCookie] = useState()
    const [awaiting, setAwaiting] = useState(false)
    const [conversation, setConversation] = useState([{ message: `Hey, how can I help you?`, sender: "ai", loading: true }])
    const [sessionId, setSessionId] = useState("")

    const inputRef = useRef()

    const processData = (data) => {
        const workout = data.workout_plan.split("\n")
        const result = []
        for (const el of workout) {
            if (el === "" || el.includes("**"))
                continue
            else if (el.includes("*Day ") || el.includes("*Rest") || el.includes(" Day "))
                result.push({
                    header: el,
                    list: []
                })
            else result[result.length - 1].list.push(el)
        }
        data.workout_plan = result
        const diet = data.diet_plan.split("\n")
        const result2 = []
        for (const el of diet) {
            if (el === "" || el.includes("**"))
                continue
            else if (el.includes("*Note") || el.includes("luck"))
                break
            else if (el.includes("*Day ") || el.includes("supplements") || el.includes("Rest"))
                result2.push({
                    header: el,
                    list: []
                })
            else result2[result2.length - 1].list.push(el)
        }
        data.diet_plan = result2
    }

    useEffect(() => {
        const fetchUserData = async (cookieValue) => {
            const config = {
                method: 'get',
                url: 'http://localhost:5000/fetchdata',
                params: {
                    cookie: cookieValue,
                    isHome: true
                },
                headers: {
                    'Content-Type': 'application/json',
                }
            }
            const data = (await basic_call(config)).data
            processData(data)
            setuserData(data)
            setTimeout(() => {
                setConversation([{ message: `Hey ${data.username}! How can I help you today?`, sender: "ai", loading: false }])
            }, 1500)
        }
        const cookies = document.cookie.split('; ')
        const myCookie = cookies.find(cookie => cookie.startsWith('auth='))
        const cookieValue = myCookie && myCookie.split('=')[1]
        setCookie(cookieValue)
        fetchUserData(cookieValue)
    }, [])

    const messageLog = () => {
        return conversation.map(el => {
            const classname = `home-content-left-log-indiv ${el.sender[0] === 'a' ? "ai-message" : "human-message"}`
            if (el.loading) {
                return (
                    <div className={`${classname} loading`} key={el.message}>
                        <div></div>
                        <div></div>
                        <div></div>
                    </div>
                )
            }
            return (
                <div className={classname} key={`${el.message}-${el.sender}`}>
                    {el.message}
                </div>
            )
        })
    }

    const getResponse = async (message) => {
        const config = {
            method: 'get',
            url: 'http://localhost:5000/getAiResponse',
            params: {
                cookie: cookie,
                sessionId: sessionId,
                message: message
            },
            headers: {
                'Content-Type': 'application/json',
            }
        }
        const data = (await basic_call(config)).data
        return data
    }

    const handleSubmit = async () => {
        if (awaiting) return
        if (inputRef.current.value === "") return
        const newMessage = {
            message: inputRef.current.value,
            sender: "human"
        }
        setAwaiting(true)
        inputRef.current.value = ""
        setConversation(prevMessageLog => [...prevMessageLog, newMessage, { message: "loading", loading: true, sender: "ai" }])

        const ai_res = await getResponse(newMessage.message)
        setConversation(prevMessageLog => {
            const newMessageLog = [...prevMessageLog]
            newMessageLog[newMessageLog.length - 1].message = ai_res.message
            newMessageLog[newMessageLog.length - 1].loading = false
            return newMessageLog
        })
        setSessionId(ai_res.sessionId)
        setAwaiting(false)
    }

    const handleScrolling = (ref) => {
        if (ref) {
            ref.scrollTop = ref.scrollHeight - ref.getBoundingClientRect().height
        }
    }

    const workoutDisplay = () => {
        if (userData.workout_plan)
            return userData.workout_plan.map(el => {
                return (
                    <div className="home-content-right-indivlistitem">
                        <strong>{el.header}</strong>
                        {el.list.length > 0 && <div>{el.list.map(line => <p>{line}</p>)}</div>}
                    </div>
                )
            })
    }

    const dietDisplay = () => {
        if (userData.diet_plan)
            return userData.diet_plan.map(el => {
                return (
                    <div className="home-content-right-indivlistitem">
                        <strong>{el.header}</strong>
                        {el.list.length > 0 && <div>{el.list.map(line => <p>{line}</p>)}</div>}
                    </div>
                )
            })
    }

    return (
        <div className="home-content">
            <div className="home-content-left">
                <div className="home-content-left-log" ref={handleScrolling}>
                    {messageLog()}
                </div>
                <div className="home-content-left-inputbar">
                    <input
                        ref={inputRef}
                        placeholder="What should I do if I want to bench more?"
                        onSubmit={handleSubmit}
                        onKeyDown={(e) => e.keyCode === 13 && (e.preventDefault() || handleSubmit())}
                    />
                    <img alt="submit button" src={submitButton} onClick={handleSubmit} />
                </div>
            </div>
            <div className="home-content-right">
                <div>
                    <h1>Workout Plan:</h1>
                    <div>
                        {workoutDisplay()}
                    </div>
                </div>
                <div>
                    <h1>Diet Plan:</h1>
                    <div>
                        {dietDisplay()}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default General;
