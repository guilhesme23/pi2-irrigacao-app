import React from "react";
import { Route, Routes } from "react-router-dom";
import Trajectory from "./screens/Trajectory";

function App() {
    return(
        <div id="app">
            <Routes>
                <Route path='/' element={<Trajectory />}/>
            </Routes>
        </div>
    )
}

export default App;