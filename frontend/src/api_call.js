import axios from "axios"

export const basic_call = async(config)=>{
    const res = await axios(config)
    return res
}