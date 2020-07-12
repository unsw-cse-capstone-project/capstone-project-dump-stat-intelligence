import api from "./api";
import paging from "../utils/paging";

const UserAPI = {
  login: async (username, password) => {
    try {
      const res = await api.post(
        `/user/login/`,
        JSON.stringify({ username, password })
      );
      return res;
    } catch (e) {
      return e.response;
    }
  },
  logout: async () => {
    return await api.get(`/user/logout/`);
  },
  register: async (username, email, password) => {
    try {
      const res = await api.post(
        `/user/register`,
        JSON.stringify({ username, email, password })
      );
      return res;
    } catch (e) {
      return e.response;
    }
  },
};

export default UserAPI;
