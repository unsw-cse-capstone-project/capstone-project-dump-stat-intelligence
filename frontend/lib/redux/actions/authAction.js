import * as types from "../types";

import UserAPI from "../../api/user";
/*
AUTH

    Holds the redux state for account state

    auth : {
        isLoggedIn : bool,
        uid : int,
        nextPage : string,
        userInfo : {
            first : string,
            last : string,
            email : string,
            phone : string
        }
    }



*/
//NEED TO ADD DOCUMENTATION FOR API STUFF IN THIS ONE TOO

export const remove_favourite = (id) => async (dispatch) => {
  dispatch({
    type: types.REMOVE_FAVE,
    id : id
  })
}

export const add_favourite = (recipe) => async (dispatch) => {
  dispatch({
    type: types.ADD_FAVE,
    recipe: recipe

  })
}


export const clear_next = () => async (dispatch) => {
  dispatch({
    type: types.CLEAR_NEXT
  })
}


export const new_next = (next) => async (dispatch) => {
  dispatch({
    type: types.NEW_NEXT,
    next: next
  })
}

export const update_password = (old, pwd) => async (dispatch) => {
  //actually check that the password is valid
  //Don't need to dispatch anything cause state hasn't changed??
};

export const update_details = (first, last, email, phone) => async (
  dispatch
) => {
  //Do the actual account rego stuff...
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

export const register = (first, last, email, phone, pwd) => async (
  dispatch
) => {
  //Do the actual account rego stuff...
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

export const login = (email, pwd) => async (dispatch) => {
  //DO THE AUTHENTICATION STUFF TO LOGIN
  let userInfo = {
    email: email,
    phone: null,
  };

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

export const logout = () => async (dispatch) => {
  dispatch({
    type: types.LOGOUT,
  });
};
