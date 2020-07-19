import * as types from "../types";


const initialState = {
    name : null,
    category : null,
    expiry : null
}


export const expiryReducer = (state=initialState, action) => {
    switch (action.type) {
        case types.CHANGE_EXPIRY:
            return {
                ...state,
                expiry : action.expiry,
            }
        case types.LOAD_EXPIRY:
            return {
                name : action.name,
                category : action.category,
                expiry : action.expiry,
            }
        case types.CLEAR_EXPIRY:
            return initialState
        default:
            return state
    }
}