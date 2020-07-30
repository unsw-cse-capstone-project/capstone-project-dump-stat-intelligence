import * as types from "../types";

const initialState = {
    //Each key is a category and each value is a list of ingredient types

    //EXCEPT for meta tag which holds a list of all the ingredient names
    meta : []
}


export const pantryReducer = (state = initialState, action) => {
    switch (action.type) {
        case types.PANTRY_CHANGE:
            let newOne = state;
            if (newOne[action.category]) {
                for (let j = 0; j < newOne[action.category].length; j++) {
                    if (newOne[action.category][j].name === action.ingredient) {
                        newOne[action.category][j].expiry = action.expiry;
                        return {
                            ...newOne,
                        }
                    }
                }
            }
            return state
            
        case types.PANTRY_GET:
            let newMeta = [];
            for (var cat in action.pantry) {
                for (var ing in action.pantry[cat]) {
                    newMeta.push(ing);
                }
            }
            return {
                ...action.pantry,
                meta : newMeta
            }
        case types.PANTRY_ADD:
            let currCat = []
            //IF CATEGORY ALREADY IN PANTRY, USE CURRENT PANTRY
            if (action.newIngredient.category in state) {
                currCat = state[action.newIngredient.category];
            }
            newMeta = state.meta;
            if (state.meta.indexOf(action.newIngredient.name) === -1) {
                currCat.push({
                    name : action.newIngredient.name,
                    expiry : action.newIngredient.expiry
                })
                newMeta.push(action.newIngredient.name);
            }

            let newState = state;
            newState[action.newIngredient.category] = currCat;
            return {
                ...newState,
                meta : newMeta,
            }
        case types.PANTRY_REMOVE:
            //CASE already removed
            if (!(action.toRemove.category in state)) {
                return state
            }
            let newCat = state[action.toRemove.category];
            //FIND LOCATION OF INGREDIENT
            for (let i = 0; i < newCat.length; i++) {
                if (newCat[i].name === action.toRemove.ingredient) {
                    newCat.splice(i, 1);
                    break;
                } 
            }
            newState = state;
            newState[action.toRemove.category] = newCat;
            if (newCat.length === 0) {
               delete  newState[action.toRemove.category];
            }
            newMeta = state.meta;
            newMeta.splice(newMeta.indexOf(action.toRemove.ingredient), 1);
            return {
                ...newState,
                meta : newMeta
            }

        default:
            return state
    }
}