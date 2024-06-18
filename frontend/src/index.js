// import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import './components/CustomAntd.css';
import "./components/CustomHtml.css";
import './components/component.css';
import CompanyDashBoard from './components/js/CompanyDashBoard';
import QrBatch from './components/js/QrBatch';
import QrCode from './components/js/QrCode';
import UserWallet from './components/js/UserWallet';
import UsersWalletReport from './components/js/UsersWalletReport';
import Dashboard from './components/js/dashboard';
import Login from './components/js/login';
import Profile from './components/js/profile';
import Register from './components/js/register';
import User from './components/js/user';
import Permissions from './components/js/Permissions'
import AuthProvider from './context/AuthContext';
import './index.css';
import reportWebVitals from './reportWebVitals';
import PrivateRoute from './utils/PrivateRoute';
import SystemParameter from './components/js/SystemParameter';
import Page404 from './404' 

const AuthRoute = ({component}) => {
  // return <Page404 />
  return component
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
      <Routes>
        <Route>
          <Route element={<AuthProvider  />}>
            <Route  element={<PrivateRoute  />}>
              <Route path="/" element={<Dashboard />}>
                    <Route path="profile"              element={<AuthRoute component={<Profile/>}           code="" />} />
                    <Route path="company_dashboard"    element={<AuthRoute component={<CompanyDashBoard/>}  code="" />} />
                    <Route path="user"                 element={<AuthRoute component={<User/>}              code="" />} />
                    <Route path="qr_batch"             element={<AuthRoute component={<QrBatch/>}           code="" />} />
                    <Route path="qr_code"              element={<AuthRoute component={<QrCode/>}            code="" />} />
                    <Route path="user_wallet/:user_id" element={<AuthRoute component={<UserWallet/>}        code="" />} />
                    <Route path="users_wallet_report/" element={<AuthRoute component={<UsersWalletReport/>} code="" />} />
                    <Route path="permissions/"         element={<AuthRoute component={<Permissions/>}       code="" />} />
                    <Route path="system_parameter/"    element={<AuthRoute component={<SystemParameter/>}   code="" />} />
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
