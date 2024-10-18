import React from 'react';
import ReactDOM from 'react-dom/client';
import axios from 'axios';

import App from './App';



const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);



//========================= 초기화 설정 =========================

// axios 기본값지정 (싱글톤패턴)
axios.defaults.baseURL = process.env.REACT_APP_BASE_URL;
axios.defaults.timeout = 5000;
axios.defaults.headers.common['Content-Type'] = 'application/json';
