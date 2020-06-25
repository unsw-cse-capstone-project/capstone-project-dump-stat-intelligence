import axios from "axios";
import { SERVER_URL } from "../utils/constant";
import paging from "../utils/paging";

const UserAPI = {
  login: async (email, password) => {
    try {
      const res = await axios.post(
        `${SERVER_URL}/user/login`,
        JSON.stringify({ user: { email, password } })
      );
      return res;
    } catch (e) {
      return e.response;
    }
  },
  register: async (name, email, password) => {
    try {
      const res = await axios.post(
        `${SERVER_URL}/user/register`,
        JSON.stringify({ user: { name, email, password } })
      );
      return res;
    } catch (e) {
      return e.response;
    }
  },
};

export default UserAPI;
