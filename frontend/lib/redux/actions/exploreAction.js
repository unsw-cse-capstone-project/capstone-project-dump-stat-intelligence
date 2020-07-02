import * as types from "../types";
import store from "../store";

export const explore_all = () => async dispatch => {
    
    //Add all the ingredients in the pantry to the running list
    let pantry = store.getState().pantry;
    let newList = []
    let i = 0;
    Object.keys(pantry).map((key) => {
        for (i = 0; i < pantry[key].length; i++) {
            newList.push(pantry[key][i].name)
        }
    })
    dispatch({
        type : types.EXPLORE_ALL,
        newList : newList
    })

}

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