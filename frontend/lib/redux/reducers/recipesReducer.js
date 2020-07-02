import * as types from "../types";


const initalState = {
    recipes : [
        {name : "Sushi"},
        {name : "meat"},
        {name : "beg"},
      ]
}
export const recipesReducer = (state = initalState, action) => {
    switch (action.type) {
        case types.RECIPES_UPDATE:
            return {
                recipes : action.recipes
            }        
        case types.RECIPES_CLEAR:
            return initalState
        default:
            return state
    }
}