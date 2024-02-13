// import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import './components/component.css';
import CompanyDashBoard from './components/js/CompanyDashBoard';
import QrBatch from './components/js/QrBatch';
import QrCode from './components/js/QrCode';
import UserWallet from './components/js/UserWallet';
import Dashboard from './components/js/dashboard';
import Login from './components/js/login';
import Profile from './components/js/profile';
import Register from './components/js/register';
import User from './components/js/user';
import AuthProvider from './context/AuthContext';
import './index.css';
import reportWebVitals from './reportWebVitals';
import PrivateRoute from './utils/PrivateRoute';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
      <Routes>
        <Route>
          <Route element={<AuthProvider  />}>
            <Route  element={<PrivateRoute  />}>
              <Route path="/" element={<Dashboard />}>
                    <Route path="profile" element={<Profile/>}/>
                    <Route path="company_dashboard" element={<CompanyDashBoard/>}/>
                    <Route path="user" element={<User/>}/>
                    <Route path="qr_batch" element={<QrBatch/>}/>
                    <Route path="qr_code" element={<QrCode/>}/>
                    <Route path="user_wallet/:user_id" element={<UserWallet/>}/>
              </Route>
            </Route>
            <Route path="/login" element={<Login />} />
          </Route>
          <Route path="/register" element={<Register />} />
        </Route>
      </Routes>
  </BrowserRouter>
);

reportWebVitals();
