import * as types from "../types";

const initialState = {
    searchString : "",
    //each one is an object with name and category
    results : [],
    pantryOnly : true,
}


export const searchReducer = (state = initialState, action ) => {
    switch (action.type) {
        case types.SEARCH_TYPE:
            return {
                ...state,
                pantrOnly : action.pantryOnly
            }
        case types.SEARCH:
            return { 
                ...state,
                searchString : action.search,
                results : action.results
            }
        case types.CLEAR_SEARCH:
            return {
                ...initialState
            }
        default:
            return state
    }
}