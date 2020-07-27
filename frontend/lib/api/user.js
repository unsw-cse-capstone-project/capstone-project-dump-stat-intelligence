import api from "./api";

const UserAPI = {
  login: async (username, password) => {
    return await api.post(`/user/login/`, { username, password });
  },
  logout: async () => {
    return await api.get(`/user/logout/`);
  },
  register: async (username, email, password) => {
    const res = await api.post(`/user/register/`, {
      username,
      email,
      password,
    });
    return res;
  },
  get: async (userId) => {
    return await api.get(`/user/${userId}/`);
  },
  owned: async () => {
    return await api.get(`/user/myrecipes/`);
  },
  update: async (userId, username, email, password) => {
    return await api.put(`/user/${userId}/`, { username, password, email });
  },
};

export default UserAPI;
