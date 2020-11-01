import React, { useState } from "react";
import loginService from "../services/login";
import userService from "../services/user";

import { Button, Form } from "react-bootstrap";

const RegistrationForm = ({ setUser, setNotification }) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleRegistration = async (event) => {
        event.preventDefault();

        try {
            await userService.register({
                username,
                password,
            });

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
            setNotification(null);
            setUser(user);
        } catch (exception) {
            setNotification({
                message: exception.response.data.error,
                isError: true,
            });
        }
    };
    return (
        <div>
            <h1>Registration Form</h1>
            <hr />

            <Form onSubmit={handleRegistration}>
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
                        Note: Username is unique
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

export default RegistrationForm;
