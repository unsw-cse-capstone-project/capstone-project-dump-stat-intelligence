import * as types from "../types";



export const update_query = (query) => async dispatch => {
    //Fetch query results from backend
    dispatch({
        type : types.QUERY,
        query : query,
        results : []
    })
}


export const clear_query = () => async dispatch => {
    dispatch({
        type : types.CLEAR_QUERY
    })
}