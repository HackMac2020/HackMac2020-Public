import axios from "axios";
const baseUrl = "/api/users";

let token = "";

const setToken = (newToken) => {
    token = `bearer ${newToken}`;
};

const register = async (credentials) => {
    const response = await axios.post(baseUrl, credentials);
    return response.data;
};

const get = async (id) => {
    const config = {
        headers: {
            Authorization: token,
        },
    };
    const response = await axios.get(`${baseUrl}/${id}`, config);
    return response.data;
};

export default { register, get, setToken };
