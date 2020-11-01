import React from "react";
import { Container, CardColumns, Card, Button } from "react-bootstrap";

const rooms = [
    {
        id: 0,
        name: "Luxury Muxury",
        rate: "$50/d",
        description: "Only for kings and queens!",
    },
    {
        id: 1,
        name: "The Ghostly Shadows",
        rate: "$1/d",
        description: "Too spooky for me",
    },
    {
        id: 2,
        name: "Party Marty",
        rate: "$20/d",
        description: "Party animals ONLY. Yeehaw.",
    },
    {
        id: 3,
        name: "The Zoo",
        rate: "$30/d",
        description: "Animal themed room with lots of stuffed animals.",
    },
    {
        id: 4,
        name: "The Aquarium",
        rate: "$30/d",
        description: "Swim with the dolphins with our water themed room.",
    },
    {
        id: 5,
        name: "Common Room",
        rate: "$10/d",
        description: "For commoners like oessatreB nadroJ",
    },
];

const Rooms = ({ setNotification }) => {
    return (
        <Container>
            <h1>Rooms</h1>
            <CardColumns>
                {rooms.map((room) => {
                    return (
                        <Card key={room.id}>
                            <Card.Body>
                                <Card.Title>{room.name}</Card.Title>
                                <Card.Text>
                                    <small>{room.rate}</small>
                                </Card.Text>
                                <Card.Text>{room.description}</Card.Text>
                                <Button
                                    onClick={() => {
                                        setNotification({
                                            message: "Not implemented yet",
                                            isError: true,
                                        });
                                    }}
                                >
                                    Book now!
                                </Button>
                            </Card.Body>
                        </Card>
                    );
                })}
            </CardColumns>
        </Container>
    );
};

export default Rooms;
