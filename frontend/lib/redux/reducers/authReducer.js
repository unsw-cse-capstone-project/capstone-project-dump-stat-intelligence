import * as types from '../types';

const initialState = {
    isLoggedIn : false,
    uid : null,
    userInfo : {
        first : "Michael",
        last  : "Jameson",
        email : "",
        phone : ""
        
    }
}


export const authReducer = (state=initialState, action) => {
    switch (action.type) {
        case types.LOGIN:
            return {
                ...state,
                isLoggedIn : true
            }
        default:
            return state
    }
} 