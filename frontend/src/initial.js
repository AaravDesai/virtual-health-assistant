import {useNavigate } from "react-router-dom";

import './App.css';

function Inital() {
  const navigate = useNavigate()
  document.cookie = `auth=6559401561fb12c17f6a5a2e`
  navigate("/home")
  return (
    <div className="">
        initial
        <button onClick={()=>{navigate("/home")}}>START</button>
    </div>
  );
}

export default Inital;
