import * as types from "../types";

import store from "../store";

import UserAPI from "../../api/user";
import CookbookAPI from "../../api/cookbook";
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

export const remove_favourite = (id) => async (dispatch) => {
  let user = store.getState().auth;

  CookbookAPI.delete(id)
    .then((res) => {
      // console.log(res);
    })
    .catch((err) => console.error(err.response));

  dispatch({
    type: types.REMOVE_FAVE,
    id: id,
  });
};

export const add_favourite = (recipe) => async (dispatch) => {
  let user = store.getState().auth;

  CookbookAPI.add(recipe.id)
    .then((res) => {
      // console.log(res);
    })
    .catch((err) => console.error(err.response));

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

export const update_password = (password) => async (dispatch) => {
  let user = store.getState().auth;

  UserAPI.update(
    user.uid,
    user.userInfo.username,
    user.userInfo.email,
    password
  )
    .then((res) => {
      let data = res.data;
      // don't need to update anything on frontend
    })
    .catch((err) => {
      console.error(err.response);
    });
};

export const update_details = (username, email, old_password) => async (
  dispatch
) => {
  let user = store.getState().auth;

  UserAPI.update(user.uid, username, email, old_password)
    .then((res) => {
      let data = res.data;

      let userInfo = {
        username: username,
        email: email,
      };
      dispatch({
        type: types.UPDATE_DEETS,
        userInfo: userInfo,
      });
    })
    .catch((err) => {
      console.error(err.response);
    });
};

export const register = (username, email, password) => {
  return (dispatch) => {
    return UserAPI.register(username, email, password)
      .then((res) => {
        let data = res.data;
        setUser({ id: data.id, token: data.token });

        dispatch({
          type: types.LOGIN,
          userInfo: data,
          uid: data.id,
          token: data.token,
        });
        return true;
      })
      .catch((err) => {
        return false;
      });
  };
};

export const attemptLoginFromLocalStorage = () => async (dispatch) => {
  let user = getUser(); // this also sets the token

  if (!user) {
    // obviously not logged in
    return false;
  }

  return UserAPI.get(user.id)
    .then((res) => {
      let data = res.data;
      // console.log("login success from localstorage");

      // Then get the favourite recipes for this user
      CookbookAPI.get().then((res) => {
        let favourites = res.data;
        dispatch({
          type: types.LOGIN,
          userInfo: data,
          uid: data.id,
          token: user.token,
          favourites,
        });
      });
      return true;
    })
    .catch((err) => {
      console.log(err);
      if (err.statusCode == 401) {
        // Token has expired
        console.log("Token expired");
        removeUser();
        dispatch({ type: types.LOGOUT });
      }
      return false;
    });
};

export const login = (email, password) => {
  return (dispatch) => {
    removeUser();

    return UserAPI.login(email, password)
      .then((res) => {
        let data = res.data;
        setUser({ id: data.id, token: data.token });

        CookbookAPI.get().then((res) => {
          let favourites = res.data;
          dispatch({
            type: types.LOGIN,
            userInfo: data,
            uid: data.id,
            token: data.token,
            favourites,
          });
        });

        return { success: true };
      })
      .catch((err) => {
        return { success: false };
      });
  };
};

/*
  Log the user out
*/
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

/*
  Get recipes that belong to the current logged in user
*/
export const get_owned = () => async (dispatch) => {
  UserAPI.owned()
    .then((res) => {
      dispatch({
        type: types.LOAD_OWNED,
        owned: res.data,
      });
    })
    .catch((err) => {
      console.log(err.response);
    });
};
