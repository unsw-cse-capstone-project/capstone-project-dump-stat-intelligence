import * as types from "../types";

import store from "../store";

import UserAPI from "../../api/user";
import { getUser, setUser, removeUser } from "../../utils/localstorage";

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
            username : string,
            email : string,
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
export const update_details = (username, email, password) => async (
  dispatch
) => {
  let user = store.getState().auth;
  //INSERT API, tell backend to update respective details. Note not all deets may have actually changed - check to see which ones are different what is currntly in user.

  let userInfo = {
    username: username,
    email: email,
  };
  dispatch({
    type: types.UPDATE_DEETS,
    userInfo: userInfo,
  });
};

//NEEDS API
export const register = (username, email, password) => {
  return (dispatch) => {
    return UserAPI.register(username, email, password).then(res => {
      let data = res.data;
      setUser({id : data.id, token : data.token});

      dispatch({
        type: types.LOGIN,
        userInfo: data,
        uid: data.id,
        token: data.token,
      });
      return true;
    }).catch(err => {
      return false;
    })
  }
}



export const attemptLoginFromLocalStorage = () => async (dispatch) => {
  let user = getUser(); // this also sets the token

  if (!user) {
    // obviously not logged in
    return;
  }

  UserAPI.get(user.id)
    .then((res) => {
      let data = res.data;
      console.log("login success from localstorage");
      dispatch({
        type: types.LOGIN,
        userInfo: data,
        uid: data.id,
        token: user.token,
      });
    })
    .catch((err) => {
      console.log(err);
      if (err.statusCode == 401) {
        // Token has expired
        console.log("Token expired");
        removeUser();
        dispatch({ type: types.LOGOUT });
      }
    });
};

export const login = (email, password) => {
  return (dispatch) => {
    return UserAPI.login(email, password)
    .then(res => {
      let data = res.data;
      setUser({ id: data.id, token: data.token });

      dispatch({
        type: types.LOGIN,
        userInfo: data,
        uid: data.id,
        token: data.token
      });
      return {success : true};
    })
    .catch(err => {
      return {success : false};
    })
  }
}



export const logout = () => async (dispatch) => {
  UserAPI.logout()
    .then((res) => {
      console.log("API logout");
      removeUser();

      dispatch({
        type: types.LOGOUT,
      });
    })
    .catch((err) => {
      console.error(err.response);
    });
};
