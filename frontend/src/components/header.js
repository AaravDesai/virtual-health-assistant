import { useState } from "react"
import { useNavigate } from "react-router-dom"

import logo from "../logo.png"
import menuIcon from "../Hamburger_icon.svg.png"
import "./header.css"

function Header() {
    const [toggleOpen, setToggleOpen] = useState(false)
    const navigate = useNavigate()
    
    return (
        <div className="header">
            <img src={logo}/>
            <img onClick={()=>setToggleOpen(prevToggle=>!prevToggle)} className={`header-menu ${toggleOpen && "header-menu-open"}`} src={menuIcon}/>
            {toggleOpen && (
                <div className={toggleOpen ? "header-dropdown-open" : "header-dropdown"}>
                    <div onClick={()=>navigate("/profile")}>Profile</div>
                    <div>Logout</div>
                </div>
            )}
        </div>
    );
}

export default Header;
