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
    let match = [];
    if (query !== "") {
        const ingredients = await IngredientAPI.getAll();
        var i;
        for(i = 0; i < ingredients.data.length; i++) {
            if (ingredients.data[i].name.startsWith(query))
                match.push({name: ingredients.data[i].name, category: ingredients.data[i].category.name});
        }

    }



    dispatch({
        type : types.QUERY,
        query : query,
        results: match.slice(0,10),
    })
}


export const clear_query = () => async dispatch => {
    dispatch({
        type : types.CLEAR_QUERY
    })
}