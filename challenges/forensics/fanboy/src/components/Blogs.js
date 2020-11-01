import React from "react";
import { ListGroup } from "react-bootstrap";

const Blogs = ({ blogs }) => {
    return (
        <div className="centerRelative">
            <ListGroup variant="flush" className="container">
                {blogs.map((blog) => (
                    <ListGroup.Item>
                        <p>
                            <b>{blog.title}</b>
                            {"  "}
                            <i>{blog.date}</i>
                        </p>
                        {blog.content}
                    </ListGroup.Item>
                ))}
            </ListGroup>
        </div>
    );
};

export default Blogs;
