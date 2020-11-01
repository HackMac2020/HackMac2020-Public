import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import { Container, Row, Col } from "react-bootstrap";
import "./App.css";
import Blogs from "./components/Blogs";

const initialBlogs = [
    {
        title: "The beginning",
        date: "27 September 2020",
        content: (
            <div>
                <p>Welcome to my new site!</p>
                <p>
                    I made this <i>pro</i> site like a <i>pro</i> dev with{" "}
                    <i>pro</i> tools on my
                    <b> macbook pro</b>. I used <i>git</i> and <git>react</git>{" "}
                    to help me manage and style it!
                </p>
                <p>Stay tuned for new posts about my fanboy adventures."</p>
            </div>
        ),
    },
    {
        title: "Please send me OP's address",
        date: "29 September 2020",
        content: (
            <div>
                <img alt="random meme" width="80%" src="https://i.redd.it/sqqzfvqnjpx11.jpg" />
                <br></br>
                <br></br>
                <p>I WILL DESTROY THE WINDOWS NERDS</p>
            </div>
        ),
    },
];

function App() {
    return (
        <Container fluid style={{ textAlign: "center" }}>
            <Router>
                <Row
                    className="stickyNavbar my-auto justify-content-md-center"
                    style={{
                        backgroundColor: "white",
                    }}
                >
                    <Col xs>
                        <Link to="/">Home</Link>
                    </Col>
                    <Col xs>
                        <Link to="/blogs">Blogs</Link>
                    </Col>
                </Row>

                <Switch>
                    <Route path="/blogs">
                        <Blogs blogs={initialBlogs} />
                    </Route>
                    <Route path="/">
                        <div className="center">
                            <Row className="justify-content-md-center">
                                <Col>
                                    <h1>Welcome to AppleLand!</h1>
                                </Col>
                            </Row>
                            <Row className="justify-content-md-center">
                                <Col>
                                    <img
                                        alt="Apple logo"
                                        style={{
                                            padding: "2rem",
                                            height: "10rem",
                                        }}
                                        src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/1200px-Apple_logo_black.svg.png"
                                    ></img>
                                </Col>
                            </Row>

                            <Row>
                                <Col>
                                    <h2>
                                        Check out my{" "}
                                        <Link to="/blogs">Blogs</Link> on my
                                        future plans for this site
                                    </h2>
                                </Col>
                            </Row>
                        </div>
                    </Route>
                </Switch>
            </Router>
        </Container>
    );
}

export default App;
