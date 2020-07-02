import * as types from "../types";



export const update_query = (query) => async dispatch => {
    //Fetch query results from backend
    
    //temp testing
    let prac = [
        {name : " one", category : "meh"},
        {name : " 2", category : "meh"},
        {name : " 3", category : "meh"},
        {name : " 4", category : "meh"},
        {name : " 5", category : "meh"},
        {name : " 6", category : "meh"},
        {name : " 7", category : "meh"},
        {name : " 8", category : "meh"},
        {name : " 9", category : "meh"}
    ]
    
    
    dispatch({
        type : types.QUERY,
        query : query,
        results : prac.splice(0,query.length)
    })
}


export const clear_query = () => async dispatch => {
    dispatch({
        type : types.CLEAR_QUERY
    })
}