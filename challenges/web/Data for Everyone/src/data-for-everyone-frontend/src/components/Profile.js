import React, { useState, useEffect } from "react";
import userService from "../services/user";

import { Button, Table } from "react-bootstrap";

const Profile = ({ user, setNotification }) => {
    const [fullUser, setFullUser] = useState(null);

    useEffect(() => {
        const getUser = async () => {
            const tempUserData = await userService.get(user.id);
            setFullUser(tempUserData);
        };

        getUser();
    }, [user.id]);

    return (
        <div>
            <h1>Profile</h1>
            <hr />
            <Table>
                <tr>
                    <td>Username</td>
                    <td>{user.username}</td>
                </tr>
                <tr>
                    <td>Credit Card</td>
                    {fullUser && fullUser.creditCard ? (
                        <td>
                            ************
                            {fullUser.creditCard.substring(12, 16)}
                        </td>
                    ) : (
                        <td>
                            <p>You need to set a credit card</p>
                            <Button
                                variant="primary"
                                onClick={() => {
                                    setNotification({
                                        message: "Not implemented yet",
                                        isError: true,
                                    });
                                }}
                            >
                                Set credit card
                            </Button>
                        </td>
                    )}
                </tr>
            </Table>
        </div>
    );
};

export default Profile;
