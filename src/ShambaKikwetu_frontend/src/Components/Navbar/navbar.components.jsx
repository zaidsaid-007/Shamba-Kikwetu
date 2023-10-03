import React from 'react';
import { Link, Route, Routes } from 'react-router-dom';
import './navbar.style.css';
import SignUp from "../Auth/signup.component";
import SignInForm from "../Auth/login.component";

function Nav() {
    return (
        <div>
            <div className="main">
                <div className="logo">
                    <h1>Shamba Kikwetu</h1>
                </div>
                <Routes>
                    <Route
                        path="/"
                        element={
                            <div className="displays">
                                    <li>
                                        <Link to="/">Home</Link>
                                    </li>
                                    <li>
                                        <Link to="/search">Search</Link>
                                    </li>
                                    <li>
                                        <Link to="/about">About</Link>
                                    </li>
                                    <li>
                                        <Link to="/join-us">Log In</Link>
                                    </li>
                            </div>
                        }
                    />
                </Routes>

            </div>

            <Routes>
                <Route path="/join-us" element={<SignInForm/>} />
            </Routes>
        </div>
    );
}

export default Nav;
