const getToken = () => {
  return localStorage.getItem("token");
};

const setToken = (token) => {
  return localStorage.setItem("token", token);
};

const removeToken = () => {
  return localStorage.removeItem("token");
};

export { getToken, setToken, removeToken };
