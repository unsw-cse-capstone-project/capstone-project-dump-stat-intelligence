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
    type : types.PANTRY_CHANGE,
    ingredient : ingredient, 
    category : category,
    expiry : expiry,
  })
}

export const add = (ingredient) => async (dispatch) => {
  let auth = store.getState().auth;
  let response;
  let exists = false
  let i;

  if (auth.isLoggedIn) {
    response = await PantryAPI.get(10, 1, "");

    for (i = 0; i < response.data.length; i++) {
      if (response.data[i]['ingredient']['name'] == ingredient.name) {
        exists = true
      }
    }
  }

  if (exists == false) {
    await PantryAPI.add({'expiry_date': ingredient.expiry, 'user': auth.uid, 'ingredient': ingredient.name});

    let newIngredient = {
      category: ingredient.category,
      name: ingredient.name,
      expiry : ingredient.expiry
    };

    dispatch({
      type: types.PANTRY_ADD,
      newIngredient: newIngredient,
    });
  }
};

//NEEDS API
export const remove = (ingredient) => async (dispatch) => {
  let auth = store.getState().auth;
  let response;
  let i;

  if (auth.isLoggedIn) {
    response = await PantryAPI.get(10, 1, "");

    for (i = 0; i < response.data.length; i++) {

      if (response.data[i]['ingredient']['name'] == ingredient.ingredient) {
        console.log(response.data[i]['id'])
        await PantryAPI.delete(response.data[i]['id']);
      }
    }
  }
  let toRemove = {
    category: ingredient.category,
    ingredient: ingredient.ingredient,
  };
  let auth = store.getState().auth;
  dispatch({
