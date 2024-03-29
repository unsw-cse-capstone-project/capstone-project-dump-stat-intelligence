import * as types from "../types";

import store from "../store";
import RecipeAPI from "../../api/recipe";
import IngredientAPI from "../../api/ingredient";

/*
CREATE

    Holds the redux state for the creation and edit of recipes
    create : {
        title : string,
        id : int,
        cook_time : string,
        ingredients : [{}, {}, ...],
        method : [string, string, ...]
    }


*/
//NO API, frontend only
export const add_category = (name, category) => async (dispatch) => {
  dispatch({
    type: types.CAT_ADD_CREATE,
    name: name,
    category: category,
  });
};

//NO API, frontend only
export const remove_category = (name, category) => async (dispatch) => {
  dispatch({
    type: types.CAT_REMOVE_CREATE,
    name: name,
    category: category,
  });
};

export const create_ingredient = (name, category) => {
  IngredientAPI.create({ name, category });
};

//NO API, frontend only
export const add_ingredient = (ingredient) => async (dispatch) => {
  let ingredients = [...store.getState().create.ingredients];
  ingredients.push(ingredient);
  dispatch({
    type: types.UPDATE_CREATE,
    category: "ingredients",
    newVal: ingredients,
  });
};

//NO API, frontend only
export const remove_ingredient = (idx) => async (dispatch) => {
  let ingredients = [...store.getState().create.ingredients];
  ingredients.splice(idx, 1);
  dispatch({
    type: types.UPDATE_CREATE,
    category: "ingredients",
    newVal: ingredients,
  });
};

//NO API, frontend only
export const update_create = (category, newVal) => async (dispatch) => {
  dispatch({
    type: types.UPDATE_CREATE,
    category: category,
    newVal: newVal,
  });
};

export const save_create = () => async (dispatch) => {
  let recipe = store.getState().create;
  let tmp;
  let i;
  for (i = 0; i < recipe.ingredients.length; i++) {
    tmp = recipe.ingredients[i]["ingredient"]["name"];
    recipe.ingredients[i]["ingredient"] = tmp;
  }
  let user = store.getState().auth;

  RecipeAPI.create({ ...recipe, author: user.uid })
    .then((res) => {
      dispatch({
        type: types.LOAD_CREATE,
        loaded: recipe,
      });
      dispatch({
        type: types.CLEAR_CREATE, //Just removing all left over info
      });
      console.log("created recipe", { ...recipe, author: user.uid });
    })
    .catch((err) => {
      console.error(err.response);
    });
};

export const update_recipe = () => async (dispatch) => {
  let recipe = store.getState().create;
  let user = store.getState().auth;

  let updateRecipe = { ...recipe, author: user.uid };

  let updateIngredients = [];
  for (let ingredient of updateRecipe.ingredients) {
    updateIngredients.push({
      ingredient: ingredient.ingredient.name,
      adjective: ingredient.adjective,
      unit: ingredient.unit,
      amount: ingredient.amount,
    });
  }

  updateRecipe.ingredients = updateIngredients;

  console.log("Sending", updateRecipe);

  RecipeAPI.update(recipe.id, updateRecipe)
    .then((res) => {
      dispatch({
        type: types.CLEAR_CREATE, //Just removing all left over info
      });
      console.log("updating recipe", { ...recipe, author: user.uid });
    })
    .catch((err) => {
      console.error(err.response);
    });
};

//NO API, frontend only
export const clear_create = () => async (dispatch) => {
  dispatch({
    type: types.CLEAR_CREATE,
  });
};

export const load_create = (id) => async (dispatch) => {
  //TEMPORARY ... LOAD RECIPE LIKE WHEN YOU VEIW A RECIPE
  let recipe = null;
  RecipeAPI.get(id)
    .then(({ data }) => {
      recipe = data;
    })
    .then(() => {
      dispatch({
        type: types.LOAD_CREATE,
        loaded: { ...recipe, existing: true }, // Edit flag is for the create page
      });
    });
};
