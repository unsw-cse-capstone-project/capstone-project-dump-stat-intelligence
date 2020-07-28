import api from "../api/api";

const getUser = () => {
  let user = JSON.parse(localStorage.getItem("user"));
  if (user == null || user == undefined) {
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
  removeTokenHeader();
  return localStorage.removeItem("user");
};

const setTokenHeader = (token) => {
  api.defaults.headers.common["Authorization"] = `Token ${token}`;
};


const removeTokenHeader = () => {
  delete api.defaults.headers.common["Authorization"];
}

export { getUser, setUser, removeUser };
