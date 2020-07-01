import * as types from '../types';
import store from '../store';



export const add = (ingredient, category, expiry) => async dispatch => {
    //DO INTERACTON WITH BACKEND

    let uid = store.getState().auth.uid;


    let newIngredient = {
        category : category,
        name : ingredient,
        expiry : expiry
    }
    dispatch({
        type : types.PANTRY_ADD,
        newIngredient : newIngredient
    })
} 

export const remove = (ingredient, category) => async dispatch => {
    //DO INTERACTION WITH BACKEND

    let uid = store.getState().auth.uid;

    let toRemove = {
        category : category,
        ingredient : ingredient
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