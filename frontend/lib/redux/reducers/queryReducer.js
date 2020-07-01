import * as types from "../types";

const initialState = {
    queryString : "",
    results : []
}


export const queryReducer = (state = initialState, action ) => {
    switch (action.type) {
        case types.QUERY:
            return { 
                queryString : action.query,
                results : action.results
            }
        case types.CLEAR_QUERY:
            return initialState
        default:
            return state
    }
}