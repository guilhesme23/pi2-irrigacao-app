import React from "react";
import { Route, Routes } from "react-router-dom";
import Data from "./screens/Data";
import Trajectory from "./screens/Trajectory";

function App() {
    return(
        <div id="app">
            <Routes>
                <Route path='/' element={<Trajectory />}/>
                <Route path='/data' element={<Data />} />
            </Routes>
        </div>
    )
}

export default App;