import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./landing/login";
import Signup from "./landing/signup";
import Home from "./pages/home";
import Profile from "./pages/profile";
import Inital from "./initial";

import './App.css';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Inital />} />
          <Route path="/login" element={<Login />}/>
          <Route path="/signup" element={<Signup />}/>
          <Route path="/home" element={<Home />}/>
          <Route path="/profile" element={<Profile />}/>
        </Routes>
     </BrowserRouter>
    </div>
  );
}

export default App;
