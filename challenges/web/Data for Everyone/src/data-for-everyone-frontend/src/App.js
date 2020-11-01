import React, { useState, useEffect } from "react";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    Redirect,
} from "react-router-dom";
import LoginForm from "./components/LoginForm";
import Notification from "./components/Notification";
import Profile from "./components/Profile";
import RegistrationForm from "./components/RegistrationForm";
import Rooms from "./components/Rooms";
import userService from "./services/user";

import { Navbar, Nav, Button } from "react-bootstrap";

const App = () => {
    const [user, setUser] = useState(null);
    const [notification, setNotification] = useState(null);

    const linkStyle = {
        padding: 5,
        color: "white",
        textDecoration: "none",
    };
    useEffect(() => {
        const loggedUserJSON = window.localStorage.getItem(
            "loggedHotelappUser"
        );
        if (loggedUserJSON) {
            const user = JSON.parse(loggedUserJSON);
            userService.setToken(user.token);
            setUser(user);
        }
    }, []);

    return (
        <Router>
            <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
                <Navbar.Brand href="#">
                    <Link style={linkStyle} to="/">
                        Hotels Galore
                    </Link>
                </Navbar.Brand>
                <Nav className="mr-auto">
                    <Nav.Link href="#" as="span">
                        <Link style={linkStyle} to="/">
                            Home
                        </Link>
                    </Nav.Link>
                    <Nav.Link href="#" as="span">
                        <Link style={linkStyle} to="/rooms">
                            Rooms
                        </Link>
                    </Nav.Link>
                    {!user ? (
                        <>
                            <Nav.Link href="#" as="span">
                                <Link style={linkStyle} to="/register">
                                    Register
                                </Link>
                            </Nav.Link>
                            <Nav.Link href="#" as="span">
                                <Link style={linkStyle} to="/login">
                                    Login
                                </Link>
                            </Nav.Link>
                        </>
                    ) : (
                        <Nav.Link href="#" as="span">
                            <Link style={linkStyle} to={"/profile"}>
                                Profile
                            </Link>
                        </Nav.Link>
                    )}
                </Nav>

                {user ? (
                    <div>
                        <Navbar.Text style={{ paddingRight: "20px" }}>
                            Signed in as: {user.username}
                        </Navbar.Text>
                        <Button
                            variant="primary"
                            onClick={() => {
                                setUser(null);
                                window.localStorage.removeItem(
                                    "loggedHotelappUser"
                                );
                            }}
                        >
                            Logout
                        </Button>
                    </div>
                ) : (
                    <div>
                        <Button
                            variant="primary"
                            onClick={() => {
                                setUser(null);
                                window.localStorage.removeItem(
                                    "loggedHotelappUser"
                                );
                            }}
                        >
                            <Link style={linkStyle} to="/login">
                                Login
                            </Link>
                        </Button>
                    </div>
                )}
            </Navbar>

            <div
                className="container"
                style={{ paddingTop: "40px", paddingBottom: "20px" }}
            >
                <Notification notification={notification} />

                <Switch>
                    <Route path="/rooms">
                        <Rooms setNotification={setNotification} />
                    </Route>
                    <Route path="/profile">
                        {user ? (
                            <Profile
                                user={user}
                                setNotification={setNotification}
                            />
                        ) : (
                            <Redirect to="/login" />
                        )}
                    </Route>
                    <Route path="/login">
                        {!user ? (
                            <LoginForm
                                setUser={setUser}
                                setNotification={setNotification}
                            />
                        ) : (
                            <Redirect to="/profile" />
                        )}
                    </Route>
                    <Router path="/register">
                        {!user ? (
                            <RegistrationForm
                                setUser={setUser}
                                setNotification={setNotification}
                            />
                        ) : (
                            <Redirect to="/profile" />
                        )}
                    </Router>
                    <Route path="/">
                        <h1>Hotels Galore</h1>
                        <hr />
                        <p>
                            Welcome to Hotels Galore! Find the perfect room for
                            you to sleep comfortably in.
                        </p>
                    </Route>
                </Switch>
            </div>
        </Router>
    );
};

export default App;
