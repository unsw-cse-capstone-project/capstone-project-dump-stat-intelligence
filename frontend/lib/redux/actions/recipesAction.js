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

export const recipes_unsuggest = () => async dispatch => {
  dispatch({
    type: types.RECIPES_UNSUGGEST,
  })
}

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

  let ingredientStr = explore.ingredients.join(",");

  let mealCats = Object.keys(explore.filters.meal)
    .filter((key) => explore.filters.meal[key])
    .join("+");
  let mealStr = mealCats.length > 0 ? mealCats : "";

  let dietCats = Object.keys(explore.filters.diet)
    .filter((key) => explore.filters.diet[key])
    .join("+");
  let dietStr = dietCats.length > 0 ? dietCats : "";

  // get all recipes
  // TODO: backend has changed format to now have match_percentage
  // going to just extract recipes for now
  const recipes = await RecipeAPI.getAll(mealStr, dietStr, ingredientStr);
  let extractedRecipes = [];
  let suggestion = null;
  recipes.data.forEach((r) => {
    if (r.suggestion) {
      suggestion = r.suggestion;
    } else {
      extractedRecipes.push({...r.recipe, missing_ing : r.missing_ing, match_percentage : r.match_percentage, nearly_expiring : r.nearly_expiring});
    }
  });
  if (explore.ingredients.length === 0) suggestion = null;
  dispatch({
    type: types.RECIPES_UPDATE,
    recipes: extractedRecipes,
    suggestion : suggestion,
  });
};
