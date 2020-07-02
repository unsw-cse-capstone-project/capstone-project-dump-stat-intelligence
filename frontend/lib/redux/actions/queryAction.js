import * as types from "../types";

/*
QUERY

    Holds the redux state for the search query to add a new ingredient

    query : {
        queryString : "String they are entering",
        results : [{ingredient}, {}, {}, ...]
    }

*/


//NEEDS API
export const update_query = (query) => async dispatch => {
    //parameter query holds the new string to search for

    //INSERT API, take query param and turn into list of possible ingredients
    
    //currently for testing, it just has more options as the string gets longer...
    //prestige bootleg 
    let prac = [
        {name : "one", category : "meh"},
        {name : "2", category : "meh"},
        {name : "3", category : "meh"},
        {name : "4", category : "meh"},
        {name : "5", category : "meh"},
        {name : "6", category : "meh"},
        {name : "7", category : "meh"},
        {name : "8", category : "meh"},
        {name : "9", category : "meh"}
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