import * as types from '../types';

const initialState = {
    isLoggedIn : false,
    uid : null,
    token : null,
    nextPage : null,
    favourites : [],
    owned : [],
    userInfo : {
        first : null,
        last  : null,
        email : null,
        phone : null
        
    }
}


export const authReducer = (state=initialState, action) => {
    switch (action.type) {
        case types.ADD_FAVE:
            //do a check to make sure it's not already a fave
            for (let i = 0; i < state.favourites.length; i++) {
                if (action.recipe.id === state.favourites[i].id) {
                    return {
                        ...state
                    }
                } 
            }
            //Evidently, hasn't been added
            let newFaves = state.favourites;
            newFaves.push(action.recipe);
            return {
                ...state,
                favourites:[...newFaves]
            }
        case types.REMOVE_FAVE:
            for (let i = 0; i < state.favourites.length; i++) {
                if (action.id === state.favourites[i].id) {
                    //delete it!
                    newFaves = state.favourites;
                    newFaves.splice(i,1);
                    return {
                        ...state,
                        favourites:[...newFaves]
                    } 
                }
            }
            return {
                ...state
            }
        case types.NEW_NEXT:
            return {
                ...state,
                nextPage : action.next
            }
        case types.CLEAR_NEXT:
            return {
                ...state,
                nextPage : null
            }
        case types.LOGIN:
            return {
                ...state,
                isLoggedIn : true,
                userInfo : {
                    ...action.userInfo
                },
                uid : action.uid
            }
        case types.LOGOUT:
            return {
                ...initialState,
                isLoggedIn : false,
                token : null
            }
        case types.UPDATE_DEETS:
            return {
                ...state,
                userInfo : {
                    ...action.userInfo
                }
            }
        default:
            return state
    }
} 