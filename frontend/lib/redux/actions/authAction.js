import * as types from "../types";

import store from "../store";

import UserAPI from "../../api/user";
/*
AUTH

    Holds the redux state for account state

    auth : {
        isLoggedIn : bool,
        uid : int,
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
    id : id
  })
}

//NEEDS API
export const add_favourite = (recipe) => async (dispatch) => {
  let user = store.getState().auth;

  //INSERT API, tell backend to add recipe <id> as favourite from user
  
  dispatch({
    type: types.ADD_FAVE,
    recipe: recipe

  })
}

//No API, only used for frontend
export const clear_next = () => async (dispatch) => {
  dispatch({
    type: types.CLEAR_NEXT
  })
}

//No API, frontend use only
export const new_next = (next) => async (dispatch) => {
  dispatch({
    type: types.NEW_NEXT,
    next: next
  })
}

//NEEDS API
export const update_password = (old, pwd) => async (dispatch) => {
  let user = store.getState().auth;
  //INSERT API, no frontend change but tell backend to update password for user  
};


//NEEDS API
export const update_details = (first, last, email, phone) => async (dispatch) => {
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
export const register = (first, last, email, phone, pwd) => async (dispatch) => {
  //INSERT API, register new user with backend

  let userInfo = {
    first: first,
    last: last,
    email: email,
    phone: phone,
  };


  UserAPI.register(`{first} {last}`, email, pwd)
    .then((res) => {
      // TODO: do something with token here that comes back from response

      dispatch({
        type: types.LOGIN,
        userInfo: userInfo,
        uid: 0,
      });
    })
    .catch((err) => {
      console.error(err);
    });
};


//NEEDS API
export const login = (email, pwd) => async (dispatch) => {
  let userInfo = {
    email: email,
    phone: null,
  };
  
  //INSET API, login and return token TODO: NOT SET UP WITH REDUX YET
  UserAPI.login(email, pwd)
    .then((res) => {
      // TODO: do something with token here that comes back from response

      dispatch({
        type: types.LOGIN,
        userInfo: userInfo,
        uid: 0,
      });
    })
    .catch((err) => {
      console.error(err);
    });
};


//NEEDS API
export const logout = () => async (dispatch) => {
  //INSERT API, tell backend to invalidate the session token
  dispatch({
    type: types.LOGOUT,
  });
};
