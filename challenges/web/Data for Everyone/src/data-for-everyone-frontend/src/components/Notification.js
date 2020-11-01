import React from "react";

const error = {
    color: "red",
    background: "lightgrey",
    fontSize: "20px",
    borderStyle: "solid",
    borderRadius: "5px",
    padding: "10px",
    marginBottom: "10px",
};

const success = {
    color: "green",
    background: "lightgrey",
    fontSize: "20px",
    borderStyle: "solid",
    borderRadius: "5px",
    padding: "10px",
    marginBottom: "10px",
};

const Notification = ({ notification }) => {
    if (!notification || !notification.message) {
        return null;
    }
    if (notification.isError) {
        return <div style={error}>{notification.message}</div>;
    } else {
        return <div style={success}>{notification.message}</div>;
    }
};

export default Notification;
