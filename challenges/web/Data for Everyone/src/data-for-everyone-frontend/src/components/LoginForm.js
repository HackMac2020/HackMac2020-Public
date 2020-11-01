import React, { useState } from "react";
import loginService from "../services/login";
import userService from "../services/user";

import { Button, Form } from "react-bootstrap";

const LoginForm = ({ setUser, setNotification }) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const handleLogin = async (event) => {
        event.preventDefault();

        try {
            const user = await loginService.login({
                username,
                password,
            });

            window.localStorage.setItem(
                "loggedHotelappUser",
                JSON.stringify(user)
            );

            setUsername("");
            setPassword("");
            userService.setToken(user.token);
            setNotification(null);
            setUser(user);
        } catch (exception) {
            setNotification({ message: "Wrong credentials", isError: true });
        }
    };

    return (
        <div>
            <h1>Login Form</h1>
            <hr />
            <Form onSubmit={handleLogin}>
                <Form.Group>
                    <Form.Label>Username</Form.Label>
                    <Form.Control
                        id="username"
                        type="text"
                        placeholder="Enter username"
                        value={username}
                        onChange={({ target }) => setUsername(target.value)}
                    />
                    <Form.Text className="text-muted">
                        Note: Kept the password as default for the admin account
                        for ease of testing
                    </Form.Text>
                </Form.Group>

                <Form.Group controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control
                        id="password"
                        type="password"
                        placeholder="Enter password"
                        value={password}
                        onChange={({ target }) => setPassword(target.value)}
                    />
                </Form.Group>
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form>
        </div>
    );
};

export default LoginForm;
