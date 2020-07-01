import * as types from "../types";

export const explore_add = (toAdd) => async dispatch => {
    //Do we do the recipeList here as well? something to consider
    dispatch({
        type : types.EXPLORE_ADD,
        toAdd : toAdd
    })
}

export const explore_remove = (toRemove) => async dispatch => {
    //Do we do the recipeList here as well? something to consider
    dispatch({
        type : types.EXPLORE_REMOVE,
        toRemove : toRemove.ingredient
    })
}

export const explore_clear = () => async dispatch => {
    //Do we do the recipeList here as well? something to consider
    dispatch({
        type : types.EXPLORE_CLEAR,
    })
}