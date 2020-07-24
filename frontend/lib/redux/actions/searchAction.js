import * as types from "../types";
import IngredientAPI from "../../api/ingredient";

/*
SEARCH

    Holds the redux state for the search query to add a new ingredient to running list. 
    IMPORTANTLY, can hold results from pantry only and also backend

    search : {
        queryString : "String they are entering",
        results : [{ingredient}, {}, {}, ...],
        pantryOnly : bool
    }

*/
export const search_type = (pantryOnly) => async dispatch => {
    dispatch({
        type: types.SEARCH_TYPE,
        pantryOnly : pantryOnly
    })
}


export const update_search = (query) => async dispatch => {

    
    const ingredients = await IngredientAPI.getAll();

    let match = [];

    var i;
    for(i = 0; i < ingredients.data.length; i++) {
        if (ingredients.data[i].name.startsWith(query))
            match.push({name: ingredients.data[i].name, category: ingredients.data[i].category.name});
    }

    dispatch({
        type : types.SEARCH,
        query : query,
        results: match
    })
}


export const clear_search = () => async dispatch => {
    dispatch({
        type : types.CLEAR_SEARCH
    })
}