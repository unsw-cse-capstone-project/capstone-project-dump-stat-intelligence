import * as types from "../types";

const initialState = []

export const exploreReducer = (state = initialState, action) => {
    switch(action.type) {
        case types.EXPLORE_ADD:
            let idx = state.indexOf(action.toAdd);
            let tempState = [...state]
            if (idx === -1) {
                tempState.push(action.toAdd);
            }
            return tempState
        case types.EXPLORE_REMOVE:
            idx = state.indexOf(action.toRemove);
            tempState = [...state]
            if (idx !== -1 ) {
                tempState.splice(idx, 1);
            }
            return tempState
        case types.EXPLORE_CLEAR:
            return initialState
        default:
            return state
    }
}