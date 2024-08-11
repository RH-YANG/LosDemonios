import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Home from './pages/home/Home';
import Gate from './pages/gate/Gate';



const Router = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/gate" element={<Gate />} />
            </Routes>
        </BrowserRouter>
    );
};
export default Router;
