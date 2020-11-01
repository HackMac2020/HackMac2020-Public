const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const usersRouter = require("express").Router();
const User = require("../models/user");

usersRouter.get("/", async (request, response) => {
    const users = await User.find({});
    response.json(users);
});

usersRouter.post("/", async (request, response) => {
    const body = request.body;

    const saltRounds = 10;
    const passwordHash = await bcrypt.hash(body.password, saltRounds);

    const user = new User({
        username: body.username,
        creditCard: body.creditCard,
        passwordHash,
    });

    const savedUser = await user.save();

    response.json(savedUser);
});

usersRouter.get("/:id", async (request, response) => {
    const decodedToken = jwt.verify(request.token, process.env.SECRET);

    if (!decodedToken || !decodedToken.id) {
        return response.status(401).send({ error: "token missing or invalid" });
    }

    const user = await User.findById(decodedToken.id);

    response.json(user);
});

usersRouter.put("/:id", async (request, response) => {
    const decodedToken = jwt.verify(request.token, process.env.SECRET);

    if (!decodedToken || !decodedToken.id) {
        return response.status(401).send({ error: "token missing or invalid" });
    }

    const user = await User.findById(decodedToken.id);

    if (user.username === "admin") {
        return response.status(401).send({
            error:
                "cannot change profile details of admin for security purposes",
        });
    }

    const body = request.body;

    // Ceebs implementing password change
    const tempUser = {
        creditCard: body.creditCard || user.creditCard,
    };

    const updatedUser = await User.findByIdAndUpdate(
        request.params.id,
        tempUser,
        {
            new: true,
            runValidators: true,
        }
    );

    response.json(updatedUser);
});

module.exports = usersRouter;
