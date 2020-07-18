import * as types from "../types";

import store from "../store";

import RecipeAPI from "../../api/recipe";

/*
RECIPES

    Holds the redux state for the recipes on the explore page
    (currently a dict cause if we want to do pagination could lazy load extra pages to dict)
    recipes : {
        recipes : [{recipe}, {recipe}, ...]
    }


*/

//NO API, MAY NOT EVEN BE NECESSARY
export const recipes_clear = () => async (dispatch) => {
  dispatch({
    type: types.RECIPES_CLEAR,
  });
};

// NEW SEARCH
export const recipes_update = () => async (dispatch) => {
  let explore = store.getState().explore;

  // TODO: use .get(searchParams) to take into account explore parameters

  // get all recipes
  const recipes = await RecipeAPI.getAll();
  dispatch({
    type: types.RECIPES_UPDATE,
    recipes: recipes.data,
  });
};
