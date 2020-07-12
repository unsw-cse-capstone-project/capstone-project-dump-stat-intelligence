import axios from "axios";

import { SERVER_URL } from "../utils/constant";

let instance = axios.create({
  baseURL: SERVER_URL,
  header: {
    Authorization: `Token`,
    "content-type": "application/json",
  },
});

export default instance;
