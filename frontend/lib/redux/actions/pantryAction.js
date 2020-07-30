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

export const change = (ingredient, category, expiry) => async (dispatch) => {
  let pantry = await PantryAPI.get(10, 1, "");
  let i;
  for (i = 0; i < pantry.data.length; i++) {
    if (pantry.data[i]["ingredient"]["name"] == ingredient) {
      await PantryAPI.update(pantry.data[i]["id"], {expiry_date:expiry});
    }
  }

  dispatch({
    type: types.PANTRY_CHANGE,
    ingredient: ingredient,
    category: category,
    expiry: expiry,
  });
};

export const add = (ingredient) => async (dispatch) => {
  let auth = store.getState().auth;
  let response;
  let exists = false;
  let i;

  if (auth.isLoggedIn) {
    response = await PantryAPI.get(10, 1, "");

    for (i = 0; i < response.data.length; i++) {
      if (response.data[i]["ingredient"]["name"] == ingredient.name) {
        exists = true;
      }
    }
  }

  if (exists == false) {
    await PantryAPI.add({
      expiry_date: ingredient.expiry,
      user: auth.uid,
      ingredient: ingredient.name,
    });

    let newIngredient = {
      category: ingredient.category,
      name: ingredient.name,
      expiry: ingredient.expiry,
    };

    dispatch({
      type: types.PANTRY_ADD,
      newIngredient: newIngredient,
    });
  }
};

export const remove = (ingredient) => async (dispatch) => {
  let auth = store.getState().auth;
  let response;
  let i;

  if (auth.isLoggedIn) {
    response = await PantryAPI.get(10, 1, "");

    for (i = 0; i < response.data.length; i++) {
      if (response.data[i]["ingredient"]["name"] == ingredient.ingredient) {
        console.log(response.data[i]["id"]);
        await PantryAPI.delete(response.data[i]["id"]);
      }
    }
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

export const get_pantry = () => {
  return async (dispatch) => {
    let auth = store.getState().auth;
    if (auth.isLoggedIn) {
      PantryAPI.get(10, 1, "")
      .catch(err => {
        dispatch({
          type: types.PANTRY_GET,
          pantry: {}
        })
      })
      .then(res => {
        console.log(res.data);
        let newPantry = {}
        for (var i = 0; i < res.data.length; i++) {
          let ing = res.data[i];
          if (!(ing.ingredient.category.name in newPantry)) {
            newPantry[ing.ingredient.category.name] = []
          }
          newPantry[ing.ingredient.category.name].push({
            name : ing.ingredient.name,
            expiry : ing.expiry_date
          })
        }
        
        
        console.log(newPantry)
        dispatch({
          type: types.PANTRY_GET,
          pantry: {...newPantry}
        })
      })
      
    }
    
  }
}

