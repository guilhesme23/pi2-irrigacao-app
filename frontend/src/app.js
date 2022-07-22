import React from "react";
import { Route, Routes } from "react-router-dom";
import Data from "./screens/Data";
import Trajectory from "./screens/Trajectory";
import Reports from "./screens/Reports";

function App() {
    return(
        <div id="app">
            <Routes>
                <Route path='/' element={<Trajectory />}/>
                <Route path='/data' element={<Data />} />
                <Route path='/reports' element={<Reports />} />
            </Routes>
        </div>
    )
}

export default App;