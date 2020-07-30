import * as types from "../types";
import store from "../store";

import PantryAPI from "../../api/pantry";

/*
PANTRY

    Holds the redux state for the user's pantry ingredients

    pantry : {
        category : [{ingredient}, {}, {}, ...]
    }

*/

//NO API, frontend only
export const change = (ingredient, category, expiry) => async (dispatch) => {
  dispatch({
    type: types.PANTRY_CHANGE,
    ingredient: ingredient,
    category: category,
    expiry: expiry,
  });
};

//NEEDS API
export const add = (ingredient) => async (dispatch) => {
  let auth = store.getState().auth;

  if (auth.isLoggedIn) {
    // TODO: token auth
    // TODO: is ingredient.ingredient the primary key of
    // TODO: error handle
    //await PantryAPI.add(ingredient.ingredient, "");
  }
  let newIngredient = {
    category: ingredient.category,
    name: ingredient.name,
    expiry: ingredient.expiry,
  };
  dispatch({
    type: types.PANTRY_ADD,
    newIngredient: newIngredient,
  });
};

//NEEDS API
export const remove = (ingredient) => async (dispatch) => {
  let auth = store.getState().auth;

  if (auth.isLoggedIn) {
    //INSER API, user is logged in so update pantry on backend
    // TODO: token auth
    // TODO: is ingredient.ingredient the primary key of
    // TODO: error handle
    //await PantryAPI.delete(ingredient.ingredient, "");
  }
  let toRemove = {
    category: ingredient.category,
    ingredient: ingredient.ingredient,
  };
  dispatch({
    type: types.PANTRY_REMOVE,
    toRemove: toRemove,
  });
};

export const get_pantry = () => async (dispatch) => {
  let auth = store.getState().auth;
  let newPantry = {};

  if (auth.isLoggedIn) {
    response = await PantryAPI.get();
    newPantry = response.data;
  }

  dispatch({
    type: types.PANTRY_GET,
    pantry: newPantry,
  });
};
