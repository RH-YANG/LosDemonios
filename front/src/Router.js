import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Home from './pages/home/Home';
import Gate from './pages/gate/Gate';
import Login from './pages/login/Login';



const Router = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/gate" element={<Gate />} />
                <Route path="/login" element={<Login />} />
            </Routes>
        </BrowserRouter>
    );
};
export default Router;
