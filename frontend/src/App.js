import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./landing/login";
import './App.css';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />}/>
      </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
