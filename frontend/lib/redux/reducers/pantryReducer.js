import * as types from "../types";

const initialState = {
    //Each key is a category and each value is a list of ingredient types
}


export const pantryReducer = (state = initialState, action) => {
    switch (action.type) {
        case types.CREATE:
            return {
                ...action.pantry
            }
        case types.ADD:
            let currCat = {}
            //IF CATEGORY ALREADY IN PANTRY, USE CURRENT PANTRY
            if (action.newIngredient.category in state) {
                currCat = state[action.newIngredient.category];
            }
            currCat[action.newIngredient.category] = {
                name : action.newIngredient.name,
                expiry : action.newIngredient.expiry
            }
            let newState = state;
            newState[action.newIngredient.category] = currCat;
            return {
                ...newState,
            }
        case types.REMOVE:
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
            
            return {
                ...newState
            }

        default:
            return state
    }
}