import axios from "axios";

import { SERVER_URL } from "../utils/constant";

let instance = axios.create({
  baseURL: SERVER_URL,
  header: {
    "content-type": "application/json",
    // No authorization tokens set here until user login / localstorage login event occurs
    // token is set in getUser / setUser in utils/localstorage
  },
});

export default instance;
