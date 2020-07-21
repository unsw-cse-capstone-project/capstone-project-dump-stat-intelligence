import * as types from "../types";
import IngredientAPI from "../../api/ingredient";

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
    
    const ingredients = await IngredientAPI.getAll();

    let match = [];

    var i;
    for(i = 0; i < ingredients.data.count; i++) {
        if (ingredients.data.results[i].name.startsWith(query))
            match.push({name: ingredients.data.results[i].name});
    }

    dispatch({
        type : types.QUERY,
        query : query,
        results: match
    })
}


export const clear_query = () => async dispatch => {
    dispatch({
        type : types.CLEAR_QUERY
    })
}