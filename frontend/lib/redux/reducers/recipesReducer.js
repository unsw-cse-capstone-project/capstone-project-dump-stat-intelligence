import * as types from "../types";

const initalState = {
  recipes: [],
  suggestion: null,
};
export const recipesReducer = (state = initalState, action) => {
  switch (action.type) {
    case types.RECIPES_UPDATE:
      return {
        recipes: action.recipes,
        suggestion: action.suggestion
      };
    case types.RECIPES_CLEAR:
      return {
        ...initalState
      };
    default:
      return state;
  }
};
