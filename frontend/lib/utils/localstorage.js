import api from "../api/api";

const getUser = () => {
  let user = JSON.parse(localStorage.getItem("user"));
  if (user == null) {
    return null;
  }
  setTokenHeader(user.token);
  return user;
};

const setUser = (user) => {
  setTokenHeader(user.token);
  return localStorage.setItem("user", JSON.stringify(user));
};

const removeUser = () => {
  return localStorage.removeItem("user");
};

const setTokenHeader = (token) => {
  api.defaults.headers.common["Authorization"] = `Token ${token}`;
};

export { getUser, setUser, removeUser };
