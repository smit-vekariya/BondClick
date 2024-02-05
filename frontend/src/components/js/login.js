import React from "react";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { Link } from "react-router-dom";
import logo from './logo-no-background.png';
import{useContext} from 'react';
import { AuthContext } from "../../context/AuthContext";


export default function  Login(){
    const {loginUser} = useContext(AuthContext)
    return(
        <>
            <div className="home_nav">
                <Link to="/home"><Button variant="outline-dark">Home</Button></Link>
                <Link to="/register"><Button variant="outline-warning">Sign Up</Button></Link>
            </div>
            <div className="main_div">
                <div className="login_div">
                    <Form onSubmit={loginUser}>
                        <Form.Group className="mb-3" controlId="formBasicEmail" style={{textAlign:'center'}}>
                            <img src={logo} alt="logo-no-background.png" style={{width:"300px",marginBottom:"15px"}}></img>
                            <h2 className="fontfamily">Login</h2>
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="formBasicEmail">
                            <Form.Label>Username</Form.Label>
                            <Form.Control type="text" name="username" className="input_field" required/>
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="formBasicPassword">
                            <Form.Label>Password</Form.Label>
                            <Form.Control type="password" name="password" className="input_field" required/>
                        </Form.Group>
                        <div className="d-grid gap-2">
                        <Button variant="primary" size="lg" className="main_button" type="submit">
                            Login
                        </Button>
                        </div>
                    </Form>
                </div>
            </div>
        </>
    )
}