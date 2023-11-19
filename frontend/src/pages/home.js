import { useState } from "react";

import Header from "../components/header";
import General from "./general";
import FormAnalysis from "./formanalysis";

import "./home.css"
import "./home2.css"

function Home() {
    const [currentTab, setCurrentTab] = useState(1)

    return (
        <div className="Home">
            <Header />
            <div className="home-menubar">
                <div className={`${currentTab && "home-menubar-activated"}`} onClick={()=>setCurrentTab(1)}>
                    A
                </div>
                <div className={`${!currentTab && "home-menubar-activated"}`} onClick={()=>setCurrentTab(0)}>
                    B
                </div>
            </div>
            {currentTab ? <General /> : <FormAnalysis />}
        </div>
    );
}

export default Home;
