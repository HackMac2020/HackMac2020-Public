const mongoose = require("mongoose");
const uniqueValidator = require("mongoose-unique-validator");

mongoose.set("useCreateIndex", true);
mongoose.set("useFindAndModify", false);

const userSchema = new mongoose.Schema({
    username: {
        type: String,
        unique: true,
    },
    creditCard: {
        type: String,
        minlength: 16,
        maxlength: 16,
    },
    passwordHash: String,
});

userSchema.set("toJSON", {
    transform: (document, returnedObject) => {
        returnedObject.id = returnedObject._id.toString();
        delete returnedObject._id;
        delete returnedObject.__v;
        delete returnedObject.passwordHash;
    },
});

userSchema.plugin(uniqueValidator);

const User = mongoose.model("User", userSchema);

module.exports = User;
