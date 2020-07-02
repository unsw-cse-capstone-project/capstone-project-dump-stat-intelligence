import * as types from '../types';
import store from '../store';



export const add = (ingredient) => async dispatch => {
    //DO INTERACTON WITH BACKEND

    let uid = store.getState().auth.uid;


    let newIngredient = {
        category : ingredient.category,
        name : ingredient.name,
        expiry : ingredient.expiry
    }
    dispatch({
        type : types.PANTRY_ADD,
        newIngredient : newIngredient
    })
} 

export const remove = (ingredient) => async dispatch => {
    //DO INTERACTION WITH BACKEND

    let uid = store.getState().auth.uid;

    let toRemove = {
        category : ingredient.category,
        ingredient : ingredient.ingredient
    }
    dispatch({
        type : types.PANTRY_REMOVE,
        toRemove : toRemove
    })
}

export const create_pantry = () => async dispatch => {
    //GET current pantry from backend

    //CURRENTLY GETS IT LIKE THIS:
    let uid = store.getState().auth.uid;
    
    
    let newPantry = {
        meat : [{name : 'sosig', expiry : 'today'}, {name : 'tofu', expiry : 'today'}],
        veg : [],
        moreVEG : [{name : 'beans'}]
    }
    dispatch({
        type : types.PANTRY_CREATE,
        pantry : newPantry
    })


}