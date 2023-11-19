import { useState, useRef } from "react";
import { basic_call } from "../api_call";
import { initializeApp } from "firebase/app";
import { getStorage, ref, uploadBytesResumable, getDownloadURL } from "firebase/storage";

import squatsGood from "../squats/squatscorrect1.mov"
import ReactPlayer from "react-player"
import fileUpload from "../fileUpload.png"

function FormAnalysis() {
    const [percent, setPercent] = useState(0);
    const fileRef = useRef()
    const exerciseRef = useRef()

    const handleChange = async (e) => {
        const file = e.target.files[0]
        const fileType = (file.name.split(".")[1]).toLowerCase()
        const config = {
            method: 'get',
            url: 'http://localhost:5000/processVideo',
            params: {
                downloadUrl: "https://firebasestorage.googleapis.com/v0/b/virtual-health-assistant2.appspot.com/o/files%2Fcorrect1%20(1).MOV?alt=media&token=2c7033df-61e5-4aee-809d-af21a2a9bb2e%20formanalysis.js:54%20{data:%20{%E2%80%A6},%20status:%20200,%20statusText:%20%27OK%27,%20headers:%20AxiosHeaders,%20config:%20{%E2%80%A6},%C2%A0%E2%80%A6}",
                fileType: fileType,
                exercise: exerciseRef.current.value
            },
            headers: {
                'Content-Type': 'application/json',
            }
        }
        const firebaseConfig = {
            apiKey: "AIzaSyC9wqIO-wtj5COB5qeATH0KLqt-k-r7sjM",
            authDomain: "virtual-health-assistant2.firebaseapp.com",
            projectId: "virtual-health-assistant2",
            storageBucket: "virtual-health-assistant2.appspot.com",
            messagingSenderId: "70874114381",
            appId: "1:70874114381:web:e482658bdc02cb83c3ef04",
            storageBucket: "virtual-health-assistant2.appspot.com",
        }
        const app = initializeApp(firebaseConfig)
        const storage = getStorage(app)
        const storageRef = ref(storage, `/files/${file.name}`)
        const uploadTask = uploadBytesResumable(storageRef, file)
        uploadTask.on(
            "state_changed",
            (snapshot) => {
                const percent = Math.round(
                    (snapshot.bytesTransferred / snapshot.totalBytes) * 100
                );
                setPercent(percent);
            },
            (err) => console.log(err),
            () => {
                // download url
                getDownloadURL(uploadTask.snapshot.ref).then(async(url) => {
                    console.log(url);
                    config.params.downloadUrl = url
                    const res = await basic_call(config)
                    console.log(res)
                });
            }
        )
    }

    return (
        <div className="home-content2">
            <div className="home-content2-input">
                <iframe src="https://www.youtube.com/embed/hthj8zk0CEE"></iframe>
                <iframe src="https://www.youtube.com/embed/-dkSuVq_kzA"></iframe>                
                <iframe src="https://www.youtube.com/embed/qpol8m2SxXE"></iframe>
                <iframe src="https://www.youtube.com/embed/ymgsawlZNjM"></iframe>
                {/* <input onChange={handleChange} type="file" ref={fileRef} />
                <img onClick={() => fileRef.current.click()} src={fileUpload} />
                <h1>Upload Video For Form Analysis</h1> */}
            </div>
        </div>
    );
}

export default FormAnalysis;
