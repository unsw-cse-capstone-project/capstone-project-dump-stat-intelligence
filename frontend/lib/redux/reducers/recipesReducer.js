import * as types from "../types";

const initalState = {
  recipes: [],
};
export const recipesReducer = (state = initalState, action) => {
  switch (action.type) {
    case types.RECIPES_UPDATE:
      return {
        recipes: action.recipes,
      };
    case types.RECIPES_CLEAR:
      return initalState;
    default:
      return state;
  }
};
