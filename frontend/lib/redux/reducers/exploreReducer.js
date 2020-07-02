import * as types from "../types";

const initialState = {
    ingredients : []
}

export const exploreReducer = (state = initialState, action) => {
    switch(action.type) {
        case types.EXPLORE_ALL:
            return {
                ...state,
                ingredients : action.newList
            }
        case types.EXPLORE_ADD:
            let idx = state.ingredients.indexOf(action.toAdd);
            let tempList = [...state.ingredients]
            if (idx === -1) {
                tempList.push(action.toAdd);
            }
            return {
                ...state,
                ingredients : tempList
            }
        case types.EXPLORE_REMOVE:
            idx = state.ingredients.indexOf(action.toRemove);
            tempList = [...state.ingredients]
            if (idx !== -1 ) {
                tempList.splice(idx, 1);
            }
            return {
                ...state,
                ingredients : tempList
            }
        case types.EXPLORE_CLEAR:
            return initialState
        default:
            return state
    }
}