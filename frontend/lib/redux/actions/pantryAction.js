import * as types from '../types';
import store from '../store';

/*
PANTRY

    Holds the redux state for the user's pantry ingredients

    pantry : {
        category : [{ingredient}, {}, {}, ...]
    }

*/

//NEEDS API
export const add = (ingredient) => async dispatch => {
    let auth = store.getState().auth;

    if (auth.isLoggedIn) {
        //INSERT API, user is logged in so update pantry on backend

    }

    let newIngredient = {
        category : ingredient.category,
        name : ingredient.name
    }
    dispatch({
        type : types.PANTRY_ADD,
        newIngredient : newIngredient
    })
} 

//NEEDS API
export const remove = (ingredient) => async dispatch => {
    let auth = store.getState().auth;

    if (auth.isLoggedIn) {
        //INSER API, user is logged in so update pantry on backend

    }

    let toRemove = {
        category : ingredient.category,
        ingredient : ingredient.ingredient
    }
    dispatch({
        type : types.PANTRY_REMOVE,
        toRemove : toRemove
    })
}


//NEEDS API
export const create_pantry = () => async dispatch => {
    let auth = store.getState().auth;

    if (auth.isLoggedIn) {
        //INSER API, user is logged in so update pantry on backend

    }
    
    
    let newPantry = {}



    dispatch({
        type : types.PANTRY_CREATE,
        pantry : newPantry
    })


}