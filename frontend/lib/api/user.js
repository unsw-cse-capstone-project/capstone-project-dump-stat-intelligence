import api from "./api";

const UserAPI = {
  login: async (username, password) => {
    try {
      return await api.post(`/user/login/`, { username, password });
    } catch (e) {
      console.error(e.response);
    }
  },
  logout: async () => {
    return await api.get(`/user/logout/`);
  },
  register: async (username, email, password) => {
    try {
      const res = await api.post(`/user/register/`, {
        username,
        email,
        password,
      });
      return res;
    } catch (e) {
      console.error(e.response);
    }
  },
  get: async (userId) => {
    return api.get(`/user/${userId}/`);
  },
};

export default UserAPI;
