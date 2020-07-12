import * as types from "../types";

import store from "../store";

import UserAPI from "../../api/user";
import { getToken, setToken, removeToken } from "../../utils/token";

/*
AUTH

    Holds the redux state for account state

    auth : {
        isLoggedIn : bool,
        uid : int,
        token : string,
        nextPage : string,
        favourites : [{recipe}, ...],
        owned : [{recipe}, ...]
        userInfo : {
            first : string,
            last : string,
            email : string,
            phone : string
        }
    }



*/

//NEEDS API
export const remove_favourite = (id) => async (dispatch) => {
  let user = store.getState().auth;

  //INSERT API, tell backend to remove recipe <id> as favourite from user

  dispatch({
    type: types.REMOVE_FAVE,
    id: id,
  });
};

//NEEDS API
export const add_favourite = (recipe) => async (dispatch) => {
  let user = store.getState().auth;

  //INSERT API, tell backend to add recipe <id> as favourite from user

  dispatch({
    type: types.ADD_FAVE,
    recipe: recipe,
  });
};

//No API, only used for frontend
export const clear_next = () => async (dispatch) => {
  dispatch({
    type: types.CLEAR_NEXT,
  });
};

//No API, frontend use only
export const new_next = (next) => async (dispatch) => {
  dispatch({
    type: types.NEW_NEXT,
    next: next,
  });
};

//NEEDS API
export const update_password = (old, pwd) => async (dispatch) => {
  let user = store.getState().auth;
  //INSERT API, no frontend change but tell backend to update password for user
};

//NEEDS API
export const update_details = (first, last, email, phone) => async (
  dispatch
) => {
  let user = store.getState().auth;
  //INSERT API, tell backend to update respective details. Note not all deets may have actually changed - check to see which ones are different what is currntly in user.

  let userInfo = {
    first: first,
    last: last,
    email: email,
    phone: phone,
  };
  dispatch({
    type: types.UPDATE_DEETS,
    userInfo: userInfo,
  });
};

//NEEDS API
export const register = (username, email, password) => async (dispatch) => {
  //INSERT API, register new user with backend
  console.log("REGISTER EVENT!");
  UserAPI.register(username, email, password)
    .then((res) => {
      let data = res.data;
      setToken(data.token);

      dispatch({
        type: types.LOGIN,
        userInfo: data,
        uid: data.id,
        token: data.token,
      });
    })
    .catch((err) => {
      console.error(err);
    });
};

export const login = (email, password) => async (dispatch) => {
  console.log("LOGIN ACTION!");
  UserAPI.login(email, password)
    .then((res) => {
      let data = res.data;
      setToken(data.token);

      dispatch({
        type: types.LOGIN,
        userInfo: data,
        uid: data.id,
        token: data.token,
      });
    })
    .catch((err) => {
      console.log("redux error");
      console.error(err);
      console.error(err.response);
    });
};

export const logout = () => async (dispatch) => {
  UserAPI.logout()
    .then((res) => {
      console.log("API logout");
      removeToken();

      dispatch({
        type: types.LOGOUT,
      });
    })
    .catch((err) => {
      console.error(err.response);
    });
};
